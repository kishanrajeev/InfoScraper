#Infoscraper_Cloudfare_Bypass

import os
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
import warnings
import re

global person_name
person_name = input('Enter the name of the person you want to search: ')
warnings.filterwarnings('ignore', category=DeprecationWarning)
global Headless
Headless = False
global driver_path
driver_path = "C:\\Users\\kisha\\Documents\\msedgedriver.exe"
def instagramidperplexity():
    try:
        global finalinstahandle
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument("user-data-dir=C:\\Users\\kisha\\AppData\\Local\\Microsoft\\Edge\\ud1")
        edge_options.add_argument("--disable-dev-shm-usage")
        if Headless == True:
            edge_options.add_argument("--headless")  
        elif Headless == False:
            pass
        driver = Edge(executable_path=driver_path, options=edge_options)
        perplexityprompt = "Paste only the instagram handle without the @ please. Dont add any text to your answer. Just the handle. For "+person_name
        driver.get("https://www.perplexity.ai/")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/textarea')))
        driver.find_element("xpath", '/html/body/div/main/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/textarea').send_keys(perplexityprompt)
        driver.find_element("xpath", "/html/body/div/main/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/button").click()
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div')))
        time.sleep(5)
        instahandleraw = driver.find_element("xpath", '/html/body/div/main/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div')
        instahandle = instahandleraw.text
        finalinstahandle = instahandle
        driver.quit()
    except:
        driver.quit()

def youtubechannelperplexity():
    try:
        global finalinstahandle
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument("user-data-dir=C:\\Users\\kisha\\AppData\\Local\\Microsoft\\Edge\\ud1")
        edge_options.add_argument("--disable-dev-shm-usage")
        if Headless == True:
            edge_options.add_argument("--headless")  
        elif Headless == False:
            pass  
        driver = Edge(executable_path=driver_path, options=edge_options)
        perplexityprompt = "Paste only the youtube channel url. Use /user/ not /c/ For: "+person_name
        driver.get("https://www.perplexity.ai/")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/textarea')))
        driver.find_element("xpath", '/html/body/div/main/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/textarea').send_keys(perplexityprompt)
        driver.find_element("xpath", "/html/body/div/main/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/button").click()
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div')))
        time.sleep(5)
        youtubeurlraw = driver.find_element("xpath", '/html/body/div/main/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div')
        youtubeurl = youtubeurlraw.text
        global finalyoutubeurl
        finalyoutubeurl = youtubeurl
        driver.quit()
    except:
        driver.quit()


def twitteridperplexity():
    try:
        global finalinstahandle
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument("user-data-dir=C:\\Users\\kisha\\AppData\\Local\\Microsoft\\Edge\\ud1")
        edge_options.add_argument("--disable-dev-shm-usage")
        if Headless == True:
            edge_options.add_argument("--headless")  
        elif Headless == False:
            pass  
        driver = Edge(executable_path=driver_path, options=edge_options)
        perplexityprompt = "Paste only the twitter account url. Include https For: "+person_name
        driver.get("https://www.perplexity.ai/")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/textarea')))
        driver.find_element("xpath", '/html/body/div/main/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/textarea').send_keys(perplexityprompt)
        driver.find_element("xpath", "/html/body/div/main/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/button").click()
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div')))
        time.sleep(5)
        twitteridraw = driver.find_element("xpath", '/html/body/div/main/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div')
        twitterid = twitteridraw.text
        global finaltwitterid
        finaltwitterid = twitterid
        driver.quit()
    except:
        driver.quit()


def emailandphoneperplexity():
    try:
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument("user-data-dir=C:\\Users\\kisha\\AppData\\Local\\Microsoft\\Edge\\ud1")
        edge_options.add_argument("--disable-dev-shm-usage")
        if Headless == True:
            edge_options.add_argument("--headless")  
        elif Headless == False:
            pass  
        perplexityprompt = "Business Email and Phone number for the person i give you. Only answer with the both of these in this format. Email: Phone: Do not say anything else. Just the phone number and email. Person: "+person_name
        driver = Edge(executable_path=driver_path, options=edge_options)
        driver.get("https://www.perplexity.ai/")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/textarea')))
        driver.find_element("xpath", '/html/body/div/main/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/textarea').send_keys(perplexityprompt)
        driver.find_element("xpath", "/html/body/div/main/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/button").click()
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div')))
        time.sleep(5)
        emailandphoneraw = driver.find_element("xpath", '/html/body/div/main/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/div')
        global finalemailandphone
        emailandphone = emailandphoneraw.text
        finalemailandphone = emailandphone
        driver.quit()
    except:
        driver.quit()

