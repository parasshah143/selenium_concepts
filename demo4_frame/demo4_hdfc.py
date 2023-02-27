from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def runner():
    # initialize the driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://netbanking.hdfcbank.com/netbanking/")
    driver.switch_to.frame(driver.find_element(By.XPATH, "//frame[@name='login_page']"))
    driver.find_element(By.XPATH, "//input[@name='fldLoginUserId']").send_keys("parasshah")
    driver.find_element(By.XPATH, "//a[@class='btn btn-primary login-btn']").click()

    driver.switch_to.default_content()


    time.sleep(5)
    driver.quit()
