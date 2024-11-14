# Web Scraping

This repository contains projects that demonstrate web scraping and data manipulation using Python. Each project is designed to highlight specific scraping techniques, data processing, and file handling.

## Projects

### 1. bs4
A web scraping project that uses the Beautiful Soup (`bs4`) library to extract information from articles and identify the article with the highest upvotes. This project demonstrates parsing HTML elements, accessing data, and filtering based on criteria.

#### Project Details:
- **Scraping Target**: Articles on a sample website
- **Data Extracted**:
  - Article titles and content
  - Upvote counts for each article
  - The article with the highest upvotes
- **File(s)**: 
  - `main.py` - The script containing the scraping logic

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

## 3. Musical Time Machine
The **Musical Time Machine** project scrapes data from the Billboard Hot 100 and uses the Spotify API to create a playlist of the top 100 songs from a specified date in history. Users can input a date, and the program will retrieve the Billboard Hot 100 songs from that time, compiling them into a Spotify playlist to recreate the music experience of that era.

#### Project Details:
- **Data Source**: Billboard Hot 100 (scraped) and Spotify API
- **Features**:
  - Scrape the Billboard Hot 100 for top songs from a specific date
  - Connects to the Spotify API using an OAuth token for playlist creation and modification.
  - Compiles the top 100 songs into a Spotify playlist.
- **Note**: The `token.txt` file contains authentication details needed for Spotify API access. Set up your own Spotify Developer account and obtain access tokens to use this project.


---

This repository contains projects showcasing different aspects of web scraping and API interaction using Python. Each project focuses on practical examples of data extraction, manipulation, filtering, and API integration, demonstrating essential skills for working with structured data from web pages and external APIs.
