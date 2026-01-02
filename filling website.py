# ----------------------------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

#*****************************************************************************************************
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
#*****************************************************************************************************


# Path to your ChromeDriver
# chrome_driver_path = r"C:/Driver/chromedriver-win64/chromedriver.exe"

# Initialize driver

options = webdriver.ChromeOptions()

# options.add_argument("--remote-debugging-port=9222")

options.add_argument(r"user-data-dir=c:/selinium/chrome-taha")

options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=options)

# Open a new tab
# driver.execute_script("window.open('');")

# Switch to the new tab
# driver.switch_to.window(driver.window_handles[-1])

# Now navigate to the page
driver.get("https://www.olx.com.pk")
time.sleep(5)

sell_button = driver.find_element(By.XPATH, "//span[text()='Sell']")
sell_button.click()
phone_button = driver.find_element(By.XPATH, "//span[text()='Mobiles']")
phone_button.click()
sub_phone_button = driver.find_element(By.XPATH, "//div[text()='Mobile Phones']")
sub_phone_button.click()
title_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='title']"))
)

title_input.send_keys(product_title)

description_box = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "description"))
)

description_box.send_keys(product_description)

select_brand = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='make']"))
)
select_brand.click()

phone_button = driver.find_element(By.XPATH, "//div[text()='Samsung Mobile']")
phone_button.click()

#Uploading pics
folder_path = r"C:/Users/DELL/Downloads/down"

files = [
    os.path.join(folder_path, f)
    for f in os.listdir(folder_path)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]

file_input = driver.find_element(By.NAME, "photos")

file_input.send_keys("\n".join(files))


input("Press Enter to close the browser...")
driver.quit()