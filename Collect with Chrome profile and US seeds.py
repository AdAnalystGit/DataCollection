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
import undetected_chromedriver as uc

# configure the chrome thing to have the extension within the drive

#s = Service('C:/Users/dell/Desktop/LIG/ProjetAdCollector/Code/GitHub/selenuim/chromedriver2.exe')
import ssl 


ssl._create_default_https_context = ssl._create_unverified_context
options = uc.ChromeOptions()
options.add_argument('--load-extension=./archive')
options.add_argument("--user-data-dir=./profiles/")
options.add_argument('--profile-directory=Profile 11')
#options.add_argument('--headless')
options.add_argument("--no-sandbox")
#options.add_argument("--headless")
driver = uc.Chrome(executable_path='./chromedriver',options=options)

# create new Chrome driver object with blazemeter extension

#driver = webdriver.Chrome( './chromedriver',options=chop)

# this part is to upload the browser and then getting connected to the gmail account
# we upload the file where we have the list of the channels we will be using for the study



# driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.youtube.com/")
time.sleep(2)
driver.delete_all_cookies()
time.sleep(10)
print('I will click')

print('I will just open the file')
# nous allons regarder max 60 videos sur chaque chaine
#with open('youtubeKids.json') as json_data:
with open('5youtubeKids.json') as json_data:
    data_dict = json.load(json_data)

# nous allons regarder max 60 videos sur chaque chaine
k = 1
i =0

while ((k < 700) & (i < len(data_dict))):
    print(k)
    chaineName = data_dict[i]["nom"]
    chaineLink = data_dict[i]["link"]
    driver.get(chaineLink + "/featured")
    time.sleep(30)
    toutRegarder = driver.find_element(By.XPATH,
                                       #'//div[@id="dismissible"]/div[@class="grid-subheader style-scope ytd-shelf-renderer"]/div[@id="title-container"]/h2[@class="style-scope ytd-shelf-renderer"]/div[@id="play-button"]/ytd-button-renderer[@class="style-text size-default style-scope ytd-shelf-renderer"]/a[@class="yt-simple-endpoint style-scope ytd-button-renderer"]')
                                      #'//*[@id="play-button"]/ytd-button-renderer/a')
                                      '//*[@id="play-button"]/ytd-button-renderer/yt-button-shape/a')
    toutRegarder.click()
    time.sleep(2)
    j = 1
    while (j < 20):
        print("intered")
        url = driver.current_url
        time.sleep(50)
        ids = ['25','26','27','29','28','30','31','32']
        for id in ids :

            try:
                nextvideoButton = driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div['+id+']/div[2]/div[1]/a[2]')
                                                        
                                                       
                nextvideoButton.click()
                break
                
            except :
                print("we didn't find me",id)


        #while driver.current_url == url:
        print(k)
        j += 1
        k += 1

    i += 1

driver.close()

# check /video of each link
# check tout regarder 
# check how to control the number of videos that can be contained in each channel
# move to the next channel
