from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)  # неявное ожидание
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0,600)")  #скроллим страницу вниз
driver.find_element_by_css_selector("li.post-160.product.type-product a").click()
driver.find_element_by_xpath("//a[@href='#tab-reviews']").click()
driver.find_element_by_class_name("star-5").click()
driver.execute_script("window.scrollBy(0,600)")

driver.find_element_by_id("comment").send_keys("Nice book!")
driver.find_element_by_id("author").send_keys("Vasiliy")
driver.find_element_by_id("email").send_keys("Vasiliy@vasa.com")
driver.find_element_by_id("submit").click()


driver.quit()







