from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def runner():
    # initialize the driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://netbanking.hdfcbank.com/netbanking/IpinResetUsingOTP.htm")
    driver.find_element(By.XPATH, "//img[@alt='Go']").click()
    message = driver.switch_to.alert.text
    print(message)

    driver.switch_to.alert.accept()

    time.sleep(5)
    driver.quit()
