import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_orangehrm_login():
    driver = webdriver.Chrome()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    # Add 5second wait for Login page to Load
    # time.sleep(5)
    #
    # Verify the Orange HRM Logo is Present using normal way
    # orangehrm_logo = driver.find_element(By.XPATH, "//img[@alt='company-branding']").is_displayed()
    # assert orangehrm_logo

    # Verify the OrangeHRM Logo is present using Explicit Wait
    orangehrm_logo = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//img[@alt='company-branding']")))
    assert orangehrm_logo

    # Get the Username
    get_username = driver.find_element(By.XPATH, "//p[text()='Username : Admin']").text
    get_username = get_username.replace("Username : ", "")

    # Enter Username
    driver.find_element(By.NAME, "username").send_keys(get_username)

    # Get the Password
    get_password = driver.find_element(By.XPATH, "//p[text()='Password : admin123']").text
    get_password = get_password.replace("Password : ", "")

    # Enter the Password
    driver.find_element(By.NAME, "password").send_keys(get_password)

    # Click on Login Button
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Verify the Change URL
    assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    # Add 3second wait for Dashboard page to Load
    # time.sleep(3)

    # Verify that the Dashboard Text present with normal way
    # verify_dashboard = driver.find_element(By.XPATH, "//h6[text()='Dashboard']").text
    # assert verify_dashboard == "Dashboard"

    # Verify the Dashboard text present using Explicit Wait
    verify_dashboard = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))).text
    assert verify_dashboard == "Dashboard"
