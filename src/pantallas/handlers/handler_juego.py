import os
import json

def abrir_configuracion ():
    """
    funcion para poder abrir el archivo json
    de las configuraciones del juego
    """
    ruta_archivo = os.path.join('config.json')
    archivo_json = open (ruta_archivo, 'r')
    datos = json.load(archivo_json)
    return datos
