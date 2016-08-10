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
    if mobile_flag == 1:
        browser_search(mobile_flag=1)
        mobile_emulation = {
            "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        dr = webdriver.Chrome(chrome_options = chrome_options)
    else:
        dr = webdriver.Chrome("Data\\chromedriver.exe")

    login_with_credentials(dr)

    return dr

def login_with_credentials(dr):
    #get log in information
    e = xml.etree.ElementTree.parse('Data\\credentials.xml').getroot()
    email_data = e.findall('email')[0].text
    password_data = e.findall('password')[0].text

    #log in to Microsoft Acct
    dr.get('http://login.live.com')

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

def browser_search(dr, mobile_flag=0):

    NUM_SEARCHES = 1

    #construct search urls
    base_url = "http://www.bing.com/search?q="
    with open("Data\\words.txt") as f:
        words = f.readlines()
    words = [x.strip('\n') for x in words]
    urls = []
    for i in range(0,NUM_SEARCHES):
        # vary search pattern
        search_word_length = random.randint(1,4)
        
        addr = base_url + ' '.join(random.sample(words, search_word_length))
        urls.append(addr)

    #Bing Time
    dr.get('http://bing.com/')
    time.sleep(1)
    # do the searhes
    for i in range(0,NUM_SEARCHES):
        doASearchInNewTab(dr, urls[i])
    #leave
    dr.find_element_by_tag_name('body').send_keys("Thank You for Using Bing Bucks Bot ;)")
    time.sleep(5)
    dr.quit()

def dashboard_links(dr):
    #get log in information
    time.sleep(random.randint(1,7))
    dr.get("https://www.bing.com/rewards/dashboard")
    soup = BeautifulSoup(dr.page_source,'html.parser')
    offers = soup.find('div',{'class':'offers'}).find_all('ul',{'class':'row'})[0].find_all('li')

    for link in offers:
        time.sleep(random.randint(3,10))
        dr.get('https://www.bing.com' + link.find('a')['href'])
        time.sleep(random.randint(1,10))
        dr.get('https://www.bing.com/rewards/dashboard')
        

if __name__ == '__main__':

    dr = instantiate_session(0)
    browser_search(dr)
    dashboard_links(dr)
    time.sleep(random.randint(5,10))
    

    dr = instantiate_session(1)
    browser_search(dr)
    time.sleep(random.randint(1,60))

