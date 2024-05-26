# using Automation download and install of Drivers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
import os
import time
import requests
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)

# Opening the Labour Ministry website
driver.get("https://labour.gov.in/")
time.sleep(1)
## Navigating to Media menu and then to Photo Gallery
media_menu=driver.find_element(By.LINK_TEXT,"Media").click()
press_release=driver.find_element(By.LINK_TEXT,"Click for more info of Press Releases").click()
photo_gallery= driver.find_element(By.LINK_TEXT,"Photo Gallery").click()
time.sleep(2)

##Location to store the photos
photo_folder= r"D:\ProgramS\PyCharm\Guvi-Projects\11May24\Selenium\PhotoGallery"
if not os.path.exists(photo_folder):
    os.makedirs(photo_folder)

## Downloading the first 10 Images
photos = driver.find_elements(By.CSS_SELECTOR,"img")[:10]
for index, photo in enumerate(photos):
    photo_url = photo.get_attribute('src')
    photo_response = requests.get(photo_url)
    with open(os.path.join(photo_folder, f"photo_{index + 1}.jpg"), 'wb') as file:
        file.write(photo_response.content)
    print(f"Photo {index + 1} Downloaded")
print("First 10 Photos Downloaded Successfully")
driver.quit()
