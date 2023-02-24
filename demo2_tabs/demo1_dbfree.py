from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def runner():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.db4free.net/")
    time.sleep(3)
    # driver.find_element(By.XPATH, '//a[contains(@href,phpMyAdmin"]').click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "phpMyAdmin").click()
    print(driver.window_handles)
    print(driver.window_handles[0])
    print(driver.window_handles[1])

    driver.switch_to.window(driver.window_handles[1])

    driver.find_element(By.ID, "input_username").send_keys("paras")
    driver.find_element(By.ID, "input_password").send_keys("welcome123")
    driver.find_element(By.ID, "input_go").click()

    time.sleep(5)
    driver.close()

    time.sleep(5)
    driver.quit()
