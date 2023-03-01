from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def runner():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)

    driver.get("https://www.royalcaribbean.com/")
    driver.find_element(By.XPATH, "//div[@class='notification-banner__close']").click()



    time.sleep(5)
    driver.quit()
