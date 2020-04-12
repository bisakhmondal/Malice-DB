from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
option=webdriver.ChromeOptions()
option.add_argument(' - incognito')

browser=webdriver.Chrome(executable_path='/home/bisakh/Desktop/Scripts/chromedriver_linux64\
/chromedriver',chrome_options= option)
# browser.implicitly_wait(3)
browser.get('http://167.99.233.64/')
# browser.get('http://google.com')
# webdriver(browser)
# time.sleep(10)
# browser.quit()
timeout=10
try:
    WebDriverWait(browser,timeout= timeout).until(EC.visibility_of_element_located((By.XPATH,
    '//*[@id="navbarNav"]/ul/li[4]/a')))
except TimeoutException:
    print("Network Error!!!")
    browser.quit();

script='function getElementByXpath(path)\
     {return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}\
     const obj=getElementByXpath(`//*[@id="root"]/div/div[2]/div/div[2]`); \
     obj.remove();'

signUp_elt=browser.find_element_by_xpath('//*[@id="navbarNav"]/ul/li[4]/a')
signIn_elt=browser.find_element_by_xpath('//*[@id="navbarNav"]/ul/li[3]/a')
signUp_elt.click()

N=1000
generic_name="Anonymous1"
generic_password="voila123"

for id in range(N):
    print(id)
    Name_elt=browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/form/div[1]/input')
    Name_elt.clear()
    Name_elt.send_keys(generic_name)


    Email_elt=browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/form/div[2]/input')
    Email_elt.clear()
    Email_elt.send_keys(f'hiii2pratik{id}@hotmail.com')

    Pass_elt=browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/form/div[3]/input')
    Pass_elt.clear()
    Pass_elt.send_keys(generic_password)

    submit_btn=browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/form/button')
    submit_btn.click()
    signIn_elt.click()
    signUp_elt.click()
    try:
        # WebDriverWait(browser,timeout= timeout).until(EC.visibility_of_element_located((By.XPATH,
        # '//*[@id="root"]/div/div[2]/div/div[2]'))) #wait for success message
        WebDriverWait(browser,timeout= timeout).until(EC.visibility_of_element_located((By.XPATH,
        '//*[@id="root"]/div/div[2]/div/form/div[1]/input'))) #wait form input
    except TimeoutException:
        print("Network Error!!!")
        browser.quit();
    # browser.execute_script(script)#remove success message for next check

browser.quit()