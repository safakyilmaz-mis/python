from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Selenium WebDriver'ı başlatın
chrome_options = Options()
chrome_options.add_argument("--headless")  # Tarayıcı penceresini göstermemek için
service = Service('C:\Users\Safak Yilmaz\Downloads\chrome-win64')  # Buraya kendi chromedriver yolunuzu ekleyin
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Web sayfasını açın
    driver.get('https://servers.fivem.net/')  # Buraya kendi web sayfanızın URL'sini ekleyin

    # Sayfanın tamamen yüklenmesini bekleyin
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'img'))
    )

    # Tüm img elementlerini seçin
    img_elements = driver.find_elements(By.TAG_NAME, 'img')

    # img alt attribute'larını almak için bir liste oluşturun
    img_alts = []

    # Sayfayı kaydırarak tüm img alt attribute'larını toplama işlemi
    while True:
        # Mevcut img elementlerinin alt attribute'larını ekleyin
        for img in img_elements:
            alt_text = img.get_attribute('alt')
            if alt_text and alt_text not in img_alts:
                img_alts.append(alt_text)
        
        # Sayfayı kaydırın
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        
        # Sayfanın tamamen yüklenmesini bekleyin
        time.sleep(2)

        # Yeni img elementlerini al
        new_img_elements = driver.find_elements(By.TAG_NAME, 'img')
        
        # Eğer yeni img elementleri yoksa, döngüyü sonlandırın
        if len(new_img_elements) == len(img_elements):
            break

        # img elementleri listesini güncelle
        img_elements = new_img_elements

finally:
    # WebDriver'ı kapatın
    driver.quit()

# Sonuçları yazdırın
for alt in img_alts:
    print(alt)
