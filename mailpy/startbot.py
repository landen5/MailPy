import time
from selenium import webdriver

chromedriver = r"chromedriver location here" #location of chromedriver
driver = webdriver.Chrome(chromedriver)

email = 'Your email here' #email you want to login with
password = 'Your password here' #password for desired email

driver.get("http://www.gmail.com") #destination URL
driver.maximize_window() #maximizes chrome window

driver.find_element_by_name('identifier').send_keys(email) #fills out with email
driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click() #clicks next button

driver.implicitly_wait(4) #waits tell page is fully loaded

driver.find_element_by_name('password').send_keys(password) #fills out with password
time.sleep(1.5) #waits until password is entered completely
driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click() #clicks next button
