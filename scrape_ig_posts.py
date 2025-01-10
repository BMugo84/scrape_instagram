#import dependencies

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import time
import requests
from bs4 import BeautifulSoup
import re
import config
import json
import os
from urllib.parse import urlparse 
import csv

#setup chromedriver
driver = webdriver.Chrome()

# open webpage
driver.get("https://www.instagram.com/")

# target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))


#enter username and password
username.clear()
username.send_keys(os.getenv('INSTAGRAM_USERNAME'))
password.clear()
password.send_keys(os.getenv('INSTAGRAM_PASSWORD'))

#target the login button and click it
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
# wait a few seconds for the search button to be clickable
search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[aria-label='Search']")))

# wait until button is clickable
search_button.click()

# target the search input field
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

# search for the @handle orkeyword
keyword = "bank.repossessedcars"
searchbox.send_keys(keyword)

# check if the keyword starts with @
if keyword.startswith("@"):
    # remove @ symbol
    keyword = keyword[1:]

# find the first element with specified xpath that matches the keyword
time.sleep(5)
first_result = driver.find_element(By.XPATH, f'//span[text()="{keyword}"]')
first_result.click()

# get the initial page height
initial_height = driver.execute_script("return document.body.scrollHeight")

# create a list to store htmls
soups = []

# scroll loop
while True:
    # scroll down to the bottom of the page
    driver.execute_script("Window.scrollTo(0, document.body.scrollHeight);")

    # wait a moment to allow new content to load 
    time.sleep(5)

    # parse the html
    html = driver.page_source

    # create beautifulsoup object from scrapped html
    soups.append(BeautifulSoup(html, 'html.parser'))

    # get current page height
    current_height = driver.execute_script("return document.body.scrollHeight")
    if current_height == initial_height:
        break# exit the loop when you cant scroll down any further

    # update the initial height for the next iteration 
    initial_height = current_height

# list to store the post image urls
post_urls = []

# loop through the soup elements 
for soup in soups:

    # find all image elements that match the specific class in soup 
    elements = soup.find_all('a', class_='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd')

    # extract the href attributes and filter urls that start with "/p/" or "/ree/"
    post_urls.extend([element['href'] for element in elements if element['href'].startswith(("/bank.repossessedcars/reel/", "/bank.repossessedcars/p/"))])

# convert list to a set to remove duplicates 
unique_post_urls = list(set(post_urls))

# create a list to store the json for each post 
json_list = []

# define the query parameters 
query_parameters = "__a=1&__d=dis"

# go through the urls 

# error handling 

    # get the current url of the page 

    # append the query parameters to the current url 

    # get url 

    # wait for a moment to allow new content to load(adjust as needed)

    # find the <pre> tag containing json data 