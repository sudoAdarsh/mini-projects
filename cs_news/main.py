from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"


response = requests.get(url)
yc_news = response.text

soup = BeautifulSoup(yc_news, "html.parser")


article_texts = []
article_links = []

articles = soup.find_all(name="span", class_="titleline")
for article in articles:
    article_text = article.find("a").getText()
    article_texts.append(article_text)
    article_link = article.find("a").get("href")
    article_links.append(article_link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


# for i in range(len(article_texts)):
#     print(article_texts[i], article_links[i], article_upvote[i])

top_news = article_upvote.index(max(article_upvote))

print(f"Headline: {article_texts[top_news]} \nSource: {article_links[top_news]} \nUpvotes: {article_upvote[top_news]}")