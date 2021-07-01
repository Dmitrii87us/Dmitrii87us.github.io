from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)  # неявное ожидание
driver.get("http://practice.automationtesting.in/")

driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("username").send_keys("Vasiliy@vasa.com")
driver.find_element_by_id("password").send_keys("VAsek1234!$ws")
driver.find_element_by_name("login").click()

logout_exists = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.woocommerce-MyAccount-navigation-link--customer-logout a")))


driver.quit()