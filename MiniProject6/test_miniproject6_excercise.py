# 1. Login with the Credential -
# https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
# 2. Add user
# https://opensource-demo.orangehrmlive.com / web / index.php / admin / saveSystemUser
# 3. Search User and Verify the result

import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_miniproject6():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(15)

    # Verify the OrangeHRM Logo is present using Explicit Wait
    orangehrm_logo = WebDriverWait(driver, 5).until(
        ec.presence_of_element_located((By.XPATH, "//img[@alt='company-branding']")))
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

    # Verify the Dashboard URL
    assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    # Click on Admin Text at Left-side panel
    driver.find_element(By.XPATH, "//span[text()='Admin']").click()

    # Verify the User listing page URL
    assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"

    # Click on Add button to create new user
    driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()

    # Verify the Current URL
    assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser"

    # <-------------- Create User form fill-up ---------------------->

    # Select the user role from dropdown
    driver.find_element(By.XPATH, "//label[text()='User Role']/parent::div/following-sibling::div//i").click()
    driver.find_element(By.XPATH, "//div[@role='listbox']//span[text()='Admin']").click()

    # Select status from dropdown
    driver.find_element(By.XPATH, "//label[text()='Status']/parent::div/following-sibling::div//i").click()
    driver.find_element(By.XPATH, "(//div[@role='listbox']//child::div)[2]").click()

    # Enter Employee name and select from the suggestion list
    employee_name = driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
    employee_name.send_keys("James")
    time.sleep(10)
    driver.find_element(By.XPATH, "(//div[@role='listbox']//child::div)[1]").click()

    # Enter the Username
    input_username = driver.find_element(By.XPATH,
                                         "//label[text()='Username']/parent::div/following-sibling::div/input")
    username = "Monty" + str(random.randint(1000, 9999))
    print(username)
    input_username.send_keys(username)

    # Enter Password
    (driver.find_element(By.XPATH, "//label[text()='Password']/parent::div/following-sibling::div/input")
     .send_keys("Monty@123"))

    # Enter Confirm Password
    (driver.find_element(By.XPATH, "//label[text()='Confirm Password']/parent::div/following-sibling::div/input")
     .send_keys("Monty@123"))

    # Click on Save button
    save_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    save_btn.click()
    time.sleep(5)

    # <------------------------ Search for newly added user profile phase----------------------->

    # Enter Username in Admin search section
    driver.find_element(By.XPATH,
                        "//label[text()='Username']/parent::div/following-sibling::div/input").send_keys(username)

    # Click on search button
    driver.find_element(By.XPATH, "//button[text()=' Search ']").click()

    # Verify the Enter username in search is present in the User list
    username_column = driver.find_element(By.XPATH, f"//div[contains(text(),'{username}')]").text
    assert username_column == username
