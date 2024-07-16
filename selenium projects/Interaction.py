from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# result = driver.find_element(By.XPATH,'//*[@id="articlecount"]/a[1]').text

name = driver.find_element(By.NAME, "fName")
name.send_keys("Safak")

sname = driver.find_element(By.NAME, "lName")
sname.send_keys("Yilmaz")

email = driver.find_element(By.NAME, "email")
email.send_keys("Safakyilmazz@yandex.com")

click = driver.find_element(By.CLASS_NAME, "btn-primary")
click.click()
