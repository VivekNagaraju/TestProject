from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
import time

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.maximize_window()

driver.get(r"C:\Users\iQuest02\Desktop\MyPage.html")
radioButton= driver.find_element(By.ID, "radio-1")
print("Radio button is selected-->",radioButton.is_selected())
time.sleep(3)
radioButton.click()
print("I clicked radio button")
print("Radio button is selected-->",radioButton.is_selected())
