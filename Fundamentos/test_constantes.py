# Se importa toda la informacion del archivo
from constantes import MI_CONSTANTE
from constantes import Matematicas as mate

print(MI_CONSTANTE)
print(mate.PI)

# Asignacion de un nuevo valor a una constante relativa
MI_CONSTANTE = "Nuevo Valor"
mate.PI = 3.14
print(MI_CONSTANTE)
print(mate.PI)
