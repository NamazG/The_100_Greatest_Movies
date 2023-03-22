from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text

website = BeautifulSoup(data, "html.parser")
articles = website.select(".article-title-description__text h3")
article_titles = []

for article in articles:
    if article.div:
        continue
    else:
        article_title = article.getText()
        article_titles.append(article_title)


top_list = []
for i in range(len(article_titles) - 1):
    if i != 0:
        top_list.append(article_titles[-i])
    else:
        continue

top_list.append(article_titles[0])

with open("Top 100 Movies", "w") as file:
    for movie in top_list:
        file.write(f"{movie}\n")
