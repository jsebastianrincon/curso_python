

#funcion para filtrar los aprobado

def filtrar_aprobado(estudiantes: list, nota_minima: int = 80)-> list:
    estudiantes_aprobados = []
    for estudiante in estudiantes:
        if estudiante["nota"] >= nota_minima:
            estudiantes_aprobados.append(estudiante)
    return estudiantes_aprobados

estudiantes = [
    {"nombre": "Juan", "nota":50},
    {"nombre": "Sebastian", "nota":80},
    {"nombre": "Alejandra", "nota":100},
    {"nombre": "Pablo", "nota":40},
    {"nombre": "Ana", "nota":60}
]

aprobados = filtrar_aprobado(estudiantes,70)
for aprobado in aprobados:
    print(aprobado["nombre"])