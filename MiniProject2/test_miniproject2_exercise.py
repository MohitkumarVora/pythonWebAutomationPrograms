# Selenium Mini Project #2
#
#     Open the URL - https://www.idrive360.com/enterprise/login
#     Enter the username, password
#     Verify that Trial is finished and current URL also
#     Add a logic to add Allure Screen for the Trail end.

 # Username : augtest_040823@idrive.com
 # Password : 123456

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.smoke
@allure.title("Verify that login is working in IDrive360 website")
@allure.description("TC#1 - simple login check on IDrive360 website.")
def test_mini_project2():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()

    driver.find_element(By.ID, "username").send_keys("augtest_040823@idrive.com")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "frm-btn").click()

    # Verify the Free Trial expired text
    verify_free_trial_text = WebDriverWait(driver, 25).until(
        EC.visibility_of_element_located((By.XPATH, "//h5[text()='Your free trial has expired']"))).text
    assert verify_free_trial_text == "Your free trial has expired"

    # Verify the current URL
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
