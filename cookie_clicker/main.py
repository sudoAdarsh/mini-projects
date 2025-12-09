import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("https://ozh.github.io/cookieclicker/")


time.sleep(5)
try:
    driver.find_element(By.ID, value="langSelect-EN").click()
except:
    pass

time.sleep(3)

cookie = driver.find_element(By.ID, value="bigCookie")


while True:
    cookie.click()
