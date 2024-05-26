# Method-2 using Automation download and install of Drivers
from selenium import webdriver
from selenium.webdriver.common.by import By  # Create a new instance of Chrome WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()  # Open the main window
import time
import requests
chrome_options= Options()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
# Opening the Labour Ministry website
driver.get("https://labour.gov.in/")
time.sleep(1)

# Navigating to the "Documents" menu
documents_menu = driver.find_element(By.LINK_TEXT, "Documents")
actions = ActionChains(driver)
actions.move_to_element(documents_menu).perform()
time.sleep(2)  # Holding for the dropdown menu to appear

# Click on "Monthly Progress Report"
monthly_report_link = driver.find_element(By.LINK_TEXT, "Monthly Progress Report")
monthly_report_url = monthly_report_link.get_attribute('href')

# Downloading the monthly progress report
report_response = requests.get(monthly_report_url)
with open(r"D:\ProgramS\PyCharm\Guvi-Projects\11May24\Selenium\Monthly_Progress_Report.pdf", 'wb') as file:
    file.write(report_response.content)

print("Monthly Progress Report Downloaded Successfully")
driver.close()