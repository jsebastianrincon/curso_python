dia = 8

match dia:
    case 1:
        print("Hoy es lunes")
    case 2:
        print("Hoy es martes")
    case 3:
        print("Hoy es miercoles")
    case 4:
        print("Hoy es jueves")
    case 5:
        print("Hoy es viernes")
    case 6:
        print("Hoy es sabado")
    case 7:
        print("Hoy es domingo")
    case _:
        print("Día no reconocido, por favor escoge un día válido de la semana")