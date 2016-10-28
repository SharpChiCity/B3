import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import xml.etree.ElementTree

def doASearchInNewTab(dr, url):
    #open tab
    dr.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    #look at tab
    dr.switch_to_window(dr.window_handles[-1])
    #Load a page
    dr.get(url)
    #wait a short amount of time between searches
    time.sleep(random.randint(1,10))
    #close the tab
    dr.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
    #focus on first window
    dr.switch_to_window(dr.window_handles[0])

def instantiate_session(mobile_flag=0):
    chromedriver_path = "C:\\users\\monstar\\downloads\\chromedriver.exe"
    if mobile_flag == 1:
        mobile_emulation = {
            "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        dr = webdriver.Chrome(chromedriver_path,chrome_options = chrome_options)
    else:
        dr = webdriver.Chrome(chromedriver_path)
        # dr = webdriver.Firefox()

    login_with_credentials(dr)

    return dr

def login_with_credentials(dr):
    #get log in information
    e = xml.etree.ElementTree.parse('Data\\credentials.xml').getroot()
    email_data = e.findall('email')[0].text
    password_data = e.findall('password')[0].text

    #log in to Microsoft Acct
    dr.get('https://login.live.com')

    email_loc = dr.find_element_by_id("i0116")
    password_loc = dr.find_element_by_id("i0118")
    # Enter login details and submit with delays to look less like a bot
    time.sleep(random.randint(1,5))
    email_loc.send_keys(email_data)
    time.sleep(random.randint(1,5))
    password_loc.send_keys(password_data)
    time.sleep(random.randint(1,4))
    password_loc.send_keys(Keys.ENTER)
    time.sleep(random.randint(2,10))

def browser_search(dr):

    NUM_SEARCHES = random.randint(31,36)

    #construct search urls
    base_url = "https://www.bing.com/search?q="
    with open("Data\\words.txt") as f:
        words = f.readlines()
    words = [x.strip('\n') for x in words]
    urls = []
    for i in range(0,NUM_SEARCHES):
        # vary search pattern
        search_word_length = random.randint(1,4)
        
        addr = base_url + ' '.join(['define:'] + random.sample(words, search_word_length))
        urls.append(addr)

    #Bing Time
    dr.get('https://bing.com/')
    time.sleep(1)
    # do the searhes
    for i in range(0,NUM_SEARCHES):
        doASearchInNewTab(dr, urls[i])

def dashboard_links(dr):
    #get log in information
    time.sleep(random.randint(1,7))
    dr.get("https://account.microsoft.com/rewards/dashboard")
    soup = BeautifulSoup(dr.page_source,'html.parser')
    offers = soup.find('div',{'class':'card-row spacer-32-bottom clearfix'}).find_all('a')

    for link in offers:
        try:
            time.sleep(random.randint(3,10))
            dr.get('https://account.microsoft.com' + link['href'])
            time.sleep(random.randint(1,10))
            dr.get('https://account.microsoft.com/rewards/dashboard')
        except:
            pass        

if __name__ == '__main__':
    import datetime
    def run():
        dr = instantiate_session(0)
        browser_search(dr)
        dashboard_links(dr)
        dr.quit() 
        time.sleep(random.randint(5,10))

        dr = instantiate_session(1)
        browser_search(dr)
        dr.quit()
        time.sleep(random.randint(1,60))
  

    while True:
        print('run time: {}'.format(datetime.datetime.today()))
        try:    
            run()
            sleep_time1 = 78000
            sleep_time2 = 84600 #23.5 hours 
        except:
            sleep_time1 = 3000
            sleep_time2 = 5000             
            pass

        print('next run time between: {}'.format(datetime.datetime.today()+datetime.timedelta(seconds=sleep_time1),datetime.datetime.today()+datetime.timedelta(seconds=sleep_time2)))
        time.sleep(random.randint(sleep_time1,sleep_time2))
