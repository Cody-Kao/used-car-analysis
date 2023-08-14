# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 23:47:32 2021

@author: USER
"""

import requests as req
from bs4 import BeautifulSoup as bs4
import pandas as pd
pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
volumn = []
price = []
year = []
CC = []
KM = []
for pages in range(1,7):
    url = "https://www.isave.com.tw/cars.aspx?pageindex="+str(pages)+"&brand=BENZ&list_car=grid"
    headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
    html = req.get(url, headers = headers)
    html.encoding = "UTF-8"
    webc = bs4(html.text, "html.parser")
    imfos = webc.find_all("div", class_= "content")
    titles = webc.find_all("div", class_= "price")
    for imfo in imfos:
        imfo = imfo.p.text
        imfo = imfo.replace(" ","").replace("\n","").replace("\t","").replace("\r","")
        volumn.append(imfo)
    for title in titles:
        title = title.text
        a = len(title)
        price.append(title[0:a-2])
for x in range(int(len(volumn))):
    year.append(volumn[x][3:7])
    CC.append(volumn[x][12:16])
    KM.append(volumn[x][-8:-2].replace(":",""))
data = [year, CC, KM, price]
index = ["Year", "CC", "KM", "Price"]
df = pd.DataFrame(data = data, index = index)
df.to_excel("Toyota.xlsx")

    