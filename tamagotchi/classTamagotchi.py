class Tamagotchi():
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        self.salud = 100
        self.felicidad = 100
        self.energia = 100

    #jugar(): incrementa la felicidad el 10, disminuye la salud en 5
    def jugar(self):
        self.felicidad += 10
        self.salud -= 5
        return self

    #comer(): incrementa la felicidad en 5, incrementa la salud en 10
    def comer(self):
        self.felicidad += 5
        self.salud += 10
        return self
    
    #curar(): incrementa la saludo en 20, disminuye la felicidad en 5
    def curar(self):
        self.salud += 20
        self.felicidad -= 5
        return self
    
    #mostrar sus valores actuales
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Color: {self.color}, Salud: {self.salud}, Felicidad: {self.felicidad}, Energía: {self.energia}")