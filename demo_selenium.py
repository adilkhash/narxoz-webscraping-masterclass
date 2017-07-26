from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
driver.get("http://www.python.org")

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

print(soup.title.text)

driver.close()
