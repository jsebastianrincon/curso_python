# Imprimir solo letras a

for letra in "Holanda":
    if letra == "a":
        print(letra)
        break
    else:
        print("Fin")

# Imprimir solo numeros pares

for i in range(6):
    # Residuo
    if i % 2 != 0:
        continue
    print(i)
