from orden import Orden
from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado

tecladoHP = Teclado("HP", "USB")
ratonHP = Raton("HP", "USB")
monitorLG = Monitor("LG", "30 pulgadas")
computadoraHP = Computadora("HP", monitorLG, tecladoHP, ratonHP)

teclado_acer = Teclado("Acer", "USB")
raton_acer = Raton("Acer", "Bluetooth")
monitor_acer = Monitor("Acer", "45 pulgadas")
computadora_acer = Computadora("Acer", monitor_acer, teclado_acer, raton_acer)

computadora_clon = Computadora("Clon", monitorLG, teclado_acer, ratonHP)

computadora_orden1 = [computadoraHP, computadora_acer, computadora_clon]

orden1 = Orden(computadora_orden1)
print("\n")
print(orden1)
