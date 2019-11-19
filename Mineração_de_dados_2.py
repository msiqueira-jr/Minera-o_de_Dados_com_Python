arquivo = open("Airbnb-subset.csv", encoding="utf-8", errors="ignore")
dados = arquivo.read()
arquivo.close()
distrito = ""
totLocacoes = 0
estado = 1

for c in dados:
    if estado ==  1:
        if c == ",":
            estado = 2
        else:
            estado = 1
            
    elif estado == 2: 
        if c != ",":
            distrito = distrito + c
            estado = 2
            
        elif c == ",":
            if distrito == "Brooklyn":
                totLocacoes = totLocacoes + 1
                distrito = ""
                estado = 2
            else:
                distrito = ""
                estado = 2
                
print(" Total de Locações Realizadas no Brooklyn:"+ str(totLocacoes))         