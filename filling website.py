from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import time

url = "https://www.amazon.com/dp/B0B51C2R36"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

product_title = soup.find("span", id="productTitle").text.strip()
# product_description = soup.find("span", c="a- 1st-Item.a-slze- ase.a-coor-base").text.strip()
element = soup.select_one(".a-unordered-list.a-vertical.a-spacing-small")
product_description = element.text.strip()

print(product_title)
print(product_description)


# ----------------------------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Path to your ChromeDriver
chrome_driver_path = r"C:/Driver/chromedriver-win64/chromedriver.exe"

# Initialize driver

options = Options()
options.add_argument(r"--user-data-dir=C:/Users/DELL/AppData/Local/Google/Chrome/User Data")
options.add_argument(r"--profile-directory=Default")


options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(chrome_driver_path),options=options)

time.sleep(5)
driver.get("https://www.olx.com.pk/post")
input("Press Enter to close the browser...")
driver.quit()