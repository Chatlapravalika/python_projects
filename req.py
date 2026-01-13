import requests
from bs4 import BeautifulSoup
import pandas as pd

# Practice website for scraping
URL = "https://quotes.toscrape.com/"

quotes_data = []

page = 1
while True:
    response = requests.get(URL + f"page/{page}/")
    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    if not quotes:
        break

    for q in quotes:
        text = q.find("span", class_="text").get_text()
        author = q.find("small", class_="author").get_text()
        tags = ", ".join([tag.get_text() for tag in q.find_all("a", class_="tag")])

        quotes_data.append({
            "Quote": text,
            "Author": author,
            "Tags": tags
        })

    print(f"Scraped page {page}")
    page += 1

# Save data to CSV
df = pd.DataFrame(quotes_data)
df.to_csv("scraped_quotes.csv", index=False)

print("✅ Scraping completed! Data saved to scraped_quotes.csv")
