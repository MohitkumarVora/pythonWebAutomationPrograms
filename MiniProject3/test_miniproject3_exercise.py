# Selenium Mini project #3
#
#     Open the URL - https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage
#     Enter all the fields excepts the username
#     Verify that the error message comes when you click on the submit button.

import time
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_miniproject3():
    driver = webdriver.Chrome()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    driver.maximize_window()
    time.sleep(2)

    # Switch from Webpage to iframe
    driver.switch_to.frame(driver.find_element(By.ID, "result"))
    # Enter Email
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys("testing@testing.com")
    # Enter Password
    driver.find_element(By.ID, "password").send_keys("Testing@123")
    # Enter Confirm Password
    driver.find_element(By.ID, "password2").send_keys("Testing@123")

    # Click on Submit Button
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)

    username_validation = driver.find_element(By.XPATH, "//small[normalize-space()='Username must be at least 3 characters']").text
    assert username_validation == "Username must be at least 3 characters"
    allure.attach(driver.get_screenshot_as_png(), name="empty-username", attachment_type=AttachmentType.PNG)
