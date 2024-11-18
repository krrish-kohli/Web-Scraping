from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keeps Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Creates and configures the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigates to the Cookie Clicker Game
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Hones in on the cookie using ID
cookie = driver.find_element(By.ID, value="cookie")

# Hones in on the items using ID and stores their id attribute
items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

# time
start_time = time.time()
five_min = start_time + 300
timeout = time.time() + 7

while True:
    cookie.click()

    # Runs evey 7 seconds
    if time.time() > timeout:
        # Hones in on the <b> tag using CSS Selectors
        store_items = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        prices = []

        # Converts the text from <b> tag to integer price and stores it in a list
        for item in store_items:
            if item.text != "":
                cost = int(item.text.split("-")[1].strip().replace(",", ""))
                prices.append(cost)

        # Creates a dictionary of store items and prices
        items_cost = {}
        for n in range(len(prices)):
            items_cost[prices[n]] = item_ids[n]

        # Hones in on the cookie count and converts it to an integer
        cookies_earned = driver.find_element(By.ID, value="money").text
        if "," in cookies_earned:
            cookies_earned = cookies_earned.replace(",", "")
        cookies_earned = int(cookies_earned)

        # Checks the items we can currently purchase and stores them in a dictionary
        possible_item_purchase = {}
        for cost, id in items_cost.items():
            if cookies_earned > cost:
                possible_item_purchase[cost] = id

        # Purchases the most expensive item
        if possible_item_purchase:
            most_expensive_item_cost = max(possible_item_purchase)
            most_expensive_item_id = possible_item_purchase[most_expensive_item_cost]

            driver.find_element(By.ID, value=most_expensive_item_id).click()

        # Adds another 7 seconds until the next check
        timeout = time.time() + 7

    # After 5 minutes, breaks the program and displays the cookies per second count
    if time.time() > five_min:
        cookie_per_second = driver.find_element(By.ID, value="cps").text
        print(cookie_per_second)
        break
