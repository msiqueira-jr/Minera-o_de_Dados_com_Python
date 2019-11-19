arquivo = open("Airbnb-subset.csv", encoding="utf-8", errors="ignore")
dados = arquivo.read()
arquivo.close()

print(dados)