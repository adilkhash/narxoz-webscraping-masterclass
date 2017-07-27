import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://example.webscraping.com/places/default/search")


element = driver.find_element_by_id('search_term')
element.send_keys('Kaz')

element.send_keys(Keys.RETURN)


print(driver.page_source)
