class Orden:
    contador_ordenes = 0

# Inicializacion de variables y atributos

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        # Variable Privada
        self.__id_orden = Orden.contador_ordenes
        self.__productos = productos

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.__productos:
            total += producto.get_precio()
        return total

    def __str__(self):
      # Iteracion de cada uno de los registros
        productos_str = ""
        for producto in self.__productos:
            productos_str += producto.__str__() + " | "

        return "Orden: " + str(self.__id_orden) + ", Productos" + productos_str
