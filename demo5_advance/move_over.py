from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def runner():
    # initialize the driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://nasscom.in/")

    action = webdriver.ActionChains(driver)

    action.move_to_element(driver.find_element(By.LINK_TEXT, "Membership")).perform()
    action.move_to_element(driver.find_element(By.LINK_TEXT, "Become a Member")).perform()
    driver.find_element(By.LINK_TEXT, "Membership Benefits").click()





    time.sleep(5)
    driver.quit()
