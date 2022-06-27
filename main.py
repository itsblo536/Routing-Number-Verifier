from selenium import webdriver 
from selenium.webdriver.common.by import By
# Used for return key in order to get search results
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path where our webdriver is located
PATH = "/Users/brendanlo/Desktop/Projects/chromedriver"
driver = webdriver.Chrome(PATH)

# Website used to verify routing numbers (Federal Reserve Bank)
driver.get("https://frbservices.org/")

routing_number = input("Please enter a routing number: ")

# Locates search bar by ID and enters routing number received as input
search = driver.find_element(By.ID, "search-fedach")
search.send_keys(routing_number)
search.send_keys(Keys.RETURN)

#Waits for agree button to load before proceeding to click
try:
    agree = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "agree_terms_use"))
    )
    agree.click()
except:
    driver.quit()


try:
    #Non-numerical routing number will result in a no such element exception
    search_results = driver.find_element(By.ID, "results_table_info")
    results = search_results.text
    if results == "Showing 0 to 0 of 0 entries":
        print("Invalid routing number.")
    else:
        result_table = driver.find_element(By.ID, "results_table")
        routing_num_info = result_table.find_elements(By.TAG_NAME, "td")
        for info in routing_num_info:
            print(info.text)
#Checks for case where user inputs a non-numerical routing number
except:
    print("You've entered a non-numerical routing number")


