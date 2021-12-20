# Steamgamescardsdropprofit
El programa pide ingresar la url del juego a analizar, para ver si el juego da profit al comprarlo, obtener los cromos del mismo y venderlos en el mercado de steam.

Para que el programa funcione correctamente es recomendable obtener los links de los juegos desde el siguiente buscador de steam:

[Steam Games List](https://store.steampowered.com/search/?sort_by=Price_ASC&category1=998&category2=29&os=win&specials=1&filter=topsellers)

el cual ya esta puesto para que filtre los juegos mas baratos y con cromos.

Si va a ingresar solo un juego no hace falta que ingrese una coma , si va a ingresar 2 o mas tiene que separarlo entre comas

— Los resultados que arroja va en este orden:
 
1_Primero nos Informa el precio del juego (en ARS) y el nombre.

2_Luego, el cromo de mayor valor y el de menor valor y la diferencia entre ambos.*

3_Lo que se obtendria vendiendo los cromos (ya incluido las fees del mercado (que son del 13%)).

4_Nos indica el profit total (lo que se obtendria menos lo que cuesta el juego).

5_Sobre la cantidad de cromos que se vendieron en las ultimas 24hs (el volumen), para ver si hay poco o mucho flujo de ventas (si se venden rapido o no).

6_Finalmente, va a resaltar los juegos que tengan profit, mayor a 1, de los que no sean profit y va a poner algunas indicaciones dependiendo si se venden muchos o pocos cromos, como tambien advirtiendo de la diferencia de precio del cromo de mayor valor y el menor.

*(hay juegos que tienen algun cromo a 30ars pero el resto a 1ars entonces puede ser un falso positivo).

A veces, nos dice si hubo algun error al obtener los precios de todos los cromos , esto puede deberse a que steam tiene un limite de solicitudes en servidores (por eso lo de la esperar 10 segundos) (RECUERDEN que steam tiene un limite de peticiones diarias de unas 10000, y cada cromo que el programa lee es una petición menos. (EJEMPLO: Si analizamos juegos que tengan 15 cromos, entonces podriamos chequear 666 juegos diarios).

Video de referencia: https://www.youtube.com/watch?v=Wx1tfcyen0A&list=LL

Preview:

![alt text](https://pbs.twimg.com/media/FHEkNX_XEAAicTT?format=png&name=small)

--------------------------------------------------------------------------------------------------------------------------------------

⚠️ ALGUNOS ERRORES PERCIBIDOS:

Si el juego es F2P o tiene algun caracter raro en el nombre es probable que se cierre el programa.

--------------------------------------------------------------------------------------------------------------------------------------

Para farmear los cromos usar el Idlemaster o el ArchiSteamFarm

Mi perfil de Steam: https://steamcommunity.com/id/Joaco853

Si le dan una estrellita me ayudan bastante <3
