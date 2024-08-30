from bs4 import BeautifulSoup as bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import pymongo
import json

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Start WebDriver
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.rahulpnath.com/blog/')

# Postları bulmak için sınıf adını belirle
scraped_data = []
scroll_pause_time = 2  # Scroll işlemi sonrası bekleme süresi

while True:
    posts = driver.find_elements(By.CLASS_NAME, 'c-post-card')
    
    for post in posts:
        # Resim linki
        try:
            image_tag = post.find_element(By.CLASS_NAME, 'c-post-card__image')
            srcset = image_tag.get_attribute('srcset')
            if srcset:
                image_url = srcset.split(",")[-1].split()[0]  # En yüksek çözünürlüklü URL'yi alır
            else:
                image_url = image_tag.get_attribute('src')  # Eğer `srcset` yoksa, `src`yi alır
        except NoSuchElementException:
            image_url = 'No Image'



        
        # Başlık
        try:
            title_tag = post.find_element(By.CLASS_NAME, 'c-post-card__title')
            title = title_tag.text.strip()
        except:
            title = 'No Title'
        
        # Kısa açıklama
        try:
            excerpt_tag = post.find_element(By.CLASS_NAME, 'c-post-card__excerpt')
            excerpt = excerpt_tag.text.strip()
        except:
            excerpt = 'No Excerpt'
        
        # Post linki
        try:
            link_tag = title_tag.find_element(By.TAG_NAME, 'a')
            post_link = link_tag.get_attribute('href')
        except:
            post_link = 'No Link'
        
        if post_link and image_url:  # Ensure required fields are present
            scraped_data.append({
                "title": title,
                "photo": 'https://www.rahulpnath.com'+image_url,
                "short_description": excerpt,
                "link": post_link
            })
    
    # Sayfanın sonuna ulaştığımızı kontrol edin (daha fazla "Older Posts" butonu yoksa)
    try:
        older_posts = driver.find_element(By.XPATH, '//*[@id="main-content"]/div/div[1]/div[2]/div/div/button')
    except NoSuchElementException:
        break  # Daha fazla içerik yok, döngüden çık
    
    # Sayfayı aşağı kaydır
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Scroll işleminden sonra bekleme süresi
    time.sleep(scroll_pause_time)

# Save the data to a JSON file
json_file_name = './scraped_data_from_raul_nath.json'  # name of JSON file
try:
    with open(json_file_name, 'w', encoding='utf-8') as file:
        json.dump(scraped_data, file, ensure_ascii=False, indent=4)
    print(f'Successfully saved scraped data to {json_file_name}.')
except Exception as e:
    print(f'An error occurred while saving to JSON: {e}')


# # MongoDB connection
# client = pymongo.MongoClient('mongodb://root:p2f9FXGxhdmPtEp8rmOv6ykKm0v8i1FNTmBWUqcDk9O0BiDsAzlDdQCLYQKuFc4R@95.217.39.116:5424/?directConnection=true')
# db = client['code_maze_all_pages_final']  # Replace with your database name
# collection = db['contents']  # Replace with your collection name

# # Insert scraped data into MongoDB
# try:
#     result = collection.insert_many(scraped_data)
#     print(f'Inserted {len(result.inserted_ids)} articles into MongoDB.')
# except Exception as e:
#     print(f'An error occurred: {e}')
    
