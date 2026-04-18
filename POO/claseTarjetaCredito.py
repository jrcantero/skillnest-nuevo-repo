class TarjetaCredito:
    todas_las_tarjetas=[]
    #Incluye en este método valores por default
    def __init__(self, saldo_pagar, limite_credito, intereses):
        #TU CODIGO (Aquí va los atributos de instancia y sus asignaciones de valor)
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        TarjetaCredito.todas_las_tarjetas.append(self)

    #crea un método de clase para imprimir todas las instancias de la información de las tarjetas creadas
    
    @classmethod
    def imprimir_tarjetas(cls):
        for tarjeta in cls.todas_las_tarjetas:
            tarjeta.mostrar_info_tarjeta()

    def compra(self, monto):
        #TU CODIGO
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:            
            print("Compra rechazada: excede el límite de crédito.")
        return self

    def pago(self, monto):
        #TU CODIGO
        self.saldo_pagar -= monto
        return self

    def mostrar_info_tarjeta(self):
        #TU CODIGO
        print(f"Saldo a Pagar: ${self.saldo_pagar}")
        print(f"Límite de Crédito: ${self.limite_credito}")
        print(f"Intereses: {self.intereses}")

    def cobrar_interes(self):
        #TU CODIGO
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self

'''
#Crea tres tarjetas de credito
tarjeta1 = TarjetaCredito(0, 5000, 0.15)
tarjeta2 = TarjetaCredito(0, 10000, 0.20)
tarjeta3 = TarjetaCredito(0, 20000, 0.25)

#Para la primera tarjeta, haz 2 compras y un pago. Luego cobra los intereses y muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
tarjeta1.compra(2000).compra(1500).pago(500).cobrar_interes().mostrar_info_tarjeta()

#Para la segunda tarjeta, haz 3 compras y 2 pagos. Luego cobra los intereses y muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
tarjeta2.compra(3000).compra(4000).compra(2000).pago(2500).pago(1500).cobrar_interes().mostrar_info_tarjeta()

#Para la tercera tarjeta, haz 5 compras y excede su límite de crédito. Luego muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
tarjeta3.compra(5000).compra(6000).compra(7000).compra(8000).compra(9000).mostrar_info_tarjeta()

#usa el classmethod para imprimir la información de todas las tarjetas creadas
TarjetaCredito.imprimir_tarjetas()
'''