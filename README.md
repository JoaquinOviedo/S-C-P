# Steamgamescardsdropprofit
Un programa que pide el la url del juego (Obtener desde : https://store.steampowered.com/search/?sort_by=Price_ASC&category2=29&os=win&filter=topsellers), lee la pagina del mercado de steam asociada a la parte de steam trading cards con ese juego (en ARS), y luego dice cuanto se obtiene en promedio por vender los cromos que dropea el juego. (el juego tiene que tener cromos)
errores posibles : 
-Si el juego es F2P o tiene algun caracter raro en el nombre es probable que se cierre el programa.
-Si ningun cromo del juego se ah vendido en las ultimas 24hs mostrara un keyerro: "volume" , que se refiere a que no existe el "volume" en el json de la api del market de steam, tambien puede cerrarse el programa.
