# _*_ coding:utf-8 _*_
# python medicomtoy_proxy.py
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import json
import random
import string


LastName=[]
FirstName=[]
free_4=[]
zip_1=[]
zip_2=[]
addr=[]
addr2=[]
addr3=[]
tel=[]
mail=[]
number=[]
with open('./medicomtoy/LastName.txt', 'r', encoding='UTF-8') as f:
    for name in f:
        LastName.append(name.strip('\n'))

with open('./medicomtoy/FirstName.txt', 'r', encoding='UTF-8') as f:
    for name in f:
        FirstName.append(name.strip('\n'))

with open('./medicomtoy/free_4.txt', 'r', encoding='UTF-8') as f:
    for name in f:
        free_4.append(name.strip('\n'))

with open('./medicomtoy/zip_1.txt', 'r', encoding='UTF-8') as f:
    for name in f:
        zip_1.append(name.strip('\n'))

with open('./medicomtoy/zip_2.txt', 'r', encoding='UTF-8') as f:
    for name in f:
        zip_2.append(name.strip('\n'))

with open('./medicomtoy/addr.txt', 'r', encoding='UTF-8') as f:
    for name in f:
        addr.append(name.strip('\n'))

with open('./medicomtoy/addr2.txt', 'r', encoding='UTF-8') as f:
    for name in f:
        addr2.append(name.strip('\n'))
with open('./medicomtoy/addr3.txt', 'r', encoding='UTF-8') as f:
    for name in f:
        addr3.append(name.strip('\n'))

with open('./medicomtoy/tel.txt', 'r', encoding='UTF-8') as f:
    for name in f:
        tel.append(name.strip('\n'))

with open('./medicomtoy/mail.txt', 'r', encoding='UTF-8') as f:
    for name in f:
        mail.append(name.strip('\n'))
with open('./medicomtoy/number.txt', 'r', encoding='UTF-8') as f:
    for name in f:
        number.append(name.strip('\n'))

# i=20




option = webdriver.ChromeOptions()

# prefs = {'profile.managed_default_content_settings.images': 1}
# option.add_experimental_option('prefs',prefs)
option.add_argument('--proxy-server=http://127.0.0.1:1080')
option.add_argument(r"user-data-dir=./User Data")
browser=webdriver.Chrome(r'./Chrome/chromedriver.exe',options=option)
# browser.get("https://www.msn.com/ja-jp")
# time.sleep(5)

for t in range(int(number[0]),int(number[1])+1):
    i=t-1
    print("第"+str(t)+"行")
    # browser.get("http://www.medicomtoy.tv/blog/?p=52729")
    # browser.get("http://www.medicomtoy.tv/blog/?p=52736")
    # browser.get("http://www.medicomtoy.tv/blog/?p=53421")
    # browser.get("http://www.medicomtoy.tv/blog/?p=53567")
    # browser.get("http://www.medicomtoy.tv/blog/?p=53838")
    # browser.get("http://www.medicomtoy.tv/blog/?p=54379")
    browser.get("http://www.medicomtoy.tv/blog/?p=54257")
    # time.sleep(1)

    # 时间
    radios=browser.find_elements_by_name("visittime200201")
    # print(len(radios))
    radios[random.randint(5,12)].click()
    # radios[4].click()

    # 姓/last-name
    input_username=browser.find_element_by_name("last-name")
    input_username.send_keys(LastName[i])
    # 名/First-name
    input_username=browser.find_element_by_name("first-name")
    input_username.send_keys(FirstName[i])
    # 生年月日/birthdate（YYYY/MM/DD）
    input_username=browser.find_element_by_name("birthdate")
    input_username.send_keys(free_4[i])
    # 郵便番号/zipcode 
    input_username=browser.find_element_by_name("postalcode")
    # input_username.send_keys(str(zip_1[i])+str(zip_2[i]))
    input_username.send_keys(str(zip_1[i]))
    # 住所1 都道府県/Prefectures
    input_username=browser.find_element_by_name("address1")
    input_username.send_keys(addr[i])
    # 住所2 都道府県/Prefectures
    input_username=browser.find_element_by_name("address2")
    input_username.send_keys(addr2[i])
    # 住所3 都道府県/Prefectures
    input_username=browser.find_element_by_name("address3")
    input_username.send_keys(addr3[i])
    # 電話番号/phonenumber
    input_username=browser.find_element_by_name("tel")
    input_username.send_keys(str(tel[i]))
    # メールアドレス/email
    input_username=browser.find_element_by_name("email")
    input_username.send_keys(mail[i])
    # メールアドレス(確認用)/email(confirmation)
    input_username=browser.find_element_by_name("email2")
    input_username.send_keys(mail[i])

    # 勾选复选框
    checkboxes=browser.find_elements_by_name("consent[]")
    # input_checkbox.click()
    for checkbox in checkboxes:  
        checkbox.click()  

    # 抽選申込
    # time.sleep(0.5)
    # submit=browser.find_element_by_class_name("wpcf7-submit")
    # submit.click()

    # 暂停，手动回车继续
    print("停一下")
    input()

    print("停两下")
    input()





    # 选项
    # select1=browser.find_element_by_name("free_3")
    # # time.sleep(random.randint(1,2))
    # Select(select1).select_by_index("4")

    # input_username=browser.find_element_by_name("sei")
    # input_username.send_keys("li")

    # input_username=browser.find_element_by_name("mei")
    # input_username.send_keys("ming")

    # # 生日
    # input_username=browser.find_element_by_name("free_4")
    # input_username.send_keys("19990804")
    # # 邮编
    # input_username=browser.find_element_by_name("zip_1")
    # input_username.send_keys("123")
    # input_username=browser.find_element_by_name("zip_2")
    # input_username.send_keys("345")
    # # 住所
    # input_username=browser.find_element_by_name("addr")
    # input_username.send_keys("住所")
    # # 部屋番号
    # input_username=browser.find_element_by_name("addr2")
    # input_username.send_keys("部屋番号")
    # # 電話番号
    # input_username=browser.find_element_by_name("tel")
    # input_username.send_keys("tel")
    # # email
    # input_username=browser.find_element_by_name("mail")
    # input_username.send_keys("mail")
    # # (確認用) / email
    # input_username=browser.find_element_by_name("_mail")
    # input_username.send_keys("_mail")





    # checkboxes=browser.find_elements_by_name("free_7")
    # # input_checkbox.click()
    # for checkbox in checkboxes:  
    #     checkbox.click()  

    # time.sleep(0.5)
    # SendBtn=browser.find_elements_by_xpath("//div[@id='SendBtn']/input")
    # print(SendBtn[0])
    # SendBtn[0].click()  

    # time.sleep(100)