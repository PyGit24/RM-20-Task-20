# Using Automation download and install
from selenium import webdriver
from selenium.webdriver.common.by import By  # Create a new instance of Chrome WebDriver
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome()  # Open the main window
import time

chrome_options= Options()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)

# Getting the Webpage URL
driver.get("https://www.cowin.gov.in/")
firstWindow = driver.window_handles[0]
firstwindow_title = driver.title
time.sleep(1)
## Locating the elements using Xpath and opening in different Window

driver.find_element(By.XPATH,("/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a")).click()
print(driver.find_element(By.XPATH,("/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a")).text)
secondwindow = driver.window_handles[1]

time.sleep(1)
## Locating the elements using Xpath and opening in different Window

c=driver.find_element(By.XPATH,("/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a")).click()
print(driver.find_element(By.XPATH,("/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a")).text)
thirdwindow = driver.window_handles[2]
time.sleep(3)

driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
driver.switch_to.window(driver.window_handles[2])
driver.close()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
driver.close()
time.sleep(3)
driver.quit()