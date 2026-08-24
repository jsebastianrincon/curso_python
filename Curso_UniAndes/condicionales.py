edad = 200

if edad >= 0:
    if edad < 10:
        print ("Es un niño")
    elif edad > 10 and edad < 18:
        print("Es un adolecente")
    elif edad > 18 and edad < 30:
        print("Es Un adulto joven")
    else:
        print("Es un adulto mayor")
else:
    print("Ingrese una edad valida")