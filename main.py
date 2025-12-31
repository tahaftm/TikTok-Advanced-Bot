import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B0B51C2R36"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

product_title = soup.find("span", id="productTitle").text.strip()
# product_description = soup.find("span", c="a- 1st-Item.a-slze- ase.a-coor-base").text.strip()
element = soup.select_one(".a-unordered-list.a-vertical.a-spacing-small")
product_description = element.text.strip()

print(product_title)
print(product_description)