import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

accept_cookies = driver.find_element(By.CLASS_NAME, "fc-button-label")
accept_cookies.click()

time.sleep(3)
english_lan = driver.find_element(By.ID, value='langSelect-EN')
english_lan.click()
time.sleep(2)

start_time = time.time()
game_is_on = True
prices = []
while game_is_on:
    click_cookie = driver.find_element(By.CSS_SELECTOR, "#bigCookie")
    click_cookie.click()

    current_time = time.time() + 1
    pause_timer = current_time - start_time
    # print(driver.find_element(By.ID, "cookies").text.split(" ")[0])
    # print(driver.find_element(By.ID, f"productPrice{2}").text)
    money = int(driver.find_element(By.ID, "cookies").text.split(" ")[0].replace(",", ""))
    if int(pause_timer) % 30 == 0:
        for i in range(4, -1, -1):
            max_price = (driver.find_element(By.XPATH, f'//*[@id="productPrice{i}"]'))
            edited_max_price = max_price.text.replace(",", "")
            if edited_max_price != "":
                edited_max_price = int(edited_max_price)
                # print(edited_max_price)
                if money > edited_max_price:
                    # print(edited_max_price)
                    click_max = driver.find_element(By.XPATH, f'//*[@id="product{i}"]')
                    click_max.click()

    if int(pause_timer) % 300 == 0:
        game_is_on = False
print(driver.find_element(By.ID, "cookies").text.split("\n")[1])
