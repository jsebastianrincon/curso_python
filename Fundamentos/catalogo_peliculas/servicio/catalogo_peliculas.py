import os


class CatalogoPeliculas:

    ruta_archivo = "peliculas.txt"

    @staticmethod
    def agregar_pelicula(pelicula):
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, "a")
            archivo.write(pelicula.__str__())
        except Exception as e:
            print("Excepcion al agregar:", e)
        finally:
            archivo.close()

    @staticmethod
    def listar_peliculas():
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, "w")
            print("Catalogo de peliculas")
            print(archivo.read())
        except Exception as e:
            ("Ocurrio un error al listar peliculas:")
        finally:
            archivo.close()

    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta_archivo)
            print("Archivo Eliminado:", CatalogoPeliculas)
        except Exception as e:
            print("Error al eliminar pelicula", e)
