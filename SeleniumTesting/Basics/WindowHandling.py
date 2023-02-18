from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
opts.add
driver = Chrome(options=opts)
driver.maximize_window()
driver.get("https://www.amazon.in/")
pageTitle=driver.title
print(pageTitle)
image1=driver.find_element(By.XPATH, "//img[contains(@alt, 'Clothing')]")
image1.click()
image2=driver.find_element(By.XPATH, "//img[contains(@src, '81iiPvmfJvL')]")
image2.click()
print(driver.current_window_handle)
driver.switch_to.window(driver.window_handles[1])
print("Switched to new window-->")
print(driver.current_window_handle)
image3=driver.find_element(By.XPATH, "//span[@class='cat-link']")
image3.click()