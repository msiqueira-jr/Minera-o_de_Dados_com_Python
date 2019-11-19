textto = "A cotação do dolar em torno de R$4,00 tem sido algo constante nos ultimos meses."
valor = ""
estado = 1

for c in texto: 
    if estado == 1:
        if c != "$":
            estado = 1 
        elif c == "$":
            estado = 2
            
    elif estado == 2:
        if c != " ":
            valor = valor + c
            estdo = 2
        elif c ==" ":
            print("R$" + valor)
            break