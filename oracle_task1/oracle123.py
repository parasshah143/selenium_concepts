from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def runner():
    # initialize the driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.oracle.com/in/database/")

    driver.find_element(By.XPATH, "//span[contains(text(),'View Account')]").click()

    driver.find_element(By.XPATH, "//a[contains(text(),'Sign-In')]").click()

    print("title")
    # print the title and current url of the page
    print(driver.title)
    print("URL")
    print(driver.current_url)
    print("Header")
    # get and print the page header

    page_header = driver.find_element(By.XPATH, "//h2[normalize-space()='Oracle account sign in']").text
    print(page_header)

    driver.find_element(By.XPATH, "//input[@id='sso_username']").send_keys("john")
    driver.find_element(By.XPATH, "//input[@id='ssopassword']").send_keys("john123")

    # click on the 'Sign in' button
    driver.find_element(By.XPATH, "//input[@id='signin_button']").click()

    print("Error")
    # get and print the error message
    error_message = driver.find_element(By.XPATH, "//span[@id='errormsg']//div[1]").text
    print("Error Message: ", error_message)

    time.sleep(5)
    driver.quit()
