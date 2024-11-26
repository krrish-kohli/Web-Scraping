import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
from dotenv import load_dotenv

load_dotenv()


class InstaFollower:

    def __init__(self):
        # Keep browser open so you can manually log out
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(4.2)

        # Check if the cookie warning is present on the page
        decline_cookies_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
        cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)
        if cookie_warning:
            # Dismiss the cookie warning by clicking an element or button
            cookie_warning[0].click()

        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")

        username.send_keys(os.environ.get("USERNAME"))
        password.send_keys(os.environ.get("PASSWORD"))

        time.sleep(2.1)
        password.send_keys(Keys.ENTER)

        time.sleep(4.3)
        # Click "Not now" and ignore Save-login info prompt
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

    def find_followers(self):
        time.sleep(5)
        # Will bring up the followers of an account
        self.driver.get(f"https://www.instagram.com/{os.environ.get("SIMILAR_ACCOUNT")}/followers")

        time.sleep(8.2)
        followers = self.driver.find_element(By.XPATH, value="//a[contains(text(), 'followers')]")
        followers.click()

        # The xpath of the modal will change over time. Update yours accordingly.
        time.sleep(1.7)
        modal_xpath = "/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(10):
            # Scroll the window
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        # "Follow" buttons of the followers of SIMILAR ACCOUNT.
        all_buttons = self.driver.find_elements(By.XPATH, value="//div[text(), 'Follow']")

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
