from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def runner():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)

    driver.get("https://demo.openemr.io/b/openemr")

    driver.find_element(By.ID, "authUser").send_keys("admin")
    driver.find_element(By.ID, "clearPass").send_keys("pass")

    select_language = Select(driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
    select_language.select_by_visible_text("English (Indian)")

    driver.find_element(By.ID, "login-button").click()

    action = webdriver.ActionChains(driver)
    action.move_to_element(driver.find_element(By.XPATH, "//div[normalize-space()='Patient']")).perform()
    driver.find_element(By.LINK_TEXT, "New").click()

    time.sleep(5)
    driver.quit()
