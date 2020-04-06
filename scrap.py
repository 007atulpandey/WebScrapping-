
import requests
from bs4 import BeautifulSoup
// url of the Amazon's product ..
url='https://www.amazon.in/Dr-Trust-Professional-Oximeter-Respiratory/dp/B079NSY4SY/ref=sr_1_1?dchild=1&keywords=Pulse&qid=1586210478&s=electronics&sr=8-1'

headers= {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

page = requests.get(url,headers=headers)
soup = BeautifulSoup(page.content,'html.parser')


title = soup.find(id='productTitle').get_text()
price=soup.find(id="priceblock_ourprice").get_text()
converted_price=price[0:]
print(converted_price)
