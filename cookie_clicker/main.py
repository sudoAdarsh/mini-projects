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

start_time = time.time()
wait_time = 2
while True:
    cookie.click()
    current_time = time.time()
    if (current_time - start_time) >= wait_time:
        products = driver.find_elements(By.CSS_SELECTOR, value=".enabled")
        max_product = products[-1]
        max_product_price = int(max_product.text.split('\n')[1])
        num_of_cookies = int(driver.find_element(By.ID, value="cookies").text.split()[0])
        if num_of_cookies >= max_product_price:
            max_product.click()
            wait_time += 1
        start_time = current_time