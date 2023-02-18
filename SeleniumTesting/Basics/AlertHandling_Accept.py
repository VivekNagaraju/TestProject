from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
pageTitle=driver.title
print(pageTitle)
alertButton=driver.find_element(By.XPATH, "//button[text()='Click Me']")
alertButton.click()
driver.switch_to.alert.accept()