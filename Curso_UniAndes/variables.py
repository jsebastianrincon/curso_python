import platform
import os

#obteniendo informacion del sistema
sistema = platform.system()
version = platform.version()
directorio = os.getcwd()

#mostrar informacion
print("!Hola Mundo desde Pyton!")
print(f"Sistema operativo:{sistema}")
print(f"Version {version}")
print(f"Directorio Actual:{directorio}")