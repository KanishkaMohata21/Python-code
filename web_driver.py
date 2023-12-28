from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element("name", "fName")
first_name.send_keys("Kanishka")
last_name = driver.find_element("name", "lName")
last_name.send_keys("Mohata")
email = driver.find_element("name", "email")
email.send_keys("kanishka@gmail.com")
submit = driver.find_element("css selector", "form button")
submit.click()


