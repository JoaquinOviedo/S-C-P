from bs4 import BeautifulSoup
import requests
import json
print("ingresa el appid del juego: ")
appid = input()
appid2= appid.replace("\0","")
html_doc = requests.get("https://steamcommunity.com/market/search?q=&category_753_Game%5B%5D=tag_app_"+appid2+"&category_753_cardborder%5B%5D=tag_cardborder_0&category_753_item_class%5B%5D=tag_item_class_2&appid=753")

soup = BeautifulSoup(html_doc.content, 'html.parser')
numerosdecartas = soup.find(id="searchResults_total")
Ncartas=numerosdecartas.get_text()
Cartas=float(Ncartas)
if Cartas%2==0 :
      Dropcartas=Cartas/2
if Cartas%2==1:
      Dropcartas=(Cartas/2)+0.5
      
cardprice0 = soup.find(id="resultlink_0")
cardprice1 = soup.find(id="resultlink_1")
cardprice2 = soup.find(id="resultlink_2")
cardprice3 = soup.find(id="resultlink_3")
cardprice4 = soup.find(id="resultlink_4")

price0tostring = cardprice0.get_text()
price0parseusd = price0tostring.split("\n")

price1tostring = cardprice1.get_text()
price1parseusd = price1tostring.split("\n")

price2tostring = cardprice2.get_text()
price2parseusd = price2tostring.split("\n")

price3tostring = cardprice3.get_text()
price3parseusd = price3tostring.split("\n")

price4tostring = cardprice4.get_text()
price4parseusd = price4tostring.split("\n")

urlprecio0 = "https://steamcommunity.com/market/priceoverview/?currency=34&appid=753&market_hash_name="+appid2+"-"+price0parseusd[20]

urlprecio1 = "https://steamcommunity.com/market/priceoverview/?currency=34&appid=753&market_hash_name="+appid2+"-"+price1parseusd[20]

urlprecio2 = "https://steamcommunity.com/market/priceoverview/?currency=34&appid=753&market_hash_name="+appid2+"-"+price2parseusd[20]

urlprecio3 = "https://steamcommunity.com/market/priceoverview/?currency=34&appid=753&market_hash_name="+appid2+"-"+price3parseusd[20]

urlprecio4 = "https://steamcommunity.com/market/priceoverview/?currency=34&appid=753&market_hash_name="+appid2+"-"+price4parseusd[20]

json0 = requests.get(urlprecio0)
soupprecio0 =BeautifulSoup(json0.content, 'html.parser')
strprecio0= str(soupprecio0)                                                                                       #pasa de soup a string.
jsonprecio0= json.loads(strprecio0)

json1 = requests.get(urlprecio1)
soupprecio1 =BeautifulSoup(json1.content, 'html.parser')
strprecio1= str(soupprecio1)                                                                                       
jsonprecio1= json.loads(strprecio1)

json2 = requests.get(urlprecio2)
soupprecio2 =BeautifulSoup(json2.content, 'html.parser')
strprecio2= str(soupprecio2)                                                                                       
jsonprecio2= json.loads(strprecio2)

json3 = requests.get(urlprecio3)
soupprecio3 =BeautifulSoup(json3.content, 'html.parser')
strprecio3= str(soupprecio3)                                                                                       
jsonprecio3= json.loads(strprecio3)

json4 = requests.get(urlprecio4)
soupprecio4 =BeautifulSoup(json4.content, 'html.parser')
strprecio4= str(soupprecio4)                                                                                       
jsonprecio4= json.loads(strprecio4)

strprecio0= jsonprecio0["lowest_price"].replace("ARS$ ","")
strprecio1= jsonprecio1["lowest_price"].replace("ARS$ ","")
strprecio2= jsonprecio2["lowest_price"].replace("ARS$ ","")
strprecio3= jsonprecio3["lowest_price"].replace("ARS$ ","")
strprecio4= jsonprecio4["lowest_price"].replace("ARS$ ","")

str2precio0= strprecio0.replace(",",".")
str2precio1= strprecio1.replace(",",".")
str2precio2= strprecio2.replace(",",".")
str2precio3= strprecio3.replace(",",".")
str2precio4= strprecio4.replace(",",".")

precio0= float(str2precio0)
precio1= float(str2precio1)
precio2= float(str2precio2)
precio3= float(str2precio3)
precio4= float(str2precio4)

promedioprecios= (precio0+precio1+precio2+precio3+precio4)*Dropcartas*0.87/5 
promedioprecios= round(promedioprecios,2)

strvolumen0=jsonprecio0["volume"]
strvolumen1=jsonprecio1["volume"]
strvolumen2=jsonprecio2["volume"]
strvolumen3=jsonprecio3["volume"]
strvolumen4=jsonprecio4["volume"]

str2volumen0= strvolumen0.replace(",","")
str2volumen1= strvolumen1.replace(",","")
str2volumen2= strvolumen2.replace(",","")
str2volumen3= strvolumen3.replace(",","")
str2volumen4= strvolumen4.replace(",","")

volumen0= float(str2volumen0)
volumen1= float(str2volumen1)
volumen2= float(str2volumen2)
volumen3= float(str2volumen3)
volumen4= float(str2volumen4)


volumenes= (volumen0+volumen1+volumen2+volumen3+volumen4)

strpromedioprecios= str(promedioprecios)


if volumenes>=200 :
    strvolumenes="se venden muchos por dia"
if volumenes<200 and volumenes>=100  :
     strvolumenes="se venden bastantes por dia"

if volumenes<100 and volumenes>=20 :
      strvolumenes="se venden pocos por dia"
if  volumenes<20 :
      strvolumenes="casi no se venden por dia"

print("vendiendo los cromos sacas : "+ strpromedioprecios)
print(strvolumenes)
