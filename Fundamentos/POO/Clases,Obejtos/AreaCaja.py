# Creacion de clase

class Caja:
    def __init__(self, alto, ancho, largo):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo

    def volumen(self):
        return self.alto * self.ancho * self.largo


# Ingreso de datos para hacer el calculo
alto = int(input("Ingrese altura:"))
ancho = int(input("Ingrese anchura:"))
largo = int(input("Ingrese longitud:"))

# Llamado de metodo para hacer calculo
caja = Caja(alto, ancho, largo)

print("El volumen de la caja es:", caja.volumen(), "")
