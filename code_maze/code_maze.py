from bs4 import BeautifulSoup as bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import json
import pymongo

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#Start WebDriver
driver = webdriver.Chrome(options=chrome_options)

#Go to site
driver.get("https://code-maze.com/latest-posts-on-code-maze/?et_blog")

#Lists
links = []
photos = []
titles = []
shrt_des = []

#Go to next page and parse datas
while True:
    #Reject cookies
    time.sleep(5)
    try:
        cookie_response = driver.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')
        cookie_response.click()
    except NoSuchElementException:
        pass

    #Get page's source and parse with bs4
    response = bs4(driver.page_source, "html.parser")

    #Links
    for a in response.find_all('a', class_="entry-featured-image-url", href=True):
        links.append(a['href'])

    #Photos
    image_tags = response.find_all("img")
    for image_tag in image_tags:
        img_src = image_tag.get("src")
        if img_src.startswith("data:image/svg+xml") or img_src == "https://code-maze.com/wp-content/uploads/2021/02/Code-Maze-Logo-White-Text-Transparent-Small.png":
            continue
        else:
            photos.append(img_src)

    #Titles
    for a in response.find_all('h2', class_="entry-title"):
        titles.append(a.text)

    #Short Descriptions
    for a in response.find_all('div', class_="post-content-inner"):
        shrt_des.append(a.text)

    #Next page
    try:
        older_post = driver.find_element(By.XPATH, '//*[@id="et-boc"]/div/div/div/div/div/div[1]/div/div/div[2]/nav/div/div[1]/a/span')
        older_post.click()
    except NoSuchElementException:
        break

#write datas to file which collected
dict_maze = {titles[i]: [photos[i], shrt_des[i], links[i]] for i in range(len(links))}
with open('dictionary_maze.json', 'a', encoding='utf-8') as f:
    json.dump(dict_maze, f, ensure_ascii=False, indent=4)


client = pymongo.MongoClient('mongodb://username:password@host:port/?directConnection=true')
db = client.db.quotes
try:
    db.insert_many(dict_maze)
    print(f'inserted {len(dict_maze)} articles')
except:
    print('an error occurred quotes were not stored to db')