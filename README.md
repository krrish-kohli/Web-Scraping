# Web Scraping

This repository contains projects showcasing different aspects of web scraping using Python. Each project focuses on practical examples of data extraction, manipulation, filtering, and automation, demonstrating essential skills for working with structured data from web pages. Projects include scraping top movie lists, educational web pages, generating music playlists from historical Billboard Hot 100 charts using the Spotipy API, tracking product prices on Amazon, and automating gameplay using Selenium.

---

### 1. 100 Movies to Watch
This project scrapes a webpage to generate a list of the top 100 recommended movies to watch. It uses **BeautifulSoup** to parse the webpage and extract movie titles for further processing and management.

#### Project Details:
- **Data Source**: [URL](https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/) containing the list of movies
- **Features**:
  - Scrape and save the list of top 100 movies
  - Display the movie list
  - Search for specific titles
  - Randomly recommend a movie to watch
  - Optionally, mark movies as watched
- **Tools Used**:
  - **BeautifulSoup**: For scraping the website for the provided URL and extracting movie titles
- **File(s)**:
  - `main.py` - The main script for scraping and processing the movie list
  - `movies.txt` - Contains the 100 movie titles scraped from the website

---

### 2. bs4
This project demonstrates basic web scraping from a static HTML file using **BeautifulSoup**. It extracts key information such as the name, profession, and links from a mock personal webpage.

#### Project Details:
- **Data Source**: Static HTML file (`website.html`)
- **Features**:
  - Parse HTML to extract key data points
  - Display structured information in the console
- **Tools Used**:
  - **BeautifulSoup**: For parsing the static HTML file and extracting content
- **File(s)**:
  - `main.py` - The script for parsing `website.html`
  - `website.html` - The source file containing data to scrape

---

### 3. Musical Time Machine
This project scrapes the Billboard Hot 100 to generate a playlist of the top 100 songs from a specified date in history. It uses **BeautifulSoup** to retrieve song titles from Billboard and the Spotify API to create a playlist with these songs, allowing users to experience popular music from any chosen date.

#### Project Details:
- **Data Source**: [Billboard Hot 100](https://www.billboard.com/charts/hot-100/) (scraped) and Spotipy API
- **Features**:
  - Scrape the Billboard Hot 100 for top songs from a specific date
  - Use Spotify API to create and save a playlist with these songs
  - Output a link to the generated playlist
- **Tools Used**:
  - **BeautifulSoup**: For scraping Billboard's website
  - **Spotipy API**: For playlist creation and interaction
- **File(s)**:
  - `main.py` - The main script for scraping Billboard and interacting with Spotify
  - `token.txt` - Contains authentication details for Spotipy API access

---

### 4. Amazon Price Tracker
This project tracks the price of a specific product on Amazon and notifies the user when the price drops below a certain threshold. It uses **BeautifulSoup** to scrape product details and prices dynamically.

#### Project Details:
- **Data Source**: [Amazon product page](https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6)
- **Features**:
  - Scrape the current price of a product from Amazon
  - Compare the price against a user-defined threshold
  - Send a notification when the price drops below the threshold
- **Tools Used**:
  - **BeautifulSoup**: For parsing Amazon product pages
- **File(s)**:
  - `main.py` - The main script for tracking and comparing prices

---

### 5. Automated Game Playing Bot
This project automates gameplay for the **Cookie Clicker** game using **Selenium**. The bot plays the game by continuously clicking the cookie and purchasing upgrades to maximize the cookies-per-second rate. It demonstrates how to interact with dynamic web elements using Selenium WebDriver.

#### Project Details:
- **Game Source**: [Cookie Clicker](https://orteil.dashnet.org/experiments/cookie/)
- **Features**:
  - Automatically clicks the cookie to increase the score
  - Tracks available upgrades and purchases the most expensive affordable item
  - Uses a timer to control gameplay flow and purchases
  - Retrieves the final cookies-per-second rate after 5 minutes
- **Tools Used**:
  - **Selenium WebDriver**: For browser automation and interaction with dynamic game elements
- **File(s)**:
  - `main.py` - The main script for automating gameplay

---

### 6. Automated Tinder Swiping Bot
This project automates swiping on **Tinder** using **Selenium**. The bot logs into Tinder using Facebook authentication, manages pop-ups, and performs automated right swipes upto Tinder's daily limit. It demonstrates advanced browser automation techniques for handling dynamic elements and managing user sessions.

#### Project Details:
- **Platform**: [Tinder](https://tinder.com/)
- **Features**:
  - Automates the login process via Facebook (requires manual syncing due to dynamic attributes)
  - Handles location, notification, and cookie pop-ups automatically
  - Performs automated right swipes for 100 profiles (Tinder's daily limit without subscription)
  - Detects and dismisses match pop-ups for seamless swiping
- **Tools Used**:
  - **Selenium WebDriver**: For browser automation and interaction with Tinder
- **File(s)**:
  - `main.py` - The main script for automating Tinder login and swiping

---