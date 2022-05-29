import os
import json

def abrir_configuracion ():
    """
    funcion para poder abrir el archivo json
    de las configuraciones del juego
    """
    ruta_archivo = os.path.join('config.json')
    archivo_json = open(ruta_archivo, 'r')
    datos = json.load(archivo_json)
    archivo_json.close()
    return datos

def abrir_dificultad ():
    """
    Funcion para poder abrir el archivo json
    de la dificultad del juego
    """
    ruta_archivo = os.path.join('dificultad.json')
    archivo_json = open(ruta_archivo, 'r')
    datos = json.load(archivo_json)
    archivo_json.close()
    return datos

def eventos(evento, ronda_act):
    if evento == 'Pasar':
        ronda_act += 1
    return ronda_act