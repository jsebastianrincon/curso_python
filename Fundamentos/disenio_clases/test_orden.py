from producto import Producto
from orden import Orden

producto1 = Producto("Camisa", 100000)
producto2 = Producto("Pantalon", 150000)
producto3 = Producto("Medias", 5000)

productos = [producto1, producto2]

orden1 = Orden(productos)

print(orden1)
print(orden1.calcular_total())

# productos.append(Producto3)
orden2 = Orden(productos)
orden2.agregar_producto(producto3)
print(orden2)
print(orden2.calcular_total())
