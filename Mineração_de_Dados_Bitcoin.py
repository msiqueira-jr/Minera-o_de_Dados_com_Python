import requests

html = requests.get("https://coinmarketcap.com/").text
preco = ""
estado = 1

for c in html: 
    if estado   == 1: estado  = (1 if c != "B" else 2)
    elif estado == 2: estado  = (1 if c != "T" else 3)
    elif estado == 3: estado =  (1 if c != "C" else 4)
    elif estado == 4: estado  = (1 if c != "<" else 5)
    elif estado == 5: estado  = (1 if c != "/" else 6)
    elif estado == 6: estado  = (1 if c != "a" else 7)
    elif estado == 7: estado  = (7 if c != "$" else 8)
    elif estado == 8: estado  = (8 if c != "$" else 9)
    elif estado == 9:
        if c != "<":
            preco = preco + c 
        else:
            print("$" + preco)
            break 