def twitter_followers_scraper():
    try:
        global twitter_followers
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument("user-data-dir=C:\\Users\\kisha\\AppData\\Local\\Microsoft\\Edge\\ud1")
        edge_options.add_argument("--disable-dev-shm-usage")
        if Headless == True:
            edge_options.add_argument("--headless")  
        elif Headless == False:
            pass  
        driver = Edge(executable_path=driver_path, options=edge_options)
        driver.get(finaltwitterid)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/span/span[1]')))
        time.sleep(1)
        twitter_person_name = driver.find_element("xpath", '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/span/span[1]')
        final_twitter_name = twitter_person_name.text
        time.sleep(1) 
        twitter_followers = driver.find_element("xpath", '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[2]/a')
        final_twitter_followers = twitter_followers.text
        global texfiletwitter
        texfiletwitter = f'{final_twitter_name} has {final_twitter_followers} on Youtube'

        driver.quit()
    except:
        driver.quit()
        print('Twitter ID Not Found')

def instagram_followers_scraper():
    try:
        global twitter_followers
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument("user-data-dir=C:\\Users\\kisha\\AppData\\Local\\Microsoft\\Edge\\ud1")
        edge_options.add_argument("--disable-dev-shm-usage")
        if Headless == True:
            edge_options.add_argument("--headless")  
        elif Headless == False:
            pass  
        driver = Edge(executable_path=driver_path, options=edge_options)
        driver.get('https://instagram.com/'+finalinstahandle)
        wait = WebDriverWait(driver, 10)
        time.sleep(3)
        instagram_person_name = driver.find_element("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/a/h2')
        final_instagram_name = instagram_person_name.text
        time.sleep(1) 
        instagram_followers = driver.find_element("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        final_instagram_followers = instagram_followers.text
        global texfileinstagram
        texfileinstagram = f'{final_instagram_name} has {final_instagram_followers} on Instagram'

        driver.quit()
    except:
        driver.quit()
        print('Instagram Handle Not Found')

def youtube_followers_scraper():
    try:
        global youtube_followers
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument("user-data-dir=C:\\Users\\kisha\\AppData\\Local\\Microsoft\\Edge\\ud1")
        edge_options.add_argument("--disable-dev-shm-usage")
        if Headless == True:
            edge_options.add_argument("--headless")  
        elif Headless == False:
            pass  
        driver = Edge(executable_path=driver_path, options=edge_options)
        driver.get(finalyoutubeurl)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[3]/div/div[1]/div/div[1]/ytd-channel-name/div/div/yt-formatted-string')))
        youtube_person_name = driver.find_element("xpath", '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[3]/div/div[1]/div/div[1]/ytd-channel-name/div/div/yt-formatted-string')
        final_youtube_name = youtube_person_name.text
        time.sleep(1) 
        youtube_followers_box = driver.find_element("xpath", '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[3]/div/div[1]/div/div[1]/yt-formatted-string[2]')
        youtube_followers = youtube_followers_box.text
        final_youtube_followers = youtube_followers
        global texfileyoutube
        texfileyoutube = f'{final_youtube_name} has {final_youtube_followers} on Youtube'

        driver.quit()
    except:
        driver.quit()
        print('Youtube URL Not Found')


def textfile():

    # Open a text file in write mode
    with open(os.path.join('C:\\Users\\kisha\\Documents\\output', 'output.txt'), 'w') as f:

    # Print the input to the text file
        fileinput = f'Input: {person_name}\n'
        f.write(fileinput)
        f.write('\n')
        # Print the output to the text file
        fileoutput = f'Output: \n{texfiletwitter}\n{texfileinstagram}\n{texfileyoutube}\n{finalemailandphone}\n'
        f.write(fileoutput)
        # Close the text file
        f.close()

def main():
    
    instagram = True
    twitter = True
    youtube = True

    try:
        twitteridperplexity()
    except:
        twitter = False
        print('Twitter ID not found')
    time.sleep(1)

    try:
        instagramidperplexity()
    except:
        instagram = False
        print('Instagram ID not found')
    time.sleep(1)

    try:
        youtubechannelperplexity()
    except:
        youtube = False
        print('Youtube ID not found')

    time.sleep(1)   
    if twitter == True:
        try:
            twitter_followers_scraper()
        except:
            print('Twitter ID not found')
            pass
    time.sleep(1)

    if instagram == True:
        try:
            instagram_followers_scraper()
        except:
            print('Instagram ID not found')
            pass
    time.sleep(1)

    if youtube == True:
        try:
            youtube_followers_scraper()
        except:
            print('Youtube ID not found')
            pass
    time.sleep(1)

    emailandphoneperplexity()
    time.sleep(1)
    while True:
        outputdefinput = input('Do you want to output to a text file or paste the results? (file/paste/both)')
        if outputdefinput == 'file':
            textfile()
            break
        elif outputdefinput == 'paste':
            print('Person: ', person_name)
            if twitter == True:
                print(texfiletwitter)
            if instagram == True:
                print(texfileinstagram)
            if youtube == True:
                print(texfileyoutube)
            print(finalemailandphone)
            break
        elif outputdefinput == 'both':
            print('Person : ', person_name)
            print('\n')
            if twitter == True:
                print(texfiletwitter)
            if instagram == True:
                print(texfileinstagram)
            if youtube == True:
                print(texfileyoutube)
            print(finalemailandphone)
            textfile()
            break
        else:
            print('Please enter a valid input in all lowercase characters')
            continue



if __name__ == "__main__":
    main()
