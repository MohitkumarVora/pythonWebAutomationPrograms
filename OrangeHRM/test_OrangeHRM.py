import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_orangehrm_login():
    driver = webdriver.Chrome()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    time.sleep(5)

    # Verify the Orange HRM Logo is Present
    orangehrm_logo = driver.find_element(By.XPATH, "//img[@alt='company-branding']")
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
