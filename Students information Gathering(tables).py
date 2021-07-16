#import necessary libraries
import requests
from bs4 import BeautifulSoup as bs
from itertools import zip_longest
import csv
import io
import pandas as pd
import json
import numpy as np
#making lists to store data
links=[]
labels=[]
values=[]
dic={}
#login to the page

#go to this site and get the cookies and headers before scraping
#https://curl.trillworks.com/

cookies = {
    'System': 'Q2FrZQ%3D%3D.ODljMDhjNTI5ZDliNjIyOTJmNGVjNzMxMTNmNjFmYjdjYzMxNTQzZWY0ODdjYjI3NGQxY2IxNWNhNGMwMGI3ZJw2%2FrFtPlW6I7As6A57cuhpEyQh%2BbnsEMaacLge80wMnv6Sw69BYGe0URBz7lFRGg%3D%3D',
    'CAKEPHP': 'ev1m2h4ld9ev6mus9lkh5r3f44',
    'csrfToken': '981c1f4a84ab74a7d8f0e042dd0deac3927a72a09627489a9de75edbed83903f9df7311cc7e8f8443fe4f92f0b2a0923da407bbb1d1e16ccbd84969f84585063',
    'SRVNAME': 'S7|YO9O/|YO9Oz',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://emis.moe.gov.jo/openemis-core/Institution/Institutions/dashboard/eyJpZCI6MTc2NCwiNWMzYTA5YmYyMmUxMjQxMWI2YWY0OGRmZTBiODVjMmQ5ZDExODFjZDM5MWUwODk1NzRjOGNmM2NhMWU1ZTRhZCI6ImV2MW0yaDRsZDlldjZtdXM5bGtoNXIzZjQ0In0.MWZmOWNkMWRjMzYyZGQ4NjBhMzQ0MjBmNmRhYWQzOWMwNWI5Y2Y1Y2ViNTA4MzhlYTZkYjA3NDgzMzZkNzk1NQ',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
}
#start small script for page numbers
first_range_number=int(input('Please Enter Number Of Page To Start>>>>>>> '))
second_range_number=int(input('Please Enter Number Of Page To Stop At>>>>>> '))+1
warning=input('Please Note That Stop Number Is Being Included In Data Gathering Press Enter To Continue>>>>>> ')
#you have to fetch the site first
for n in range (first_range_number,second_range_number):
    response = requests.get(f'https://emis.moe.gov.jo/openemis-core/Institution/Institutions/Students/index?academic_period_id=11&status_id=1&education_grade_id=-1&page={str(n)}', headers=headers, cookies=cookies)
#start web scraping
    soup=bs(response.content,'html.parser')
    table=soup.find('table',class_='table table-curved table-sortable table-checkable')
    for i in table.find_all('tbody'):
        rows=i.find_all('tr')
        for row in rows:
            x=row.find('a')['href']
            links.append('https://emis.moe.gov.jo'+x)
    for link in links:
        
        r=requests.get(link, headers=headers, cookies=cookies)
        s=bs(r.content,'html.parser')
        raw=s.find_all('div',class_='row')
        for j in raw:
            value=j.find('div',class_='form-input')
            if value == None:
                value='None'
                values.append(value)
            else:
                values.append(value.text.strip())
            
            label=j.find('div',class_='col-xs-6 col-md-3 form-label')
            if label == None:
                label='None'
                labels.append(label)
            else:
                labels.append(label.text.strip())
#saving students scraped data into dataframe and csv file
file_list=[labels,values]
exported=zip_longest(*file_list)
df=pd.DataFrame(exported,columns=['labels','values'])  
df.to_csv('C:/Users/drala/Desktop/My Work/Students.csv',index=False)
######################################################################################################################
#the way to json file - encoding proplem
###data_json=df.to_json()   
###with open('Students_Last_test.txt','a',encoding='utf-16') as s: 
   ### json.dump(data_json,s)
######################################################################################################################
#it was my pleasure to work with You in This project
#i hope u r satisfied with the result
#please send me your review and let me now if anything is corrupted
#Warning:You Have Only One Day To Ask For A Correction 'ONE DAY ONLY'
#feel free to ask for an advice any time :D
#Mohaed Eltantawy
#upwork:https://www.upwork.com/freelancers/~011e620c38f170e944

   

