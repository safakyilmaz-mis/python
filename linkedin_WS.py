from seleniumwire import webdriver

proxy = '94.74.159.94:59100'

# If the proxy requires authentication
proxy_options = {
    'proxy': {
        'https': f'https://alpertunga04:yPMK4v4zVL@{proxy}',
        'http': f'http://alpertunga04:yPMK4v4zVL@{proxy}'
    }
}

driver = webdriver.Chrome(seleniumwire_options=proxy_options)

driver.get("https://whatismyipaddress.com/")