class MiClase:
    variable_clase = "Variable de clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia


print(MiClase.variable_clase)

objeto1 = MiClase("Variable Instancia")
MiClase.variable_instancia = "Modificando Variable Instancia"

print(MiClase.variable_instancia)  # Valores Distintos
print(objeto1.variable_instancia)  # Valores Distintos

# Acceso a variables de clase mediante objetos
print(objeto1.variable_clase)

# Acceso a variables de clase mediante nombre de clases
print(MiClase.variable_clase)


objeto1.variable_clase = "Modificando variable de clase"
print(objeto1.variable_clase)
print(objeto1.variable_instancia)

objeto2 = MiClase("Nuevo valor de variable de instancia")
print(objeto2.variable_clase)

objeto3 = MiClase("Tercer Objeto")
MiClase.variable_clase = "Cambio de clase"
print(objeto1.variable_clase)
print(objeto2.variable_clase)
print(objeto3.variable_clase)
