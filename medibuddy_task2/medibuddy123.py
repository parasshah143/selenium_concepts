from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def runner():
    # initialize the driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.medibuddy.in/")

    driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()

    driver.find_element(By.XPATH, "//div[@class='coperate']").click()

    driver.find_element(By.XPATH, "//div[@class='coperate']").click()

    driver.find_element(By.XPATH, "//input[@placeholder='Enter Username']").send_keys("John")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("John123")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    error_message = driver.find_element(By.XPATH, "//div[@class='alert alert-danger errorTxt']").text
    time.sleep(2)
    print("Error Message: ", error_message)

    time.sleep(5)
    driver.quit()
