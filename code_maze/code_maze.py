from bs4 import BeautifulSoup as bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import pymongo


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Start WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Go to site
driver.get("https://code-maze.com/latest-posts-on-code-maze/?et_blog")

# Initialize list to store scraped data
scraped_data = []

# Go to next page and parse data
while True:
    # Reject cookies
    time.sleep(5)
    try:
        cookie_response = driver.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')
        cookie_response.click()
    except NoSuchElementException:
        pass

    # Get page's source and parse with bs4
    response = bs4(driver.page_source, "html.parser")

    # Find all articles on the page
    articles = response.find_all('article')

    for article in articles:
        # Get the link
        link_tag = article.find('a', class_="entry-featured-image-url", href=True)
        link = link_tag['href'] if link_tag else None

        # Get the photo
        img_tag = article.find("img")
        img_src = img_tag.get("src") if img_tag else None
        if img_src and (img_src.startswith("data:image/svg+xml") or img_src == "https://code-maze.com/wp-content/uploads/2021/02/Code-Maze-Logo-White-Text-Transparent-Small.png"):
            img_src = None  # Exclude unwanted images

        # Get the title
        title_tag = article.find('h2', class_="entry-title")
        title = title_tag.text if title_tag else None

        # Get the short description
        shrt_des_tag = article.find('div', class_="post-content-inner")
        shrt_des = shrt_des_tag.text if shrt_des_tag else None

        # Store the data in a dictionary and append to list
        if title and link:  # Ensure required fields are present
            scraped_data.append({
                "title": title,
                "photo": img_src,
                "short_description": shrt_des,
                "link": link
            })

    # Next page
    try:
        older_post = driver.find_element(By.XPATH, '//*[@id="et-boc"]/div/div/div/div/div/div[1]/div/div/div[2]/nav/div/div[1]/a/span')
        older_post.click()
    except NoSuchElementException:
        break

# MongoDB connection
client = pymongo.MongoClient('mongodb://root:p2f9FXGxhdmPtEp8rmOv6ykKm0v8i1FNTmBWUqcDk9O0BiDsAzlDdQCLYQKuFc4R@95.217.39.116:5424/?directConnection=true')
db = client['code_maze_all_pages_final']  # Replace with your database name
collection = db['contents']  # Replace with your collection name

# Insert scraped data into MongoDB
try:
    result = collection.insert_many(scraped_data)
    print(f'Inserted {len(result.inserted_ids)} articles into MongoDB.')
except Exception as e:
    print(f'An error occurred: {e}')
