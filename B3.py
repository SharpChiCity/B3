import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import xml.etree.ElementTree

def doASearchInNewTab(dr, url):
	#open tab
	dr.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
	#look at tab
	dr.switch_to_window(dr.window_handles[-1])
	#Load a page
	dr.get(url)
	#wait
	time.sleep(1)
	#close the tab
	dr.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
	#focus on first window
	dr.switch_to_window(dr.window_handles[0])

def main():

	NUM_SEARCHES = 33

	#construct search urls
	base_url = "http://www.bing.com/search?q="
	with open("Data\\words.txt") as f:
		words = f.readlines()
	words = [x.strip('\n') for x in words]
	urls = []
	for i in range(0,NUM_SEARCHES):
		addr = base_url + random.choice(words)
		urls.append(addr)

	#get log in information
	e = xml.etree.ElementTree.parse('Data\\credentials.xml').getroot()
	email_data = e.findall('email')[0].text
	password_data = e.findall('password')[0].text

	#Chrome Stuff
	dr = webdriver.Chrome("Data\\chromedriver.exe")

	#log in to Microsoft Acct
	dr.get('http://login.live.com')

	email_loc = dr.find_element_by_id("i0116")
	password_loc = dr.find_element_by_id("i0118")
	# Enter login details and submit
	email_loc.send_keys(email_data)
	password_loc.send_keys(password_data)
	password_loc.send_keys(Keys.ENTER)
	time.sleep(2)

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

if __name__ == '__main__':
	main()