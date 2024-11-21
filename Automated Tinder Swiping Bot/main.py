from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
from dotenv import load_dotenv
import os

# Loading the variables from the .env file
load_dotenv()

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to Tinder
driver.get("https://tinder.com/")

# Specifying the window handles
base_window = driver.window_handles[0]
driver.switch_to.window(base_window)

# Click on login button using its X Path
time.sleep(3)
login_button = driver.find_element(By.XPATH, value='//*[@id="u-825090168"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
login_button.click()

# Click on login with Facebook button
time.sleep(1)
login_with_facebook = driver.find_element(By.CLASS_NAME, value="Mend\\(a\\)")
login_with_facebook.click()

# Switching to Facebook's window
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)


# Logging in through Faceboook
time.sleep(1)
email = driver.find_element(By.NAME, value="email")
email.send_keys(os.getenv("EMAIL"))

password = driver.find_element(By.NAME, value="pass")
password.send_keys(os.getenv("PASS"))

fb_login_button = driver.find_element(By.ID, value="loginbutton")
fb_login_button.click()

# YOU WILL HAVE TO SYNC IT MANUALLY BECAUSE FACEBOOK'S SECURITY CHANGES THE ATTRIBUTES OF THAT WEBPAGE EVERYTIME
# CLICK THE "CONTINUE AS {YOUR_USERNAME} BUTTON"

# Switching back to the Tinder window
time.sleep(15)
driver.switch_to.window(base_window)
# print(driver.title)

# Managing the request pop-ups
location_allowance = driver.find_element(By.XPATH, value='//*[@id="u1741496052"]/div/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')
location_allowance.click()

time.sleep(1)
no_notification = driver.find_element(By.XPATH, value='//*[@id="u1741496052"]/div/div[1]/div/div/div[3]/button[2]/div[2]/div[2]/div')
no_notification.click()

time.sleep(1)
accept_cookies = driver.find_element(By.XPATH, value='//*[@id="u-825090168"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div')
accept_cookies.click()

# Swiping people right
for n in range(100):  # Because Tinder allows only 100 likes per day without subscription
    time.sleep(7)

    try:
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_RIGHT)

    except ElementClickInterceptedException:
        try:
            # Catches the case when there is a "Matched" pop-up in front of the "Like" button
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded
        except NoSuchElementException:
            time.sleep(2)
