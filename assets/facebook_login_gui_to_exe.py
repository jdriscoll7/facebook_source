#this allows us to open the browser and parse the html
from selenium import webdriver
#this imports a flag that lets you check if an element exists before reading it so you can poll an element until it loads... makes program as fast as possible
from selenium.common.exceptions import NoSuchElementException
#import gui stuff
import tkinter
import time

url = "https://facebook.com"

class Values(tkinter.Tk):
    """docstring for Values"""
    def __init__(self, parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        stepOne = tkinter.LabelFrame(self, text=" Enter Facebook Login Information ")
        stepOne.grid(row=0, columnspan=7, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)
        self.Val1Lbl = tkinter.Label(stepOne,text="Email")
        self.Val1Lbl.grid(row=0, column=0, sticky='E', padx=5, pady=2)
        self.Val1Txt = tkinter.Entry(stepOne)
        self.Val1Txt.grid(row=0, column=1, columnspan=3, pady=2, sticky='WE')
        self.Val2Lbl = tkinter.Label(stepOne,text="Password")
        self.Val2Lbl.grid(row=1, column=0, sticky='E', padx=5, pady=2)
        self.Val2Txt = tkinter.Entry(stepOne, show="*")
        self.Val2Txt.grid(row=1, column=1, columnspan=3, pady=2, sticky='WE')
        
        self.email = None
        self.password = None

        SubmitBtn = tkinter.Button(stepOne, text="Submit",command=self.submit)
        SubmitBtn.grid(row=4, column=3, sticky='W', padx=5, pady=2)

    def submit(self):
        self.email=self.Val1Txt.get()
        if self.password=="":
            Win2=tkinter.Tk()
            Win2.withdraw()

        self.password=self.Val2Txt.get()
        if self.password=="":
            Win2=tkinter.Tk()
            Win2.withdraw()

        self.quit()

def check_exists(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def do_the_thing(banner_offset):
    audience = 0
    more = 0
    only_me = 0
    #can probably make my xpaths smarter
    audience_xpath = "//a[@data-hover='tooltip' and @aria-label!='Help Center' and @aria-label!='Edit' and @data-tooltip-content!='Only me' and @href='#' and not (@data-tooltip-position) and @style]"
    more_xpath = "//li[@class = '_54ni _o00 __MenuItem _54ne selected']"
    #more_xpath = "//*[@id='js_1lw']/div/div/ul/li[5]"
    only_me_xpath = "//li[@class='_54ni _4mwj _4h7j _k_c _k_e _2932 _6419 __MenuItem']/a[@class = '_54nc _54nu _48t_' and @href='#' and @role='menuitemcheckbox']"
    #only_me_xpath = "//*[@id='js_1lw']/div/div/ul/li[7]/a"
    
    if(check_exists(audience_xpath)):
        #this is the button that controls who can see your post
        audience = browser.find_element_by_xpath(audience_xpath)
        #scroll down to audience button
        audience.location_once_scrolled_into_view
        #scroll backwards the height of the banner
        #browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        scroll_command = "window.scrollBy(0, " + str(-2*banner_offset) + ");"
        browser.execute_script(scroll_command)
        #browser.execute_script("window.scrollBy(0,-" + banner_offset + ")")
        audience.click()
        while(check_exists("//button[@class='hideToggler']") == False):
            time.sleep(0)
        #time.sleep(speed)
        audience.send_keys('m')
        while(more == 0):
            if(check_exists(more_xpath)):
                more = browser.find_element_by_xpath(more_xpath) 
        more.click()
        while(only_me == 0):
            if(check_exists(only_me_xpath)):
                only_me = browser.find_element_by_xpath(only_me_xpath)
        only_me.click()
    else:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #time.sleep(5*speed)
    
    return

app = Values(None)
app.title('Login')
app.mainloop() 

#_________________________________________________________________________
#Opens chrome without user profile logged in
#_________________________________________________________________________
#home = expanduser("~")
#data_dir = "user-data-dir=" + home + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
options = webdriver.ChromeOptions() #create google chrome profile object
options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications":2})
#options.add_argument(data_dir) #path to a blank profile
browser = webdriver.Chrome(options=options)
#open url
browser.get(url)

#____________________________________________________________________________
#will select input field containing an id or name of email and save to 'user'
#browser.find_element_by_xpath("//input[@id='email' or @name='email']")
#____________________________________________________________________________

#find email input field
user = browser.find_element_by_xpath("//input[@name='pass' or @name='email']")
#print("Entering email...")
#clear email field
user.clear()
#enter email address
user.send_keys(app.email)

#find password input field
pswd = browser.find_element_by_xpath("//input[@id='pass' or @name='pass']")
#print("Entering password...")
#clear email field
pswd.clear()
#enter email address
pswd.send_keys(app.password)

#find login button
#print("Logging in...")
login = 0
while(login == 0):
    if(check_exists("//button[@name='login' or @value='Log In']")):
        login = browser.find_element_by_xpath("//button[@name='login' or @value='Log In']")
    elif(check_exists("//input[@name='login' or @value='Log In']")):
        login = browser.find_element_by_xpath("//input[@name='login' or @value='Log In']")
    
login.click()
#print("Login successful")

#find timeline button
timeline = 0
timeline_xpath = "//a[@class='_5afe']"
while(timeline == 0):
    if(check_exists(timeline_xpath)):
        timeline = browser.find_element_by_xpath(timeline_xpath)

timeline.click()


#find activity button
activity = 0
activity_xpath = "//a[@class='_42ft _4jy0 _4jy4 _517h _51sy' and not (@rel)]"
while(activity == 0):
    if(check_exists(activity_xpath)):
        activity = browser.find_element_by_xpath(activity_xpath)

activity.click()

#find posts button
posts = 0
posts_xpath = "//a[@title='Posts']"
while(posts == 0):
    if(check_exists(posts_xpath)):
        posts = browser.find_element_by_xpath(posts_xpath)

posts.click()

#must offset vertical scrolling by height of posts and activity search banner since it covers the buttons i want to click
gay_banner = 0
#gay_banner_xpath = "//div[@id='js_1o']/div[1]"
gay_banner_xpath = "//div[@class='_2o3t fixed_elem']"
while(gay_banner == 0):
    if(check_exists(gay_banner_xpath)):
        gay_banner = browser.find_element_by_xpath(gay_banner_xpath)
        #use '.dict' data type to get height of banner object
        banner_offset = gay_banner.size['height']

while True:
    do_the_thing(banner_offset)	
