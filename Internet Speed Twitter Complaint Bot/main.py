from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

PROMISED_DOWN = 200
PROMISED_UP = 100
TWITTER_EMAIL = os.environ.get("your_email")
TWITTER_PASSWORD = os.environ.get("your_twitter_password")


class InternetSpeedTwitterBot:

    def __init__(self):
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP
        # Keep Chrome browser open after program finishes
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        # Create and configure the Chrome webdriver
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def get_internet_speed(self):
        # Navigate to Speedtest
        self.driver.get("https://www.speedtest.net/")

        # Hone in on the "Go" button using Class Name
        go = self.driver.find_element(By.CLASS_NAME, value="start-text")
        go.click()

        time.sleep(60)

        # Getting the values of the download and upload speed
        down_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        up_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        # print(f"down: {down_speed} \nup: {up_speed}")
        return float(down_speed), float(up_speed)

    def tweet_at_provider(self, up_speed: float, down_speed: float):
        self.up = up_speed
        self.down = down_speed

        time.sleep(5)

        # Navigate to X
        self.driver.get("https://www.x.com/login")
        time.sleep(5)

        # Fill in your email for twitter
        login = self.driver.find_element(By.NAME, value="text")
        login.send_keys(TWITTER_EMAIL)

        # Click the "Next" button
        next_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
        next_button.click()

        time.sleep(15)

        # Fill in your password
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(TWITTER_PASSWORD)

        # Click the "Log in" button
        login_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span/span')
        login_button.click()

        time.sleep(3)

        # If the Download or upload speed is lower than promised by the Internet Provider, post a tweet
        if self.up < PROMISED_UP or self.down < PROMISED_DOWN:
            # Write the tweet
            post_text = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            post_text.click()
            post_text.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
            # Click the "Post" button to post the tweet
            post_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
            post_button.click()


speed_twitter_bot = InternetSpeedTwitterBot()
internet_speed = speed_twitter_bot.get_internet_speed()
up = internet_speed[0]
down = internet_speed[1]
time.sleep(5)
speed_twitter_bot.tweet_at_provider(up, down)
