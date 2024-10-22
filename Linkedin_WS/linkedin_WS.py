import time
from seleniumwire import webdriver
from selenium.webdriver.common.by import By

proxy = '94.74.159.94:59100'

# If the proxy requires authentication
proxy_options = {
    'proxy': {
        'https': f'https://alpertunga04:yPMK4v4zVL@{proxy}',
        'http': f'http://alpertunga04:yPMK4v4zVL@{proxy}'
    }
}

driver = webdriver.Chrome(seleniumwire_options=proxy_options)

driver.get("https://www.linkedin.com/search/results/CONTENT/")

time.sleep(5)

email = driver.find_element(By.XPATH, '//*[@id="username"]')
email.click()

email.send_keys('xxxxxx@gmail.com')

password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.click()
password.send_keys('xxxxxx')

login = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[4]/button')
login.click()

input("Press Enter to close the browser...")

# The browser will only close after you press Enter in the console
driver.quit()

# search_button = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
# search_button.click()

