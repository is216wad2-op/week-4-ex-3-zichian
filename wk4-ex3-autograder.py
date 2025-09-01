from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

options = Options()
options.add_argument('--headless')  # run headlessly
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = 'file://' + os.path.abspath('ex3.html')  # or your HTML filename
driver.get(url)
time.sleep(1)  # wait for page load

# Check initial list items count and contents
ul = driver.find_element(By.TAG_NAME, 'ul')
li_items = ul.find_elements(By.TAG_NAME, 'li')

initial_items = [li.text for li in li_items]
expected_initial = ["Notebook", "Jello", "Spinach", "Rice", "Birthday Cake", "Candles"]
assert initial_items == expected_initial, f"Initial list items differ: {initial_items}"

# Elements for input and enter button
input_box = driver.find_element(By.ID, "userinput")
enter_button = driver.find_element(By.ID, "enter")

# Test 1: Add valid item
new_item = "Apples"
input_box.send_keys(new_item)
enter_button.click()
time.sleep(0.5)

li_items = ul.find_elements(By.TAG_NAME, 'li')
assert li_items[-1].text == new_item, f"New item '{new_item}' not appended correctly"

# Check that input field is cleared
assert input_box.get_attribute('value') == '', "Input field not cleared after adding item"

# Test 2: Click enter with empty input - list should remain unchanged
enter_button.click()
time.sleep(0.5)

li_items_after_empty = ul.find_elements(By.TAG_NAME, 'li')
assert len(li_items_after_empty) == len(li_items), "List changed when adding empty input"

print("All tests passed!")

driver.quit()
