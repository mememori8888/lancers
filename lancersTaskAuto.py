#!/usr/bin/env python
# coding: utf-8

# In[11]:


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
url = 'https://www.lancers.jp/work/detail/3687509?proposeReferer=work.recommend'
browser.get(url)
time.sleep(4)

#loginまで
elem_login = browser.find_element(By.CLASS_NAME,"css-1du4kmp")

elem_login.click()

elem_mail = browser.find_element(By.ID,"UserEmail")
elem_mail.send_keys("mememori8888@gmail.com")

elem_PW = browser.find_element(By.ID,"UserPassword")
elem_PW.send_keys("mm19830831")

elem_loginbtn = browser.find_element(By.ID,"form_submit")
elem_loginbtn.click()

#作業開始ボタンクリック
elem_start = browser.find_element(By.CLASS_NAME,"show_popup_button")
elem_start.click()

#同意して作業を開始する
elem_agreestart = browser.find_element(By.ID,"form_end")
elem_agreestart.click()

import pandas as pd
df_csv = pd.read_csv('YouTubeAPI - ガールズバー (1).csv')

#データフレームのループ
for i in range(0,15,1):
    #データフレームからショップ名を取得
    shopname = df_csv.iloc[i,0]
    #データフレームからtwitterを取得
    SNS = df_csv.iloc[i,1]
    #データフレームからurl取得
    URL = df_csv.iloc[i,2]
    #開始する前の開始
    
    height = 3000
    aftherheight = height + 3000
    browser.execute_script("window.scrollTo(" + str(height) + ", " + str(aftherheight) + ");")
    
    time.sleep(1)
    elem_beforestart = browser.find_element(By.CLASS_NAME,"c-button-group__item.c-button.c-button--blue.c-button--large")
    elem_beforestart.click()
    #お店の名前入力
    elem_shop = browser.find_element(By.NAME,"data[Result][results][taskFormTextArea0]")
    elem_shop.send_keys(shopname)
    if SNS == "twitter":
        twitter = browser.find_element(By.XPATH,"//*[@id='TaskCreateForm']/section[2]/p[2]/label/input")
        twitter.click()

    elif SNS == "instagram":
        instagram = browser.find_element(By.XPATH,"//*[@id='TaskCreateForm']/section[2]/p[3]/label/input")
        instagram.click()

    else: 
        mail = browser.find_element(By.XPATH,"//*[@id='TaskCreateForm']/section[2]/p[4]/label/input")
        mail.click()
    #メールアドレス入力
    inputmail = browser.find_element(By.NAME,"data[Result][results][taskFormTextField2]")
    inputmail.send_keys(URL)
    #入力後、内容を確認するクリック
    elem_execute = browser.find_element(By.ID,"form_end")
    elem_execute.click()
    #作業完了をクリック
    elem_comp = browser.find_element(By.ID,"form_end")
    elem_comp.click()
    #続けて作業するをクリック
    elem_next = browser.find_element(By.CLASS_NAME,"result-check-btn.c-btn.btn--blue.btn--large")
    elem_next.click()
    #開始する前の開始に戻る

    


# In[79]:


########################################################################################################

#データフレームからショップ名を取得
shopname = df_csv.iloc[0,0]

#開始する前の開始
elem_beforestart = browser.find_element(By.CLASS_NAME,"c-button-group__item.c-button.c-button--blue.c-button--large")
elem_beforestart.click()

#お店の名前入力
elem_shop = browser.find_element(By.NAME,"data[Result][results][taskFormTextArea0]")
elem_shop.send_keys(shopname)

#データフレームからtwitterを取得
SNS = df_csv.iloc[0,1]

SNS

#sns条件分岐

#twitterクリック
twitter = browser.find_element(By.XPATH,"//*[@id="TaskCreateForm"]/section[2]/p[2]/label/input")
twitter.click()
#instagramクリック
instagram = browser.find_element(By.XPATH,"//*[@id="TaskCreateForm"]/section[2]/p[3]/label/input")
instagram.click()
#メールアドレスクリック
mail = browser.find_element(By.XPATH,"//*[@id="TaskCreateForm"]/section[2]/p[4]/label/input")
mail.click()

if SNS == "twitter":
    twitter = browser.find_element(By.XPATH,"//*[@id='TaskCreateForm']/section[2]/p[2]/label/input")
    twitter.click()
    
elif SNS == "instagram":
    instagram = browser.find_element(By.XPATH,"//*[@id='TaskCreateForm']/section[2]/p[3]/label/input")
    instagram.click()
    
else: 
    mail = browser.find_element(By.XPATH,"//*[@id='TaskCreateForm']/section[2]/p[4]/label/input")
    mail.click()

#データフレームからurl取得
URL = df_csv.iloc[0,2]
URL

#メールアドレス入力
inputmail = browser.find_element(By.NAME,"data[Result][results][taskFormTextField2]")
inputmail.send_keys(URL)

#入力後、内容を確認するクリック
elem_execute = browser.find_element(By.ID,"form_end")
elem_execute.click()

#作業完了をクリック
elem_comp = browser.find_element(By.ID,"form_end")
elem_comp.click()

#続けて作業するをクリック
elem_next = browser.find_element(By.CLASS_NAME,"result-check-btn.c-btn.btn--blue.btn--large")
elem_next.click()
#開始する前の開始に戻る

