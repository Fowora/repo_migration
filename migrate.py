# Selenium needs to be install
# If not: pip install selenium

# Chromedriver needs to exists
# If not download correct version https://chromedriver.chromium.org/downloads

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time

email = raw_input("Enter your email : ")
password = getpass()

# If chromedriver is not in PATH, declare path to chromedriver
driver = webdriver.Chrome()
driver.get("")
driver.find_element_by_id("userName").send_keys(email)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("loginButton").click()

url_list=[]

while True:
    time.sleep(1)
    repos = driver.find_elements_by_class_name("text-plain")
    for repo in repos:
            link = repo.get_attribute('href')
            name = repo.find_element_by_class_name("project-name").text
            url_list.append(link)
    next_button = driver.find_element_by_xpath(".//a[@rel='next']")
    href = next_button.get_attribute("href")
    if href[-1] == "#":
        break
    next_button.click()
            
    #break
for url in url_list:
    print("URL: " + url)
    driver.get(url)
    url_names = driver.find_element_by_tag_name('body')
    url_namess = url_names.get_attribute('data-project')
    print("PROJECT NAME: " + url_namess)
    committer=driver.find_element_by_class_name('committer')
    name = committer.find_element_by_tag_name('a').text
    time = committer.find_element_by_tag_name('time').text
    times = committer.find_element_by_tag_name('time')
    time2 = times.get_attribute('data-original-title')
    print("DATE CREATED: " + time2)
    print("DEVELOPER: " + name)
    print("Last commit: " + time)
    
driver.quit()

