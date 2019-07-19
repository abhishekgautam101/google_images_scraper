# google_images_scraper

#### How to run this scraper?

##### Step 1 :
Clone this project.

##### Step 2 :
Open Google and enter a search term.
Select 'Image Search' tab.
Copy this URL.
Change line 10 to the copied URL.
```
url = "YOUR-URL_HERE"
```

##### Step 3 :
Paste 'chrome://help' in your Chrome browser's URL bar and copy your chrome version. 
Replace version in line 14 with your version.
```
header={"Chrome/<YOUR-CHROME-VERSION-HERE>"}
```

##### Step 4 :
Install Chromedriver which supports your Chrome version.

##### Step 5:
Change the 'chromedriver.exe' path in line 12
```
browser = webdriver.Chrome("YOUR-PATH-HERE")
```

##### Step 6 :
Run 'adv_image_scraper.py' file by opening CMD/Terminal and pasting this code
```
python adv_image_scraper.py
```
