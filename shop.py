from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)  # неявное ожидание
driver.get("http://practice.automationtesting.in/")

driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("username").send_keys("Vasiliy@vasa.com")
driver.find_element_by_id("password").send_keys("VAsek1234!$ws")
driver.find_element_by_name("login").click()

driver.find_element_by_id("menu-item-40").click()

driver.execute_script("window.scrollBy(0,300)")
driver.find_element_by_xpath("//a[@data-product_id='182']").click()
time.sleep(5)

driver.find_element_by_css_selector("a.wpmenucart-contents").click()
time.sleep(3)

proceed = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.checkout-button.button.alt.wc-forward")))
driver.find_element_by_css_selector("a.checkout-button.button.alt.wc-forward").click()
time.sleep(5)

first_name = WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.XPATH, "//label[@for='billing_first_name']"), "First Name "))
driver.find_element_by_id("billing_first_name").clear()
driver.find_element_by_id("billing_first_name").send_keys("Vasiliy")
driver.find_element_by_id("billing_last_name").clear()
driver.find_element_by_id("billing_last_name").send_keys("Ivanov")
driver.find_element_by_id("billing_email").clear()
driver.find_element_by_id("billing_email").send_keys("Vasiliy@vasa.com")
driver.find_element_by_id("billing_phone").clear()
driver.find_element_by_id("billing_phone").send_keys("88001234567")
driver.execute_script("window.scrollBy(0,300)")
driver.find_element_by_id("select2-chosen-1").click()
driver.find_element_by_id("s2id_autogen1_search").send_keys("Russia")
driver.find_element_by_css_selector("span.select2-match").click()
driver.find_element_by_id("billing_address_1").clear()
driver.find_element_by_id("billing_address_1").send_keys("Lenina Street")
driver.find_element_by_id("billing_city").clear()
driver.find_element_by_id("billing_city").send_keys("Moscow")
driver.find_element_by_id("billing_state").clear()
driver.find_element_by_id("billing_state").send_keys("Moscow Area")
driver.find_element_by_id("billing_postcode")
driver.find_element_by_id("billing_postcode").send_keys("999999")

driver.execute_script("window.scrollBy(0,600)")
time.sleep(3)
driver.find_element_by_id("payment_method_cheque").click()
driver.find_element_by_id("place_order").click()
time.sleep(3)

thanks_check = WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
payment_check = WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "li.method"), "Check Payments"))


driver.quit()