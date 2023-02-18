from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.execute_script("")