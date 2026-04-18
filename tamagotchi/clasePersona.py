from classTamagotchi import Tamagotchi

class Persona():
    def __init__(self, nombre, apellido, nombreTamagotchi, colorTamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = Tamagotchi(nombreTamagotchi, colorTamagotchi)

    #Métodos:
    #jugar_con_tamagotchi(): juega e invoca el método de tamagotchi jugar()
    def jugar_con_tamagotchi(self):
        self.tamagotchi.jugar()
        return self
    #darle_comida(): le da de comer su tamagotchi invocando al método de tamagotchi comer()
    def darle_comida(self):
        self.tamagotchi.comer()
        return self
    #curarlo(): sana las heridas de su tamagotchi invocando al método de tamagotchi curar()
    def curarlo(self):
        self.tamagotchi.curar()
        return self
    

#Crea una instancia de Persona y asígnale una instancia de Tamagotchi al atributo tamagotchi
persona1 = Persona("Juan", "Perez", "Tama", "Rojo")
#Haz que la persona le de comer, cure y juegue con su tamagotchi
persona1.darle_comida().curarlo().jugar_con_tamagotchi()
#Muestra la información de su tamagotchi
persona1.tamagotchi.mostrar_info()