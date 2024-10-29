import time
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

proxy = '94.74.159.94:59100'

# If the proxy requires authentication
proxy_options = {
    'proxy': {
        'https': f'https://alpertunga04:yPMK4v4zVL@{proxy}',
        'http': f'http://alpertunga04:yPMK4v4zVL@{proxy}'
    }
}

# Add options to keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(seleniumwire_options=proxy_options, options=chrome_options)

driver.get("https://www.linkedin.com/search/results/CONTENT/")

# Wait for the email field to be visible
email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)
email.send_keys('xxxxx@gmail.com')

password = driver.find_element(By.ID, 'password')
password.send_keys('xxxxx')

login = driver.find_element(By.XPATH, '//button[@type="submit"]')
login.click()

# Keep the script running
input("Press Enter to close the browser...")

# The browser will only close after you press Enter in the console
driver.quit()

# search_button = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
# search_button.click()
