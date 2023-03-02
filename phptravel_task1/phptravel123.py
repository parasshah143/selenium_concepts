import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def runner():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.phptravels.net/home")

    driver.find_element(By.XPATH, "//a[normalize-space()='flights']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys("LAX - Los Angeles Intl - Los Angeles")
    driver.find_element(By.XPATH, "//input[@id='autocomplete2']").send_keys("DAL - Dallas Love Fld - Dallas")
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@class='row g-0']//input[@id='departure']").clear()
    driver.find_element(By.XPATH, "(//input[@id='departure'])[1]").send_keys("2023-03-13")
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@role='button']").click()
    driver.find_element(By.XPATH, "//div[@class='dropdown-item adult_qty']//i[@class='la la-plus']").click()
    driver.find_element(By.XPATH, "//span[@class='ladda-label']//*[name()='svg']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//img[@alt='no results'])[1]").is_displayed()
    driver.quit()
