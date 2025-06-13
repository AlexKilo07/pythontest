#Dicccionarios
#Son conjuntos de pares de textos

dic={
    "nombre": "David Finch",
    "numero": 978676655,
    "casado": True
}

# print(dic["numero"])

for key, value in dic.items():
    print(key)

frutas={
    "manzana":1500,
    "frutilla": 1600,
    "durazno": 3800,
}

print(frutas)

frutas["pera"]=1200

print(frutas)