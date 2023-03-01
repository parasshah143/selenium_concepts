from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def runner():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)

    driver.get("https://www.royalcaribbean.com/")

    driver.find_element(By.ID, "rciHeaderSignIn").click()
    driver.find_element(By.LINK_TEXT, "Create an account").click()

    driver.find_element(By.XPATH, "//input[@data-placeholder='First name/Given name']").send_keys("bala")

    driver.find_element(By.XPATH, "//span[normalize-space()='Month']").click()

    driver.find_element(By.XPATH, "//span[normalize-space()='December']").click()

    time.sleep(5)
    driver.quit()
