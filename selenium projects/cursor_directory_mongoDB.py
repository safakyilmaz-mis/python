from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from pymongo import MongoClient
import os

# MongoDB connection string
mongo_uri = "mongodb://root:p2f9FXGxhdmPtEp8rmOv6ykKm0v8i1FNTmBWUqcDk9O0BiDsAzlDdQCLYQKuFc4R@95.217.39.116:5424/?directConnection=true"

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client['cursor_directory']
collection = db['cursor_codes']

# Chrome seçeneklerini ayarla
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Tarayıcıyı tam ekran başlat

# ChromeDriver'ı başlat
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://cursor.directory/"
driver.get(url)

try:
    element = driver.find_element(By.TAG_NAME, "body")
    print("Sayfa başarıyla yüklendi.")
except Exception as e:
    print(f"Sayfa yüklenirken bir hata oluştu: {e}")

cursor_data = {}  # MongoDB'ye kaydedilecek veri için sözlük oluştur

try:
    button_index = 1
    while True:
        try:
            subject_button = driver.find_element(By.XPATH, f'/html/body/div[2]/div/aside/div[2]/div/div/div/button[{button_index}]')
            subject = subject_button.text.split("\n")[0]
            cursor_data[subject] = []

            cursor_index = 1
            while True:
                try:
                    cursor_element = driver.find_element(By.XPATH, f'//*[@id="{subject}"]/div/div[{cursor_index}]/div[1]/a/div/div/div/code')
                    cursor_code = cursor_element.text
                    cursor_data[subject].append(cursor_code)
                    print(f"Cursor code successfully scraped: {cursor_code}")
                    cursor_index += 1
                except NoSuchElementException:
                    break  # No more cursors for this subject

            subject_button.click()  # Move to next subject
            button_index += 1
        except NoSuchElementException:
            print("Reached the last subject. Stopping the scraping process.")
            break

    # Save data to MongoDB
    collection.insert_one(cursor_data)

    total_cursors = sum(len(cursors) for cursors in cursor_data.values())
    print(f"\n\nTotal of {total_cursors} Cursor Directory codes scraped and saved to MongoDB.")

except Exception as e:
    print(f"An error occurred while scraping cursor codes: {e}")

finally:
    # Close MongoDB connection
    client.close()
    # Tarayıcıyı kapat
    driver.quit()
