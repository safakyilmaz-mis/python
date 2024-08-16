from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Chrome seçeneklerini ayarlama
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# WebDriver'ı başlatma
driver = webdriver.Chrome(options=chrome_options)

# Web sayfasını açma
driver.get("https://servers.fivem.net/")
time.sleep(5)  # Sayfanın yüklenmesi için bekleme

# Önceden alınan alt değerlerin listesi
seen_alts = set()

def get_elements_alt():
    try:
        # Tüm img elementlerini bulma
        img_elements = WebDriverWait(driver, 50).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="cfxui-root"]//div[contains(@class, "ussYjSxP")]//img'))
        )
        new_alts = set()
        
        # Her öğenin 'alt' özelliğini alma
        for img_element in img_elements:
            time.sleep(1) # Sayfanın
            alt_value = img_element.get_attribute("alt")
            if alt_value and alt_value not in seen_alts:
                print("Alt Değeri: ", alt_value)
                seen_alts.add(alt_value)
                new_alts.add(alt_value)
        
        return bool(new_alts)
    except (NoSuchElementException, TimeoutException) as e:
        print(f"Hata: {e}. Öğeler bulunamadı.")
        return False

# Sonsuz kaydırma ve veri alma işlemi
last_height = driver.execute_script("return document.body.scrollHeight")
scroll_attempts = 0

while True:
    time.sleep(1)
    has_new_content = get_elements_alt()
    
    # Sayfayı kaydırma
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Sayfanın kaydırılmasının tamamlanması ve yeni içeriklerin yüklenmesi için bekleme
    time.sleep(5)  # İçeriğin yüklenmesi için yeterli süre

    # Yeni sayfa yüksekliğini kontrol etme
    new_height = driver.execute_script("return document.body.scrollHeight")
    
    # Eğer yeni yüklenmiş bir içerik yoksa ve yükseklik değişmediyse çık
    if new_height == last_height:
        scroll_attempts += 1
        if scroll_attempts >= 3:  # 3 deneme sonrası hala yüklenmiyorsa çık
            print("Yeni içerik yüklenmedi.")
            break
    else:
        scroll_attempts = 0  # İçerik yüklenirse deneme sayısını sıfırla
    
    last_height = new_height

# Tarayıcıyı kapatma
driver.quit()









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
service = Service('path/to/chromedriver')  # Buraya kendi chromedriver yolunuzu ekleyin
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Web sayfasını açın
    driver.get('https://example.com')  # Buraya kendi web sayfanızın URL'sini ekleyin

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
