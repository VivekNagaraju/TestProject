from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(options=opts)
driver.maximize_window()
driver.get("https://www.amazon.in/")
pageTitle=driver.title
print(pageTitle)
image1=driver.find_element(By.XPATH, "//img[contains(@alt, 'Clothing')]")
image1.click()
image2=driver.find_element(By.XPATH, "//img[contains(@src, '81iiPvmfJvL')]")
image2.click()
driver.switch_to.window(driver.window_handles[1])
image3=driver.find_element(By.XPATH, "//span[@class='cat-link']")
image3.click()