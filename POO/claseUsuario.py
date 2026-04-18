from claseTarjetaCredito import TarjetaCredito

class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        #self.limite_credito = 30000
        #self.saldo_pagar = 0
        self.tarjeta = TarjetaCredito(0, 20000, 0.015)
  
    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.tarjeta.compra(monto)   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido
        return self

    #pagar_tarjeta(self, monto)
    def pagar_tarjeta(self, monto):
        self.tarjeta.pago(monto)
        return self
    
    #mostrar_saldo_usuario(self)
    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre} {self.apellido}, Saldo a Pagar: ${self.tarjeta.saldo_pagar}")
    
    #transferir_deuda(self, otro_usuario, monto): crea un método que reduzca la deuda (saldo_pagar) del usuario por el monto, y agrega esa cantidad al saldo_pagar de otro_usuario
    def transferir_deuda(self, otro_usuario, monto):
        self.tarjeta.saldo_pagar -= monto
        otro_usuario.tarjeta.saldo_pagar += monto
        return self

'''
#Crear 3 usarios
usuario1 = Usuario("Juan", "Perez", "juan.perez@gmail.com")
usuario2 = Usuario("Erica", "Gonzalez", "egonzalez@gmail.com")
usuario3 = Usuario("Ricardo", "Lopez", "r.lopez@gmail.com")

#Haz que el primer usuario haga 2 compras y luego pague su tarjeta. Muestra su saldo
usuario1.hacer_compra(5000)
usuario1.hacer_compra(2000)
usuario1.pagar_tarjeta(1000)
usuario1.mostrar_saldo_usuario()

#Haz que el segundo usuario haga 1 compra y luego pague 2 veces su tarjeta. Muestra su saldo
usuario2.hacer_compra(10000)
usuario2.pagar_tarjeta(3000)
usuario2.pagar_tarjeta(2000)
usuario2.mostrar_saldo_usuario()

#Haz que el tercer usuario haga 3 compras y luego pague su tarjeta 4 veces. Muestra su saldo
usuario3.hacer_compra(5500)
usuario3.hacer_compra(2500)
usuario3.hacer_compra(3500)
usuario3.pagar_tarjeta(2000)
usuario3.pagar_tarjeta(1500)
usuario3.pagar_tarjeta(1000)
usuario3.pagar_tarjeta(500)
usuario3.mostrar_saldo_usuario()

#ENCADENAMIENTO DE MÉTODOS
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
miyagi.hacer_compra(150).hacer_compra(300).pagar_tarjeta(50).mostrar_saldo_usuario()
'''
