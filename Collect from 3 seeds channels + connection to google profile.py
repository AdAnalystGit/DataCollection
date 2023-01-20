# -*-coding:Latin-1 -*
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from hashlib import sha512
import json
import unicodedata
import time

# configure the chrome thing to have the extension within the drive

#s = Service('C:/Users/dell/Desktop/LIG/ProjetAdCollector/Code/GitHub/selenuim/chromedriver2.exe')
chop = webdriver.ChromeOptions()

chop.add_extension('./archive.zip')

# create new Chrome driver object with blazemeter extension

driver = webdriver.Chrome( './chromedriver',options=chop)

# this part is to upload the browser and then getting connected to the gmail account
# we upload the file where we have the list of the channels we will be using for the study



# driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.youtube.com/")
time.sleep(2)
driver.delete_all_cookies()
time.sleep(4)
print('I will click')
# connexionButton = driver.find_element('//ytd-button-renderer[@class="style-scope ytd-masthead style-suggestive size-small"]/a[@class="yt-simple-endpoint style-scope ytd-button-renderer"]')
connexionButton = driver.find_element(By.XPATH,
                                      '//div[@class="style-scope ytd-consent-bump-v2-lightbox"]/ytd-button-renderer[@class="signin style-scope ytd-consent-bump-v2-lightbox style-suggestive size-default"]/a[@class="yt-simple-endpoint style-scope ytd-button-renderer"]')
connexionButton.click()
time.sleep(2)
email = driver.find_element(By.XPATH, '//input[@class="whsOnd zHQkBf"]')
# email.send_keys("amayasTest@gmail.com")
email.send_keys("amarakli3298@gmail.com")
time.sleep(1)
nextButton = driver.find_element(By.XPATH, '//div[@id="identifierNext"]')
nextButton.click()
time.sleep(3)
mdp = driver.find_element(By.XPATH, '//input[@class="whsOnd zHQkBf"]')
mdp.send_keys("btreko98LK")
time.sleep(3)
nextButton = driver.find_element(By.XPATH, '//div[@id="passwordNext"]')
nextButton.click()
time.sleep(2)

print('I will just open the file')
# nous allons regarder max 60 videos sur chaque chaine
#with open('youtubeKids.json') as json_data:
with open('YoutubeAll.json') as json_data:
    data_dict = json.load(json_data)

# nous allons regarder max 60 videos sur chaque chaine
k = 400
i = 50

while ((k < 600) & (i < len(data_dict))):
    print(k)
    chaineName = data_dict[i]["nom"]
    chaineLink = data_dict[i]["link"]
    driver.get(chaineLink + "/featured")
    time.sleep(30)
    toutRegarder = driver.find_element(By.XPATH,
                                       #'//div[@id="dismissible"]/div[@class="grid-subheader style-scope ytd-shelf-renderer"]/div[@id="title-container"]/h2[@class="style-scope ytd-shelf-renderer"]/div[@id="play-button"]/ytd-button-renderer[@class="style-text size-default style-scope ytd-shelf-renderer"]/a[@class="yt-simple-endpoint style-scope ytd-button-renderer"]')
                                      '//*[@id="play-button"]/ytd-button-renderer/a')
    toutRegarder.click()
    time.sleep(2)
    j = 1
    while (j < 9):
        print("intered")
        url = driver.current_url
        while driver.current_url == url:
            print(k)
        j += 1
        k += 1

    i += 1

driver.close()

# check /video of each link
# check tout regarder 
# check how to control the number of videos that can be contained in each channel
# move to the next channel
