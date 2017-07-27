import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://google.com")
element = driver.find_element_by_name('q')
time.sleep(3)
element.send_keys('PYTHON')
time.sleep(3)
element.send_keys(Keys.RETURN)

