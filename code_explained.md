### Import webdriver and urllib
#### Webdriver will be used to browse whereas urllib will be used to download the images.
```
from selenium import webdriver
import time
import urllib.request
import os
from selenium.webdriver.common.keys import Keys
```
#### Here we will use chrome as our browser and download images from google images
```
browser = webdriver.Chrome()
browser.get('https://www.google.com/')


search = browser.find_element_by_name("q")


```
Enter the keyword you want to search instead of "dogs"
```
search.send_keys("dogs",Keys.ENTER)
```
```

elem = browser.find_element_by_link_text("Images")
elem.get_attribute("href")
elem.click()
```
### The below code is just to scroll to the bottom of the page so that all the images are loaded.
```
for i in range(5):

	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(1)
```
The following lines find all the images and store their info in variable **sub**.
```
elem1 = browser.find_element_by_id("islrg")
sub = elem1.find_elements_by_tag_name('img')
```
These lines create a folder named _downloads_ on the computer.
```
try:
    os.mkdir("downloads")
except FileExistsError:
    pass
```

### These are the lines which actually download the images.
### The source URL is extracted and is used to download the images.
```
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
```
#### In case the source URL is not identified, a 'fail' message is printed.