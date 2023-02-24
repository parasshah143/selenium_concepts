from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def runner():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")
    time.sleep(3)
    # print(driver.title)
    # driver.implicitly_wait(10)
    driver.find_element(By.NAME, "UserFirstName").send_keys("John")
    # driver.find_element("name", "username").send_keys("Admin")
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "UserLastName").send_keys("wike")
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "UserEmail").send_keys("john@gmail.com")
    driver.implicitly_wait(10)
    # driver.find_element(By.NAME, "UserTitle").click()
    driver.find_element(By.XPATH, "//select[@name='UserTitle']/option[text()='IT Manager']").click()
    driver.implicitly_wait(10)
    # "//select[@name='element_name']/option[text()='option_text']").click()
    driver.find_element(By.XPATH, "//select[@name='CompanyEmployees']/option[text()='101 - 500 employees']").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//select[@name='CompanyCountry']/option[text()='United Kingdom']").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//div[@class='checkbox-ui']").click()
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "start my free trial").click()
    driver.implicitly_wait(10)
    time.sleep(5)
    driver.quit()
