import urllib3
from bs4 import BeautifulSoup
import csv
res=urllib3.PoolManager()
products=[]
for i in range(1,21):
    
    req=res.request("GET","https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_"+str(i)+"&page="+str(i))
    soup=BeautifulSoup(req.data,"html.parser")
    pl=soup.find_all("div",class_="a-section a-spacing-small a-spacing-top-small")[1:]
    
    for p in pl:
        pl=p.find("a",class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
        pn=p.find("span",class_="a-size-medium a-color-base a-text-normal")
        pc=p.find("span",class_="a-price-whole")
        pr=p.find("span",class_="a-icon-alt")
        nr=p.find("span",class_="a-size-base s-underline-text")
        products.append({

            "product link":pl['href'] if pl!=None else None,
            "product name":pn.text if pn!=None else None,
            "product cost":pc.text if pc!=None else None,
            "product review":pr.text if pr!=None else None,
            "no of reviews":nr.text if nr!=None else None})
    
names=products[0].keys()
with open("product_list1.csv","w",encoding="utf8",newline="") as file:
    dw=csv.DictWriter(file,names)
    dw.writeheader()
    dw.writerows(products)
    
    
