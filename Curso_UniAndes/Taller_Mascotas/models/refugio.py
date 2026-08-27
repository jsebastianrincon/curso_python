from .helpers import buscar_mascota


class Refugio:

    def __init__(self):
        self.__mascotas = []

    def registrar_mascota(self, mascota):
        self.__mascotas.append(mascota)

    def listar_disponibles(self):

        disponibles = []

        for mascota in self.__mascotas:

            if not mascota.adoptado:
                disponibles.append(mascota)

        return disponibles

    def asignar_adopcion(self, nombre_mascota, adoptante):

        mascota = buscar_mascota(nombre_mascota, self.__mascotas)

        if mascota is None:
            print(f"No existe una mascota con el nombre '{nombre_mascota}'.")
            return

        if mascota.adoptado:
            print(f"La mascota '{mascota.nombre}' ya fue adoptada.")
            return

        mascota.adoptado = True
        adoptante.adoptar(mascota)

        print(f" {mascota.nombre} ha sido adoptado correctamente.")