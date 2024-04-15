from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_mini_project():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    # click on "Make Appointment" button
    driver.find_element(By.ID, "btn-make-appointment").click()

    # verify the change URL
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(3)

    # Get Username
    username = driver.find_element(By.XPATH, "//input[@value='John Doe']").get_attribute("value")
    # Enter Username
    driver.find_element(By.ID, "txt-username").send_keys(username)

    # Get Password
    password = driver.find_element(By.XPATH, "//input[@value='ThisIsNotAPassword']").get_attribute("value")
    # Enter Password
    driver.find_element(By.ID, "txt-password").send_keys(password)

    # Click on Login Button
    driver.find_element(By.ID, "btn-login").click()

    # Verify the "Make Appointment" Text
    verify_element = driver.find_element(By.XPATH, "//div/h2")
    assert verify_element.text == "Make Appointment"
