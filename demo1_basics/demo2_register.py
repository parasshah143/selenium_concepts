from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def runner():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    driver.implicitly_wait(10)
    print(driver.title)
    driver.implicitly_wait(10)
    driver.find_element(By.LINK_TEXT, "Create new account").click()
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "firstname").send_keys("ParasShah")
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "lastname").send_keys("Shah")
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "reg_passwd__").send_keys("helloworld")
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@value='-1']").click()
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "websubmit").click()
    driver.implicitly_wait(10)

    time.sleep(5)
    driver.quit()
