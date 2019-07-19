from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib
import argparse
import urllib.request

searchterm = 'meters' # will also be the name of the folder
url = "https://www.google.com/search?q=indian+electricity+meters&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjf3Kzk5MDjAhUJqY8KHSkZDzwQ_AUIESgB&biw=1366&bih=625"
# NEED TO DOWNLOAD CHROMEDRIVER, insert path to chromedriver inside parentheses in following line
browser = webdriver.Chrome("F:/Downloads/chromedriver_win32/chromedriver_win32 (1)/chromedriver.exe")
browser.get(url)
header={"Chrome/75.0.3770.142"}
counter = 0
succounter = 0

if not os.path.exists(searchterm):
    os.mkdir(searchterm)

for _ in range(500):
    browser.execute_script("window.scrollBy(0,10000)")

for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
    counter = counter + 1
    print ("Total Count: ", counter)
    print ("Succsessful Count: ", succounter)
    print ("URL: "+json.loads(x.get_attribute('innerHTML'))["ou"])

    img = json.loads(x.get_attribute('innerHTML'))["ou"]
    imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]

    try:
        f = open(os.path.join(searchterm , searchterm + "_" + str(counter) + "." + imgtype), "wb")
        f.write(urllib.request.urlopen(img).read())
        f.close()
        succounter = succounter + 1
    except:
        print ("can't get img")

print (succounter ," pictures succesfully downloaded!")
browser.close()