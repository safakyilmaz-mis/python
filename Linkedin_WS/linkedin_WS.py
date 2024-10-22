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

search_button = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
search_button.click()

