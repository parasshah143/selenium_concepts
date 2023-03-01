from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.support.wait import WebDriverWait


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

    driver.find_element(By.XPATH, "//div[text()='Patient']").click()
    driver.find_element(By.XPATH, "//div[text()='New/Search']").click()

    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@name='pat']"))

    time.sleep(5)
    driver.find_element(By.ID, "form_fname").send_keys("Paras")
    driver.find_element(By.ID, "form_lname").send_keys("Shah")

    driver.find_element(By.XPATH, "//option[text()='Male']").click()

    driver.find_element(By.XPATH, "//input[@id='form_DOB']").send_keys("2023-03-01")

    driver.find_element(By.ID, "create").click()

    driver.switch_to.default_content()

    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='modalframe']"))

    driver.find_element(By.XPATH, "//input[@value='Confirm Create New Patient']").click()

    driver.switch_to.default_content()

    # time.sleep(10)
    wait = WebDriverWait(driver, 30, 2)
    wait.until(expected_conditions.alert_is_present())

    alert = driver.switch_to.alert.text
    print(alert)

    driver.switch_to.alert.accept()

    if len(driver.find_elements(By.XPATH, "//div[@class='closeDlgIframe']")) > 0:
        driver.find_element(By.XPATH, "//div[@class='closeDlgIframe']").click()

    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@name='pat']"))

    actual_added_patient = driver.find_element(By.XPATH, "//i[@class='fa fa-question-circle']/ancestor::h2").text
    print(actual_added_patient)

    time.sleep(5)
    driver.quit()
