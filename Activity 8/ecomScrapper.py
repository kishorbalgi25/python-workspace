import requests
from bs4 import BeautifulSoup
import csv

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

# Amazon:

AM_ORIGIN = "https://www.amazon.com"
AM_URL= "https://www.amazon.in/s?k=iphone+15"

AM_content = requests.get(url=AM_URL,verify=False).content

AM_soup = BeautifulSoup(AM_content,'html5lib')

AM_items = AM_soup.findAll("div", class_ = "puisg-col-inner")

# Get Item Details:
products=[]
for item in AM_items:
    title = item.find("a",class_ = "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
    print(title)
    # url= title['href']
    
    item_content = requests.get(url=AM_ORIGIN+url,verify=False).content
    
    item_soup = BeautifulSoup(item_content,'html5lib')
    
    seller = item_soup.find("div", class_="tabular-buybox-text",attrs={"tabular-attribute-name":"Sold by"})
    
    name =  title.text
    price =  item.find("div",class_="a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal").find("span",class_="a-offscreen").text
    
    products.append(list((name,seller,price)))
    
with open("amazon.csv","w",newline="",encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow(["Name","Seller","Price"])
    
    writer.writerows(products)

# Flipkart:

FK_ORIGIN = "https://www.flipkart.com"
FK_URL= "https://www.flipkart.com/search?q=iphone+15"

FK_content = requests.get(url=FK_URL,verify=False).content

FK_soup = BeautifulSoup(FK_content,'html5lib')
FK_items = FK_soup.findAll("div", class_ = "_2kHMtA")

# Get Item Details:
products=[]
for item in FK_items:
    url = item.find("a",class_ = "_1fQZEK")['href']
    
    item_content = requests.get(url=FK_ORIGIN+url,verify=False).content
    
    item_soup = BeautifulSoup(item_content,'html5lib')
    
    seller = item_soup.find("div",id="sellerName").find('span').find('span').text
    
    name =  item.find("div",class_ =  "_4rR01T").text
    price =  item.find("div",class_ = "_30jeq3 _1_WHN1").text
    
    products.append(list((name,seller,price)))
    
with open("flipkart.csv","w",newline="",encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow(["Name","Seller","Price"])
    
    writer.writerows(products)