from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
import time, subprocess
       
def check_exists(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

url = "https://facebook.com"
email = "Halogeek454@gmail.com"
password = "qwe123!@#QWE"

#_________________________________________________________________________
#Opens chrome with user profile logged in (not using this)
#_________________________________________________________________________
#options = webdriver.ChromeOptions() #create google chrome profile object
#options.add_argument("user-data-dir=C:\\Users\\daylo\\AppData\\Local\\Google\\Chrome\\User Data") #path to my chrome profile
#browser = webdriver.Chrome(chrome_options=options)


#_________________________________________________________________________
#Opens chrome without user profile logged in
#_________________________________________________________________________
options = webdriver.ChromeOptions() #create google chrome profile object
options.add_argument("user-data-dir=C:\\Users\\daylo\\AppData\\Local\\Google\\Chrome\\User Data\\Default") #path to a blank profile
browser = webdriver.Chrome(options=options)
#open url
browser.get(url)

#____________________________________________________________________________
#will select input field containing an id or name of email and save to 'user'
#browser.find_element_by_xpath("//input[@id='email' or @name='email']")
#____________________________________________________________________________

#find email input field
print("Entering email...")
user = browser.find_element_by_xpath("//input[@id='email']")
#clear email field
user.clear()
#enter email address
user.send_keys(email)

#find password input field
print("Entering password...")
pswd = browser.find_element_by_xpath("//input[@id='pass' or @name='pass']")
#clear email field
pswd.clear()
#enter email address
pswd.send_keys(password)

#find login button
print("Logging in...")
login = browser.find_element_by_xpath("//input[@value='Log In']")
login.click()
print("Login successful")

#find timeline button
timeline = browser.find_element_by_xpath("//a[@class='_5afe']")
timeline.click()

time.sleep(3)

#find activity button
activity = browser.find_element_by_xpath("//a[@class='_42ft _4jy0 _4jy4 _517h _51sy' and not (@rel)]")
activity.click()

#drop = browser.find_element_by_xpath("//a[@href='_42ft _4jy0 _4jy4 _517h _51sy' and not (@rel)]")

time.sleep(3)

#find posts button
posts = browser.find_element_by_xpath("//a[@title='Posts']")
posts.click()

time.sleep(3)

while True:
	#if (browser.find_element_by_xpath("//a[@role = 'button' and @aria-label='Shared with Your friends']")):
		#swf2 = browser.find_element_by_xpath("//a[@role = 'button' and @aria-label='Shared with Your friends']")
	#if (NoSuchElementException == browser.find_element_by_xpath("//a[@data-hover='tooltip' and @aria-label!='Help Center' and @aria-label!='Edit' and @data-tooltip-content!='Only me' and @href='#' and not (@data-tooltip-position)]")):
	if(check_exists("//a[@data-hover='tooltip' and @aria-label!='Help Center' and @aria-label!='Edit' and @data-tooltip-content!='Only me' and @href='#' and not (@data-tooltip-position)]")):
		audience = browser.find_element_by_xpath("//a[@data-hover='tooltip' and @aria-label!='Help Center' and @aria-label!='Edit' and @data-tooltip-content!='Only me' and @href='#' and not (@data-tooltip-position)]")
		audience.click()
		time.sleep(1)
		audience.send_keys('m')
		more = browser.find_element_by_xpath("//li[@class = '_54ni _o00 __MenuItem _54ne selected']") 
		#more = browser.find_element_by_xpath("//li[@class = '_54ni _o00 __MenuItem']")
		more.click()
		time.sleep(1)
		#open = browser.find_element_by_xpath("//input[@value='291667064279714']")
		#open_parent = open.find_element_by_xpath('..')
		#only_me = open_parent.find_element_by_xpath('//a')
		audience.send_keys('o')
		time.sleep(1)
		only_me = browser.find_element_by_xpath("//li[@class='_54ni _4mwj _4h7j _k_c _k_e _2932 _6419 __MenuItem']/a[@class = '_54nc _54nu _48t_' and @href='#' and @role='menuitemcheckbox']")
		#only_me = browser.find_element_by_xpath("//li[@class='_54ni _4mwj _4h7j _k_c _k_e _2932 _6419 __MenuItem']/a[@class = '_54nc _54nu _48t_' and @href='#' and @role='menuitemcheckbox']/div[@class = '_48u1']")
		only_me.click()
		time.sleep(1)
	else:
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(3)
	
