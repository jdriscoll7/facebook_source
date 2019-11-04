from selenium import webdriver #this allows us to open the browser and parse the html

#this imports a flag that lets you check if an element exists before reading it so you can poll an element until it loads... makes program as fast as possible
from selenium.common.exceptions import NoSuchElementException

#this was used when opening a Chrome window that was already logged in
#from os.path import expanduser
import time
#import subprocess

url = "https://facebook.com"
email = "Halogeek454@gmail.com"
password = "qwe123!@#QWE"
