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
driver.switch_to.frame("callout")
driver.implicitly_wait(5)
noThanksButton=driver.find_element(By.XPATH,"//button[text()='No thanks']")
noThanksButton.click()