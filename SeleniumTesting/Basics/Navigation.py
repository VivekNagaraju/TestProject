from selenium.webdriver import ChromeOptions, Chrome

from selenium.webdriver.common.by import By

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.maximize_window()
driver.get("https://www.google.com/")
# driver.implicitly_wait(10)
pageTitle=driver.title
print(pageTitle)