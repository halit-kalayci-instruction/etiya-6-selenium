#selenium.py
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#full-path url
driver.get("https://www.etiya.com")
driver.maximize_window()
sleep(2)
languageSelector = driver.find_element(By.CLASS_NAME, "lang-select")
sleep(1)
languageSelector.click()
sleep(1)
turkishLangugae = driver.find_element(By.XPATH, "//*[@id='etiya']/header/div/div[2]/div[1]/div[2]/div[1]/a")
sleep(1)
turkishLangugae.click()
sleep(3)
searchBtn = driver.find_element(By.ID, "search-btn")
sleep(1)
searchBtn.click()
sleep(2)
searchInput = driver.find_element(By.ID, "search-input")
sleep(1)
searchInput.send_keys("merhaba")
sleep(1)
searchIcon = driver.find_element(By.XPATH, "//*[@id='search-box']/form/div/button")
sleep(1)
searchIcon.click()