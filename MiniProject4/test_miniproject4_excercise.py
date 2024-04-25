# Selenium Mini Project #4
#     Open ebay.com.
#     Search for the "16 gb"
#     Print all the Top 60 Results with there Name and price.
#     Give me the cheapest one from the list.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_miniproject4():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    driver.maximize_window()

    # Search with "16 gb" text
    driver.find_element(By.ID, "gh-ac").send_keys("16 gb")
    # Click on Search Button
    driver.find_element(By.ID, "gh-btn").click()
    time.sleep(2)

    # Get the ITEM Name
    list_of_item_title_name = driver.find_elements(By.XPATH, "//span[@role='heading']")

    print(type(list_of_item_title_name))

    # For loop will fetch all the top 60 item title names
    for index, get_all_item_title in enumerate(list_of_item_title_name[:61]):
        item_name = get_all_item_title.text
        print(index, "-", item_name)

    # Get the ITEM Price
    list_of_item_price = driver.find_elements(By.XPATH, "//span[@class='s-item__price']")
    prizes = []
    # For loop will fetch all the top 60 Item price
    for index, get_all_item_price in enumerate(list_of_item_price[:60]):
        item_price = get_all_item_price.text
        print(index, "-", item_price)
        get_only_value = item_price.replace("$", "").strip()  # get only Value from item_price
        try:
            price_float = float(get_only_value)
            prizes.append(price_float)  # Add every item price in prize list at the end
        except ValueError:
            print("Invalid price format:", item_price)
    lowest_prize = min(prizes)
    print("Lowest price is : ", lowest_prize)
