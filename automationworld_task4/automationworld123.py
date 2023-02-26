from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


def runner():
    # initialize the driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.automationworld.com")

    driver.find_element(By.XPATH, "//div[@class='close-olytics-image-bottom-middarkblue']").click()

    driver.find_element(By.XPATH, "//span[@class='site-navbar__label'][normalize-space()='Subscribe']").click()

    driver.switch_to.window(driver.window_handles[1])

    driver.find_element(By.XPATH, "//input[@id='id24_344']").click()

    driver.find_element(By.XPATH, "//input[@id='id1']").send_keys("Paras")

    driver.find_element(By.XPATH, "//input[@id='id2']").send_keys("Shah")

    driver.find_element(By.XPATH, "//input[@id='id10']").send_keys("Project Manager")

    driver.find_element(By.XPATH, "//input[@id='id195']").send_keys("www.parasshah.com")

    driver.find_element(By.XPATH, "//input[@id='id3']").send_keys("Paras Shah Company")

    driver.find_element(By.XPATH, "//input[@id='id11']").send_keys("123456789")

    Select(driver.find_element(By.XPATH, "//select[@id='id7']")).select_by_value('189')

    driver.find_element(By.XPATH, "//input[@id='id6']").send_keys("chennai")

    driver.find_element(By.XPATH, "//input[@value='Submit']").click()

    error_message = driver.find_element(By.XPATH, "//li[normalize-space()='Email Address is required.']").text

    print("Error Message: ", error_message)

    time.sleep(5)
    driver.quit()


