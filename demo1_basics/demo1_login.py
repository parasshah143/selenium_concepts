from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def runner():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)
    print(driver.title)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    # driver.find_element("name", "username").send_keys("Admin")
    time.sleep(1)
    driver.find_element("name", "password").send_keys("admin123")
    time.sleep(1)
    folder = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
    folder.click()
    time.sleep(5)
    driver.quit()
