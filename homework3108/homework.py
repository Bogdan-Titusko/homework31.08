from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('https://www.saucedemo.com/')
browser.maximize_window()

email_enter = browser.find_element(By.NAME,'user-name')
email_enter.send_keys('standard_user')
time.sleep(3)

pass_enter = browser.find_element(By.NAME,'password')
pass_enter.send_keys('secret_sauce')
time.sleep(3)

login_enter = browser.find_element(By.NAME, 'login-button')
login_enter.click()
time.sleep(3)

add_to_cart = browser.find_element(By.NAME,'add-to-cart-sauce-labs-bolt-t-shirt')
add_to_cart.click()
time.sleep(3)

add_to_cart2 = browser.find_element(By.NAME,'add-to-cart-sauce-labs-backpack')
add_to_cart2.click()
time.sleep(3)

trash_button =  browser.find_element(By.CLASS_NAME, 'shopping_cart_link')
trash_button.click()
time.sleep(3)

checkout_button = browser.find_element(By.NAME, 'checkout')
checkout_button.click()
time.sleep(2)

enter_first_name = browser.find_element(By.ID, 'first-name')
enter_first_name.send_keys('Bogdan')
time.sleep(2)

enter_last_name = browser.find_element(By.ID, 'last-name')
enter_last_name.send_keys('Titusko')
time.sleep(2)

enter_zip_code = browser.find_element(By.NAME, 'postalCode')
enter_zip_code.send_keys('40232')
time.sleep(2)

continue_button = browser.find_element(By.ID, 'continue')
continue_button.click()
time.sleep(2)

browser.execute_script('window.scrollTo(0,600)')

time.sleep(3)
summary_info = browser.find_elements(By.CLASS_NAME, 'summary_info')
print(summary_info)
time.sleep(3)



finish = browser.find_element(By.NAME, 'finish')
finish.click()
time.sleep(3)

back_to_home = browser.find_element(By.NAME, 'back-to-products')
back_to_home.click()
time.sleep(3)

menu_button = browser.find_element(By.ID, 'react-burger-menu-btn')
menu_button.click()
time.sleep(3)

logout = browser.find_element(By.ID, 'logout_sidebar_link')
logout.click()

