from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Chrome seçeneklerini ayarla
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Tarayıcıyı tam ekran başlat

# ChromeDriver'ı başlat
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Verilen URL'ye git
url = "https://cursor.directory/"
driver.get(url)

# İsteğe bağlı: Sayfanın yüklendiğini doğrulamak için bir element bul
try:
    element = driver.find_element(By.TAG_NAME, "body")
    print("Sayfa başarıyla yüklendi.")
except Exception as e:
    print(f"Sayfa yüklenirken bir hata oluştu: {e}")

# Tarayıcıyı açık bırak
input("Tarayıcıyı kapatmak için Enter tuşuna basın...")

# Tarayıcıyı kapat
driver.quit()
