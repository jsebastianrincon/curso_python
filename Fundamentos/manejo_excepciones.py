# Manejo de excepciones para el control de errores y continuar la ejecucion
from numero_identicos_exception import NumeroIdenticosException

resultado = None
try:
    a = int(input("Ingrese primer valor:"))
    b = int(input("Ingrese segundo valor:"))
    if a == b:
        raise NumeroIdenticosException("numeros identicos")
    resultado = a / b

# Manejo de excpeciones por division en 0

except ZeroDivisionError as e:
    print("Ocurrio un error con ZeroDivisionError", e)
    print(type(e))
except TypeError as e:
    print("Ocurrio un error con TypeError", e)
    print(type(e))
# except ValueError as e:
#    print("Ocurrio un error con ValueError", e)
#    print(type(e))
except Exception as e:
    print("Ocurrio un error con exception", e)
    print(type(e))

else:
    print("No hubo ninguna excepcion")
finally:
    print("Fin de control de excepciones")

print("resultado:", resultado)
print("Continuamos...")
