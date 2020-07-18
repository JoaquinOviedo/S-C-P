from bs4 import BeautifulSoup
import requests
import json

#pide el appid y usa la libreria beatifulsoup y requests para leer la pagina
print("Ingrese la url del juego ")
urljuego = input()
urljuegodata= urljuego.split("/")
appid= urljuegodata[4]

store_doc = requests.get("https://store.steampowered.com/api/appdetails?appids="+appid+"&cc=ars&filters=price_overview")
storesoup= BeautifulSoup(store_doc.content,"html.parser")
strstoresoup= str(storesoup)
storejsonprecio= json.loads(strstoresoup)                                        #lee un objeto en json de un documento , y transforma el json en un string
strprecio= storejsonprecio[appid]["data"]["price_overview"]["final_formatted"]   # lee lo que pertenece a final_formatted en el json

print("El juego "+urljuegodata[5]+ " cuesta: "+ strprecio)

precioreplace= strprecio.replace("ARS$","")
precioreplace2= precioreplace.replace(",",".")
preciodeljuego= float(precioreplace2)

market_doc = requests.get("https://steamcommunity.com/market/search?q=&category_753_Game%5B%5D=tag_app_"+appid+"&category_753_cardborder%5B%5D=tag_cardborder_0&category_753_item_class%5B%5D=tag_item_class_2&appid=753")

marketsoup = BeautifulSoup(market_doc.content, "html.parser")

#lee el total de numeros de carta
numerosdecartas = marketsoup.find(id="searchResults_total")
Ncartas=numerosdecartas.get_text()
Cartas=int(Ncartas)
cartas=Cartas
if Cartas%2==0 :
      Dropcartas=Cartas/2
if Cartas%2==1:
      Dropcartas=(Cartas/2)+0.5


if Cartas>10:
      cartas=10
      
Numerocartas= marketsoup.find(id="searchResultsRows")
gettextnumerocartas = Numerocartas.get_text()

Numerocartasparsed= gettextnumerocartas.split("\n")


Director=""
urlprecio=""
jsonget=""
strprecio=""
sumadeprecios=0
volumenes=0
for directores in range(0,cartas):
      Director= Numerocartasparsed[29+27*directores]

      urlprecio = "https://steamcommunity.com/market/priceoverview/?currency=34&appid=753&market_hash_name="+appid+"-"+Director
      jsonget = requests.get(urlprecio)
      soupprecio =BeautifulSoup(jsonget.content, 'html.parser')
      soupstrprecio= str(soupprecio)
      jsonprecio= json.loads(soupstrprecio)                                   #lo convierte en json 
      strprecio= jsonprecio["lowest_price"].replace("ARS$ ","")
      str2precio= strprecio.replace(",",".")
      precio= float(str2precio)
      strvolumen=jsonprecio["volume"]
      str2volumen= strvolumen.replace(",","")
      volumen= float(str2volumen)
      
      sumadeprecios+= precio
      volumenes+= volumen


promedioprecios=sumadeprecios*0.87*Dropcartas/cartas
promedioprecios= round(promedioprecios,2)
strpromedioprecios= str(promedioprecios)


if volumenes>=250 :
     strvolumenes="Se venden mas de 250 cromos por dia"
if volumenes<250 and volumenes>=100 :
      strvolumenes="Se venden entre 100 y 250 cromos por dia"

if volumenes<100 and volumenes>=20 :
       strvolumenes="Se venden entro 20 y 100 por dia"
if  volumenes<20 :
       strvolumenes="Se venden menos de 20 cromos por dia por dia"

profit=promedioprecios-preciodeljuego
profit= round(profit,2)
strprofit= str(profit)
print("Vendiendo los cromos se obtiene : "+ strpromedioprecios)
print("Profit: "+strprofit)
print(strvolumenes)
