from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service("../chromedriver_win32/chromedriver.exe"))


driver.implicitly_wait(100)
driver.maximize_window()
driver.get("https://www.flipkart.com/")

act_title=driver.title
exp_title="Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"

if act_title==exp_title:
    print("Title check passed")
else:
    print("Title test failed")
driver.close()
