# -*- encoding: utf-8 -*-
'''
@File    :   medicomtoy_firefox_proxy.py
@Time    :   2020/01/31 12:28:40
@Author  :   conanlm 
'''

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import json
import random
import string
import yaml
import os


def get_yaml_data():
    # 打开yaml文件
    # print("***获取yaml文件数据***")
    file = open(os.path.abspath('.')+ r"/medicomtoy/config.yml",
                'r',
                encoding="utf-8")
    file_data = file.read()
    file.close()

    # print(file_data)
    # print("类型：", type(file_data))

    # 将字符串转化为字典或列表
    # print("***转化yaml数据为字典或列表***")
    data = yaml.load(file_data)
    # print(data)
    # print("类型：", type(data))
    return data


def run():

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



    # 如果firefox没有安装在默认位置，就要手动指定位置
    location = 'D:/Program Files/Mozilla Firefox/firefox.exe'
    browser = webdriver.Firefox(firefox_binary=location)
    # browser.get("https://www.msn.com/ja-jp")
    # time.sleep(5)

    number = get_yaml_data()

    for t in range(number['mailnameop'], number['mailnameed']+1):
        i=t-1
        print("第"+str(t)+"行")
        # browser.get("http://www.medicomtoy.tv/blog/?p=52729")
        # browser.get("http://www.medicomtoy.tv/blog/?p=52736")
        # browser.get("http://www.medicomtoy.tv/blog/?p=53421")
        # browser.get("http://www.medicomtoy.tv/blog/?p=53567")
        # browser.get("http://www.medicomtoy.tv/blog/?p=53838")
        # browser.get("http://www.medicomtoy.tv/blog/?p=54379")
        browser.get(number['url'])
        # time.sleep(1)

        # 时间
        try :
            radios=browser.find_elements_by_name("visittime200201")
        except:
            print("时间错误")
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

if __name__ == "__main__":
    run()