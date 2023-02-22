from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
pageTitle=driver.title
print(pageTitle)
resizable=driver.find_element(By.XPATH, "//div[contains(@class, 'diagonal-se')]")
action = ActionChains(driver)
action.drag_and_drop_by_offset(resizable, -100, -100).perform()
