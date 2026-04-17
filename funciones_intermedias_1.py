# ACTUALIZAR VALORES EN DICCIONARIOS Y LISTAS
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

#Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
matriz[1][0] = 6
print(matriz)

#Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes)

#En ciudades, cambia “Cancún” por “Monterrey”
ciudades["México"][2] = "Monterrey"
print(ciudades)

#En las coordenadas, cambia el valor de “latitud” por 9.9355431
coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)



# ITERAR A TRAVES DE UNA LISTA DE DICCIONARIOS
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario(lista):
    for diccionario in lista:
      print(f'nombre - {diccionario['nombre']}, pais - {diccionario['pais']} ')

iterarDiccionario(cantantes)



# OBTENER VALORES DE UNA LISTA DE DICCIONARIOS
def iterarDiccionario2(clave, lista):
    for diccionario in lista:
        print(diccionario[clave])

iterarDiccionario2("nombre", cantantes)
iterarDiccionario2("pais", cantantes)



#ITERAR A TRAVES DE UN DICCIONARIO CON VALORES DE LISTA
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    for clave in diccionario:
        print(f'{len(diccionario[clave])} {clave.upper()}')
        for valor in diccionario[clave]:
            print(valor)
        print()

imprimirInformacion(costa_rica)
