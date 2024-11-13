# Web Scraping

This repository contains projects that demonstrate web scraping and data manipulation using Python. Each project is designed to highlight specific scraping techniques, data processing, and file handling.

## Table of Contents
- [Projects](#projects)
  - [bs4](#bs4)
  - [100 Movies to Watch](#100-movies-to-watch)
- [Requirements](#requirements)
- [Usage](#usage)
- [License](#license)

---

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

---

This repository contains projects showcasing different aspects of web scraping using Python. Each project focuses on practical examples of data extraction, manipulation, and filtering, demonstrating essential skills for working with structured data from web pages
