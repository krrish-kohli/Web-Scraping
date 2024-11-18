# Web Scraping

This repository contains projects showcasing different aspects of web scraping using Python. Each project focuses on practical examples of data extraction, manipulation, and filtering, demonstrating essential skills for working with structured data from web pages. Projects include scraping top movie lists, educational web pages, generating music playlists from historical Billboard Hot 100 charts using the Spotify API, and tracking product prices on Amazon.

---

## Projects

### 1. bs4
This project demonstrates basic web scraping from a static HTML file using BeautifulSoup. It extracts key information such as the name, profession, and links from a mock personal webpage.

#### Project Details:
- **Data Source**: Static HTML file (`website.html`)
- **Features**:
  - Parse HTML to extract key data points
  - Display structured information in the console
- **File(s)**:
  - `main.py` - The script for parsing `website.html`
  - `website.html` - The source file containing data to scrape

---

### 2. 100 Movies to Watch
This project scrapes a webpage to generate a list of the top 100 recommended movies to watch. The URL of the page to scrape is provided in the file, and the project uses Beautiful Soup to extract each movie title, allowing further processing and management of the list.

#### Project Details:
- **Data Source**: URL containing the list of movies
- **Features**:
  - Scrape and save the list of top 100 movies
  - Display the movie list
  - Search for specific titles
  - Randomly recommend a movie to watch
  - Optionally, mark movies as watched
- **File(s)**:
  - `main.py` - The main script for scraping and processing the movie list
  - `movies.txt` - Contains the URL of the page to scrape

---

### 3. Musical Time Machine
This project scrapes the Billboard Hot 100 to generate a playlist of the top 100 songs from a specified date in history. It uses BeautifulSoup to retrieve song titles from Billboard and the Spotify API to create a playlist with these songs, allowing users to experience popular music from any chosen date.

#### Project Details:
- **Data Source**: Billboard Hot 100 (scraped) and Spotify API
- **Features**:
  - Scrape the Billboard Hot 100 for top songs from a specific date
  - Use Spotify API to create and save a playlist with these songs
  - Adds the playlist to the user's Spotify account (only if the user provides his Spotify username)
- **File(s)**:
  - `main.py` - The main script for scraping Billboard and interacting with Spotify API
  - `token.txt` - Contains authentication details for Spotify API access

---

### 4. Amazon Price Tracker
This project tracks the price of a specific product on Amazon and notifies the user when the price drops below a certain threshold. It demonstrates how to scrape dynamic content and handle headers to avoid detection by web servers.

#### Project Details:
- **Data Source**: Amazon product page
- **Features**:
  - Scrape the current price of a product from Amazon
  - Compare the price against a user-defined threshold
  - Send an email when the price drops below the threshold
- **File(s)**:
  - `main.py` - The main script for tracking and comparing prices

---
