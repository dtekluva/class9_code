from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

site= "http://www.jumia.com.ng/catalog/?q=for+honor"
import urllib.request

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 
url = "http://www.jumia.com.ng/catalog/?q=for+honor"

request=urllib.request.Request(url,None,headers) #The assembled request
response = ureq(request)

data = response.read() # The data u need
fullhtml = soup(data, 'html.parser')
response.close()
body = fullhtml.body

product_cards = body.findAll("div", {"class":"sku -gallery"})

print(len(product_cards))
