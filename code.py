import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.keepinspiring.me/quotes-from-inspirational-women/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

quotes = []
authors = []

for blockquote in soup.find_all("blockquote"):
    text = blockquote.find("p")
    cite = blockquote.find("cite")

    if text and cite:
        quotes.append(text.get_text(strip=True).replace("“", "").replace("”", ""))
        authors.append(cite.get_text(strip=True))

df = pd.DataFrame({
    "Author": authors,
    "Quote": quotes
})

df.to_csv("Women_CEO_Quotes.csv", index=False)
print(" All done! quotes are saved as 'Women_CEO_Quotes.csv'")
