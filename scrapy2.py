import urllib3
from bs4 import BeautifulSoup
import csv
with open("product_list1.csv","r") as file:
    data=file.readlines()
links=[]
for i in data[1:]:
    links.append(i.split(",")[0])
req=urllib3.PoolManager()
products=[]

for link in links:
    res=req.request("GET","https://www.amazon.in"+link)
    soup=BeautifulSoup(res.data,"html.parser")
    products.append({
        "URL":"https://www.amazon.in"+link,
        "Description":soup.find("span",id="productTitle").text if soup.find("span",id="productTitle")!=None else None,
        "asin":soup.find("th",string=" ASIN ").find_next("td").text if soup.find("th",string=" ASIN ") !=None else None,
        "product Description":" ".join([f.text for f in soup.find("ul",class_="a-unordered-list a-vertical a-spacing-mini").find_all("span") ]) if soup.find("ul",class_="a-unordered-list a-vertical a-spacing-mini") !=None else None,
        "manufacturer":soup.find("th",string=" Manufacturer ").find_next("td").text if soup.find("th",string=" Manufacturer ") != None else None,
        })
names=products[0].keys()
with open("product_list2.csv","w",encoding="utf8",newline="") as file:
    dw=csv.DictWriter(file,names)
    dw.writeheader()
    dw.writerows(products)
