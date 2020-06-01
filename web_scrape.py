from selenium import webdriver
import time
import urllib.request
import os
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.google.com/')


search = browser.find_element_by_name("q")

search.send_keys("dogs",Keys.ENTER)


elem = browser.find_element_by_link_text("Images")
elem.get_attribute("href")
elem.click()


for i in range(5):

	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(1)


elem1 = browser.find_element_by_id("islrg")


sub = elem1.find_elements_by_tag_name('img')

try:
    os.mkdir("downloads")
except FileExistsError:
    pass


count = 0
for i in sub:
    src = i.get_attribute('src')
    try:
        if src != None:
            src  = str(src)
            print(src)
            count+=1
            urllib.request.urlretrieve(src, os.path.join('downloads','image'+str(count)+'.jpg'))
        else:
            raise TypeError
    except TypeError:
        print('fail')