class Producto:
    # Variable que solo esta asociada a la calse Producto
    contador_productos = 0

    # Metodo constructor
    def __init__(self, nombre, precio):
        # Incremento de la variable (Contador)
        Producto.contador_productos += 1
        # Asignacion privada
        self.__id_producto = Producto.contador_productos
        self.__nombre = nombre
        self.__precio = precio

    def get_precio(self):
        return self.__precio

    def __str__(self):
        return "Id Producto: " + str(self.__id_producto) + ", Nombre: " + self.__nombre + ", Precio: " + str(self.__precio)
