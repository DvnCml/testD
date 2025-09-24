print ("helloWorld, this is a test file to gitHub")

# 1 / 9
print("---------------------------------Ejercicios 1 a 9---------------------------------")
nuevaTupla = ("amarillo","azul", "rojo", "verde","Morado")

print(nuevaTupla[4])

nuevaListaDeTupla = list(nuevaTupla)

print(nuevaListaDeTupla)

nuevaListaDeTupla.insert(2,"negro")

print(nuevaListaDeTupla[2])

nuevaListaDeTupla.extend(("blanco","rosa","naranja"))    #extebd explicar 🤔

print(nuevaTupla)

nuevaTupla = tuple(nuevaListaDeTupla)

print(nuevaTupla)

# 10 mochila de viaje destino
print("---------------------------------Ejercicio 10---------------------------------")

mochila = ("pantalones","camisetas","cepillo de dientes","pijama","libro")
destino = ("playa","montaña","ciudad","campo","desierto")

viajeDiccionario = {
    "fecha": "2024-07-15",
    "duracion": "7 días",
    "presupuesto_usd": 1500
}

print("---------------------------------viaje inicial---------------------------------")
print(viajeDiccionario)
print("Mochila para el viaje:", mochila)
print("Destino del viaje:", destino)

mochila1 = list(mochila)
mochila1.remove("camisetas")
mochila1.remove("pijama")
mochila1.remove("libro")
destino1 = list(destino)
destino1.remove("ciudad")
destino1.insert(2,"isla")

viajeDiccionario["presupuesto_usd"] = 50000

print("---------------------------------viaje cambiado---------------------------------")
print(viajeDiccionario)
print("Mochila para el viaje:", mochila1)
print("Destino del viaje:", destino1)
