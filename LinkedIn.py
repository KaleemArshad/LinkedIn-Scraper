from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
import time


driver = webdriver.Chrome(executable_path='C:/WebDrivers/chromedriver.exe')
driver.maximize_window()
login_url = 'https://www.linkedin.com/login'
driver.get(login_url)
email_xpath = """//*[@id="username"]"""
email_id = 'Your Email'
find_email_element = driver.find_element_by_xpath(email_xpath)
find_email_element.send_keys(email_id)

time.sleep(3)

password_xpath = """//*[@id="password"]"""
password = 'Your Password'
find_pass_element = driver.find_element_by_xpath(password_xpath)
find_pass_element.send_keys(password)
find_pass_element.send_keys(Keys.ENTER)

urls_list = ['https://www.linkedin.com/in/huydinhhcmus/',
             'https://www.linkedin.com/in/joeybronner/',
             'https://www.linkedin.com/in/delagabbe/',
             'https://www.linkedin.com/in/sebastienstormacq/',
             'https://www.linkedin.com/in/niketpathak/',
             'https://www.linkedin.com/in/christianhamelin/',
             'https://www.linkedin.com/in/predamariamadalina/',
             'https://www.linkedin.com/in/dariakhmel/',
             'https://www.linkedin.com/in/kchawla-pi/',
             'https://www.linkedin.com/in/marta-castro-53404245/',
             'https://www.linkedin.com/in/sandrinegourby/',
             'https://www.linkedin.com/in/mohamed-faraji/',
             'https://www.linkedin.com/in/mhouben/',
             'https://www.linkedin.com/in/margot-de-maulmont/',
             'https://www.linkedin.com/in/sheheryarghaznavi/']
# urls = open('Url_list.txt', 'r')
# content = urls.read()
# urls_list.append(content)
# urls.close()

name_list = []
title_list = []
country_list = []
email_list = []

for link in urls_list:
    time.sleep(2)
    driver.get(link)
    driver.implicitly_wait(10)
    src = driver.page_source
    html_soup = bs(src, 'lxml')
    name = html_soup.find('li', {'class': 'inline t-24 t-black t-normal break-words'})
    name_text = name.get_text().strip()
    text_0 = name_text
    name_list.append(text_0)
    title = html_soup.find('h2', {'class': 'mt1 t-18 t-black t-normal break-words'})
    title_text = title.get_text().strip()
    text_1 = title_text
    title_list.append(text_1)
    country = html_soup.find('li', {'class': 't-16 t-black t-normal inline-block'})
    country_text = country.get_text().strip()
    text_2 = country_text
    country_list.append(text_2)
    driver.get(link + 'detail/contact-info/')
    driver.implicitly_wait(5)

    try:
        src_0 = driver.page_source
        html_soup_0 = bs(src_0, 'lxml')
        email_find = html_soup_0.find('a', href=re.compile("mailto:"))
        email_text = email_find.get_text()
        exact_email = email_text[7:]
        email_list.append(exact_email)
    except:
        error = 'No Email Found'
        email_list.append(error)

data = {'Name': name_list,
        'Title': title_list,
        'Email': email_list,
        'Country': country_list}

df = pd.DataFrame(data)
df.to_csv('Profiles_Data.csv')
driver.quit()

# emailList.append(re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", emails[i].text)[0])
