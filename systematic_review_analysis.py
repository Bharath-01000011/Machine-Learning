
import requests 
from bs4 import BeautifulSoup as bs 
import re 
iphone_reviews=[]

for i in range(1,10):
  ip=[]  
  url="https://www.amazon.in/Apple-MacBook-Air-13-3-inch-Integrated/product-reviews/B073Q5R6VR/ref=cm_cr_arp_d_paging_btm_2?showViewpoints=1&pageNumber="+str(i)
  response = requests.get(url)
  soup = bs(response.content,"html.parser")
  reviews = soup.findAll("span",attrs={"class","a-size-base review-text"})
  for i in range(len(reviews)):
    ip.append(reviews[i].text)  
  iphone_reviews=iphone_reviews+ip 

with open("iphone.txt","w",encoding='utf8') as output:
    output.write(str(iphone_reviews))
    

iphone_snapdeal=[]
url1 = "https://www.snapdeal.com/product/apple-iphone-5c-16-gb/988871559/reviews?page="
url2 = "&sortBy=RECENCY&vsrc=rcnt#defRevPDP"

for i in range(1,10):
  ip=[]  
  base_url = url1+str(i)+url2
  response = requests.get(base_url)
  soup = bs(response.content,"html.parser")
  temp = soup.findAll("div",attrs={"class","user-review"})
  for j in range(len(temp)):
    ip.append(temp[j].find("p").text)
  iphone_snapdeal=iphone_snapdeal+ip 

iphone_snapdeal = list(set(iphone_snapdeal))

with open("ip_snapdeal.txt","w",encoding="utf-8") as snp:
    snp.write(str(iphone_snapdeal))