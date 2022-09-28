# importing Libraries
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import re

# Pilot1: Extracting 1 page for "Goal" as the topic
url= "https://www.ted.com/talks?language=en&page=1&sort=newest&topics%5B%5D=goals"
page= requests.get(url)
print(page.reason)
soup=bs(page.content, "html.parser")

s=soup.find_all('div' , {'class':"media__message"})

#presenter=p.find({"class":"h12 talk-link__speaker"})
presenter_list=[]
title_list=[]
release_list=[]
link_list=[]

for item in s: 
    d=item.text.split("\n")
    presenter=d[1]
    presenter_list.append(presenter)
    title=d[4]
    title_list.append(title)
    release=d[11]
    release_list.append(release)
    # getting the link    
    li= item.find('a', {"class":"ga-link"})
    lin= li.get('href')
    link_list.append(lin)
#print('presenter_list = ' , presenter_list,  '\n')
print('len(presenter_list) = ' , len(presenter_list),  '\n')
#print('title_list = ' , title_list, '\n')
print('len(title_list) = ' , len(title_list), '\n')
#print('release_list = ' , release_list, '\n')
print('len(release_list) = ' , len(release_list), '\n')
#print('link_list = ' , link_list)
print('en(link_list) = ' , len(link_list))

## Pilot 2: Extracting 2 pages of Tag = "Goal"
presenter_list=[]
title_list=[]
release_list=[]
link_list=[]
# url = u1 + page_number + u2
# for page 1:
# https://www.ted.com/talks?language=en&page=1&sort=newest&topics%5B%5D=goals
u1= 'https://www.ted.com/talks?language=en&page='
u2= '&sort=newest&topics%5B%5D=goals'
for p in range(1,3):
    url= u1+str(p)+u2
    page= requests.get(url)
    print(page.status_code) # print(page.reason)
    soup=bs(page.content, "html.parser")
    s=soup.find_all('div' , {'class':"media__message"})
    #presenter=p.find({"class":"h12 talk-link__speaker"})
    for item in s: 
        d=item.text.split("\n")
        presenter=d[1]
        presenter_list.append(presenter) 
        title=d[4]
        title_list.append(title)
        release=d[11]
        release_list.append(release)
        li= item.find('a', {"class":"ga-link"})
        lin= li.get('href')
        lin= "https://www.ted.com"+lin
        link_list.append(lin) 
    #print('presenter_list = ' , presenter_list,  '\n')
    #print('title_list = ' , title_list, '\n')
    #print('release_list = ' , release_list)
    #print('link_list = ' , link_list)

print('len(presenter_list) = ',len(presenter_list))
print('len(title_list) = ',len(title_list))
print('len(release_list) = ',len(release_list))
print('len(link_list) = ',len(link_list))

# Creating Data Frame
df_Ted = pd.DataFrame()
df_Ted['Presenter']= presenter_list
df_Ted['Title'] = title_list
df_Ted['Published in']= release_list
df_Ted['Tag'] = 'Goal'
df_Ted['Link Address']= link_list
df_Ted['Language'] = 'En'
df_Ted.head(2)
df_Ted.to_csv("E:/Hamid/Data Science/Teddy.csv")

## Final Product: The topic and subtitle would be defined by user 
Tag= input(print("Please import your Topic"))
Language = input(print("Please choice a language(En/Fa/Es/Ko/Fr)"))
Ad=input(print("Please import an address to Teddy store the outcome?"))
u1= 'https://www.ted.com/talks?language='+Language+'&page='
u2= '&sort=newest&topics%5B%5D='+Tag
presenter_list=[]
title_list=[]
release_list=[]
link_list=[]
for p in range(1,5):
    url= u1+str(p)+u2
    page= requests.get(url)
    #print(page.status_code) # print(page.reason)
    soup=bs(page.content, "html.parser")
    s=soup.find_all('div' , {'class':"media__message"})
    #presenter=p.find({"class":"h12 talk-link__speaker"})
    for item in s: 
        d=item.text.split("\n")
        presenter=d[1]
        presenter_list.append(presenter)    
        title=d[4]
        title_list.append(title)
        release=d[11]
        release_list.append(release)
        li= item.find('a', {"class":"ga-link"})
        lin= li.get('href')
        lin= "https://www.ted.com"+lin
        link_list.append(lin)
    #print('presenter_list = ' , presenter_list,  '\n')
    #print('title_list = ' , title_list, '\n')
    #print('release_list = ' , release_list)
    #print('link_list = ' , link_list)

# Creating Data Frame
df_Ted = pd.DataFrame()
df_Ted['Presenter']= presenter_list
df_Ted['Title'] = title_list
df_Ted['Published in']= release_list
df_Ted['Topic'] = Tag
df_Ted['Link Address']= link_list
df_Ted['Language'] = Language

file_name = "/Teddy_"+Tag+"_"+Language+".csv"
address= Ad + file_name
df_Ted.to_csv(address)
print("Thanks for your attention :)! The {file} is creater in\n {Ad}".format(file=file_name, Ad=Ad))
print("\n Please share your exprience via following connect me via address: \n https://github.com/MEHEhsani")

df_Ted
