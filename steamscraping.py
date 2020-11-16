
#made by: Joaco853
#github: https://github.com/Joaco853

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

      market_doc1 = requests.get("https://www.steamcardexchange.net/index.php?gamepage-appid-"+appid)

      marketsoup1 = BeautifulSoup(market_doc1.content, "html.parser")

      market_doc2 = requests.get("https://steamcommunity.com/market/search?q=&category_753_Game%5B%5D=tag_app_"+appid+"&category_753_cardborder%5B%5D=tag_cardborder_0&category_753_item_class%5B%5D=tag_item_class_2&appid=753")

      marketsoup2 = BeautifulSoup(market_doc2.content, "html.parser")

      #lee el total de numeros de carta

      numerosdecartas = marketsoup2.find(id="searchResults_total")
      Ncartas=numerosdecartas.get_text()
      Cartas=int(Ncartas)

      if Cartas%2==0 :
            Dropcartas=Cartas/2
      if Cartas%2==1:
            Dropcartas=(Cartas/2)+0.5


      urlprecio=""
      jsonget=""
      strprecio=""
      precios=""
      urlerror=""
      preciomasalto=0
      preciomasbajo=99999
      sumadeprecios=0
      volumenes=0
      Numerodevectores=0
      Contador=0
      erroresprecio=0

      for nombre in marketsoup1.findAll("span", attrs={"class":"element-text"}):
            Contador+=1
            if Contador<=Cartas :
             urlprecio += "https://steamcommunity.com/market/priceoverview/?currency=34&appid=753&market_hash_name="+appid+"-"+nombre.text+ "separar"


      vectorurl = urlprecio.split("separar")
      Numerodevectores= len(vectorurl)
      floatvector = int(Numerodevectores)
      
      
      for i in range(0,floatvector-1):
            
            time.sleep(0.05)

            jsonget = requests.get(vectorurl[i])
            soupprecio =BeautifulSoup(jsonget.content, 'html.parser')
            soupstrprecio= str(soupprecio)
            jsonprecio= json.loads(soupstrprecio)                                   #lo convierte en json
            try:
                  strprecio= jsonprecio["lowest_price"].replace("ARS$ ","")
            except:
                  strprecio="0"
                  erroresprecio+=1
                  urlerror+=vectorurl[i]+" "
            try:
                  strvolumen=jsonprecio["volume"]
            except:
                  strvolumen="0"
            str2volumen= strvolumen.replace(",","")
            volumen= float(str2volumen)

            volumenes+= volumen

            str2precio= strprecio.replace(",",".")
            precio= float(str2precio)

            if precio !=0 :

             if preciomasalto<precio:
                   preciomasalto=precio

             if preciomasbajo>precio:
                    preciomasbajo=precio

             sumadeprecios+= precio
             

      if erroresprecio==1 :
            print("Hubo "+str(erroresprecio)+" error con el valor del cromo: "+ str(urlerror)+" ,y no sera contemplado en el promedio de los precios")
            print("")

      if erroresprecio>1:
            print("Hubieron "+str(erroresprecio)+" errores con el valor de los cromos: "+ str(urlerror)+" ,y no seran contemplados en el promedio de los precios")
            print("")

      if erroresprecio==Cartas:
            print("Hubo un error con todas las cartas, vuelva a intentarlo , puede ser que se hayan utilizado las 100000 request diarias a las API de steam , en ese caso vuelva a intentarlo mañana")
            print("")

      if erroresprecio<Cartas:

       Diferencia=float(preciomasalto)-float(preciomasbajo)
       Diferencia= round(Diferencia,2)
       Diferencia2= (preciomasalto)/float(preciomasbajo)
       Diferencia2= round(Diferencia2,2)
       print("Mayor valor: "+str(preciomasalto)+" // Menor valor: "+str(preciomasbajo)+" // Diferencia: "+str(Diferencia))

       promedioprecios=sumadeprecios*0.87*Dropcartas/(Cartas-erroresprecio)

       promedioprecios= round(promedioprecios,2)
       strpromedioprecios= str(promedioprecios)

      
       if volumenes>=250 :
             strvolumenes="Se vendieron mas de 250 cromos en las ultimas 24hs"
       if volumenes<250 and volumenes>=100 :
             strvolumenes="Se vendieron entre 100 y 250 cromos en las ultimas 24hs"

       if volumenes<100 and volumenes>=20 :
             strvolumenes="Se vendieron entre 20 y 100 cromos en las ultimas 24hs"
       if  volumenes<20 :
             strvolumenes="Se vendieron menos de 20 cromos en las ultimas 24hs"
       if volumenes==0:
             strvolumenes="No se a vendido ningun cromo en las ultimas 24hs"
       profit=promedioprecios-preciodeljuego
       profit= round(profit,2)
       strprofit= str(profit)
       print("Vendiendo los cromos se obtiene : "+ strpromedioprecios)
       print("Profit: "+strprofit)
       print(strvolumenes)

      
       if Diferencia2>=1 and Diferencia2<=1.3 and profit>1 :
             print("")
             print("███████████ PROFIT: "+strprofit+" , diferencia de: "+str(Diferencia2)+" ███████████")

       if Diferencia2>1.3 and Diferencia2<=2 and profit>1 :
             print("")
             print("███████████ PROFIT: "+strprofit+" , revisar cromos , diferencia de: "+str(Diferencia2)+" ███████████")

       if Diferencia2>2 and profit>1 :     
             print("")
             print("███████████ PROFIT: "+strprofit+" , REVISAR CROMOS , WARNING , diferencia de: "+str(Diferencia2)+" ███████████")

      print("")
      print("Esperando 10 segundos...")
      print("")
      time.sleep(10)


print("El programa a finalizado, toque enter para cerrarlo")
input()
