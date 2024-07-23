import time

PROMISED_DOWN = 1000
PROMISED_UP = 300
WEBSITE = 'https://x.com/home'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class InternetSpeedTwitterBot:
    def __init__(self):
        self.results = []
        self.down_speed = self.speed_test_part
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def speed_test_part(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(3)
        reject_cookies = self.driver.find_element(By.XPATH, '//*[@id="onetrust-reject-all-handler"]')
        reject_cookies.click()
        time.sleep(3)
        start_test = self.driver.find_element(By.XPATH,
                                              '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                              '1]/a/span[4]')
        start_test.click()
        time.sleep(50)
        click_app_down = self.driver.find_element(By.XPATH,
                                                  '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                  '3]/div/div[8]/div/div/div[2]/a')
        click_app_down.click()

        self.down_speed = self.driver.find_element(By.XPATH,
                                                   '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                   '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.results.append(self.down_speed.text)

        self.up_speed = self.driver.find_element(By.XPATH,
                                                 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                 '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.results.append(self.up_speed.text)

    def twitter_post(self):
        self.driver.get('https://x.com/')
        time.sleep(5)

        refuse_cookies = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div/div[1]/div/div/div/div[2]/button['
                                                  '2]/div/span/span')
        refuse_cookies.click()
        time.sleep(1)

        sign_in = self.driver.find_element(By.XPATH,
                                           '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div['
                                           '3]/div[3]/a/div/span/span')
        sign_in.click()

        time.sleep(3)
        user_name = self.driver.find_element(By.XPATH,
                                             '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                             '2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        user_name.send_keys("@YOUR_USERNAME")

        time.sleep(3)
        next_user_name = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                  '2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
        next_user_name.click()

        time.sleep(3)
        user_password = self.driver.find_element(By.XPATH,
                                                 '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                 '2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div['
                                                 '2]/div[1]/input')
        user_password.send_keys("YOUR_PASSWORD")

        time.sleep(3)
        next_user_pass = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                  '2]/div/div/div[2]/div[2]/div[2]/div/div['
                                                  '1]/div/div/button/div/span/span')
        next_user_pass.click()

        time.sleep(3)
        click_new_tweet = self.driver.find_element(By.XPATH,
                                                   '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                   '1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                   '1]/div/div/div/div/div/div/div/div/div/div/div/div['
                                                   '1]/div/div/div/div/div/div[2]/div/div/div/div')
        click_new_tweet.click()

        time.sleep(3)
        tweet_enter = self.driver.find_element(By.XPATH,
                                               '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div['
                                               '3]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                               '1]/div/div/div/div/div/div/div/div/div/div/div/div['
                                               '1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_enter.send_keys(
            f"Hey @tmobilecenter, Why am I paying for 900 mbps download / 300 mbps upload and getting; download speed: "
            f"{self.results[0]} mbps / upload speed: {self.results[1]} mbps?")

        post_tweet = self.driver.find_element(By.XPATH,
                                              '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div['
                                              '3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div['
                                              '2]/div/div/div/button/div/span/span')
        post_tweet.click()


speedtest = InternetSpeedTwitterBot()
speedtest.speed_test_part()
speedtest.twitter_post()
