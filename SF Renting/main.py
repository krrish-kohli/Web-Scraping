from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

google_form_link = "https://forms.gle/5xJHfDvCL5ZCwyCG7"
zillow_link = "https://appbrewery.github.io/Zillow-Clone/"

# # # # # # # # # # # # # # # # # # # # BeautifulSoup # # # # # # # # # # # # # # # # # # # # # #

# Navigate to Zillow
response = requests.get(zillow_link)
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

# Scraping the link, price and address of property using BeautifulSoup
all_listing_links = soup.find_all(name="a", class_="property-card-link")
all_listing_prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
all_listing_addresses = soup.select(".StyledPropertyCardDataArea-anchor address")

# Creating empty lists to store the links, addresses, and prices of the property
listing_links = []
listing_prices = []
listing_addresses = []

# Updating the lists with the links, addresses, and prices
for link in all_listing_links:
    listing_links.append(link.get("href"))
print(listing_links)

for price in all_listing_prices:
    prices = price.getText().split("+")[0]
    listing_prices.append(prices.split("/mo")[0].strip())
print(listing_prices)

for addresses in all_listing_addresses:
    text = addresses.getText().replace(" | ", " ").strip()
    listing_addresses.append(text)
print(listing_addresses)

# # # # # # # # # # # # # # # # # # # # Selenium # # # # # # # # # # # # # # # # # # # # # #

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the google form
driver.get(google_form_link)

# Updating data of all the properties found on Zillow
for i, j, k in zip(listing_addresses, listing_prices, listing_links):
    # Hone in on input tag using X Path
    time.sleep(3)
    address = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # Hone in on "Submit" button using X Path
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    # Inputting the link, address, and price of each of the property in the google sheet
    address.send_keys(i)
    price.send_keys(j)
    link.send_keys(k)
    # Clicking on the "submit" button
    submit_button.click()
    time.sleep(2)
    # Clicking on "add another response" button
    another_response_button = driver.find_element(By.LINK_TEXT, value="Submit another response")
    another_response_button.click()
