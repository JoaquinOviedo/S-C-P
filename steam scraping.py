
#made by: Joaco853
#github: https://github.com/Joaco853
#steam: https://steamcommunity.com/id/Joaco853/

from bs4 import BeautifulSoup
import requests
import json
import time

#pide el appid y usa la libreria beatifulsoup y requests para leer la pagina
print("Ingrese las url de los juegos (separadas entre: , )")
urljuego = input()+","
urljuego2=urljuego.split(",")
Numerosdejuegos= len(urljuego2)
for j in range(1,Numerosdejuegos):

      urljuegodata= urljuego2[j-1].split("/")
      appid= urljuegodata[4]

      store_doc = requests.get("https://store.steampowered.com/api/appdetails?appids="+appid+"&cc=ars&filters=price_overview")
      storesoup= BeautifulSoup(store_doc.content,"html.parser")
      strstoresoup= str(storesoup)
      storejsonprecio= json.loads(strstoresoup)                                        #lee un objeto en json de un documento , y transforma el json en un string
      strprecio= storejsonprecio[appid]["data"]["price_overview"]["final_formatted"]   #lee lo que pertenece a final_formatted en el json

      print("El juego "+urljuegodata[5]+ " cuesta: "+ strprecio)

      precioreplace= strprecio.replace("ARS$","")
      precioreplace2= precioreplace.replace(",",".")
      preciodeljuego= float(precioreplace2)

      market_doc1 = requests.get("https://steamcommunity.com/market/search?q=&category_753_Game%5B%5D=tag_app_"+appid+"&category_753_cardborder%5B%5D=tag_cardborder_0&category_753_item_class%5B%5D=tag_item_class_2&appid=753#p1_price_asc")

      marketsoup1 = BeautifulSoup(market_doc1.content, "html.parser")

      market_doc2 = requests.get("https://steamcommunity.com/market/search?q=&category_753_Game%5B%5D=tag_app_"+appid+"&category_753_cardborder%5B%5D=tag_cardborder_0&category_753_item_class%5B%5D=tag_item_class_2&appid=753#p2_price_asc")

      marketsoup2 = BeautifulSoup(market_doc2.content, "html.parser")

      #lee el total de numeros de carta
      numerosdecartas = marketsoup1.find(id="searchResults_total")
      Ncartas=numerosdecartas.get_text()
      Cartas=int(Ncartas)
      cartas=Cartas
      if Cartas%2==0 :
            Dropcartas=Cartas/2
      if Cartas%2==1:
            Dropcartas=(Cartas/2)+0.5


      if Cartas>10:
            cartas=10

      urlprecio=""
      jsonget=""
      strprecio=""
      precios=""
      preciomasalto=0
      preciomasbajo=99999
      sumadeprecios=0
      volumenes=0
      Numerodevectores=0

      for nombre in marketsoup1.findAll("span", attrs={"class":"market_listing_item_name"}):

            urlprecio += "https://steamcommunity.com/market/priceoverview/?currency=34&appid=753&market_hash_name="+appid+"-"+nombre.text+ "separar"

      for nombre in marketsoup2.findAll("span", attrs={"class":"market_listing_item_name"}):
            urlprecio += "https://steamcommunity.com/market/priceoverview/?currency=34&appid=753&market_hash_name="+appid+"-"+nombre.text+ "separar"


      vectorurl = urlprecio.split("separar")
      vector= set(vectorurl)
      Numerodevectores= len(vector)
      floatvector = int(Numerodevectores)
      print("de los "+str(Cartas)+" cromos, se leyeron "+str(Numerodevectores-1))
      
      
      for i in range(0,floatvector):
            jsonget = requests.get(vectorurl[i])
            soupprecio =BeautifulSoup(jsonget.content, 'html.parser')
            soupstrprecio= str(soupprecio)
            jsonprecio= json.loads(soupstrprecio)                                   #lo convierte en json
            strprecio= jsonprecio["lowest_price"].replace("ARS$ ","")
            str2precio= strprecio.replace(",",".")
            precio= float(str2precio)
            strvolumen=jsonprecio["volume"]
            str2volumen= strvolumen.replace(",","")
            volumen= float(str2volumen)

            precios+= str(precio) + "separar"
            sumadeprecios+= precio
            volumenes+= volumen
            
            if preciomasalto<precio:
                  preciomasalto=precio
            if preciomasbajo>precio:
                  preciomasbajo=precio

      strPrecios=precios.split("separar")
      numerodeprecios2=len(strPrecios)

      Diferencia=float(preciomasalto)-float(preciomasbajo)
      Diferenci= round(Diferencia,2)
      print("Mayor valor: "+str(preciomasalto)+" Menor valor: "+str(preciomasbajo)+" Diferencia: "+str(Diferencia))
      promedioprecios=sumadeprecios*0.87*Dropcartas/numerodeprecios2
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
      print("")

      print("Esperando 10 segundos...")
      time.sleep(10)
