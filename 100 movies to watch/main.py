import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

with open("movies.txt", "w") as file:
    movie = soup.find_all(name="h3", class_="title")
    movie_list = []
    for i in movie:
        text = f"{i.string}\n"
        movie_list.append(text)
    reverse_list = movie_list[::-1]
    file.write("".join(reverse_list))
