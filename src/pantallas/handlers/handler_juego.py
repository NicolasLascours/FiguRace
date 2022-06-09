import os
import json
from roots import ROOT_VOLCANS, ROOT_LAGOS, ROOT_FIFA, ROOT_CONFIG
import csv


def abrir_volcanes():
    """
    Abre el datasets de volcanes y retorna el encabezado
    y una lista con las filas de archivo
    """
    with open(ROOT_VOLCANS, encoding='utf_8') as dataset:
        csvreader = csv.reader(dataset, delimiter=',')
        header, data = next(csvreader), list(csvreader)
    return header, data


def abrir_lagos():
    """
    Abre el datasets de lagos y retorna el encabezado
    y una lista con las filas de archivo
    """
    with open(ROOT_LAGOS, encoding='utf_8') as dataset:
        csvreader = csv.reader(dataset, delimiter=',')
        header, data = next(csvreader), list(csvreader)
    return header, data


def abrir_fifa():
    """
    Abre el datasets de fifa y retorna el encabezado
    y una lista con las filas de archivo
    """
    with open(ROOT_FIFA, encoding='utf_8') as dataset:
        csvreader = csv.reader(dataset, delimiter=',')
        header, data = next(csvreader), list(csvreader)
    return header, data


def abrir_configuracion():
    """
    Abre el archivo json de las configuraciones del juego y retorna los datos.
    En caso de no encontrar el archivo, lo crea en la direccion correcta y lo
    carga con una dificultad por defecto.
    """
    try:
        with open(ROOT_CONFIG, 'r') as archivo_json:
            datos = json.load(archivo_json)
            return datos
    except FileNotFoundError:
        dif_por_defecto = {"Tiempo": "60",
                           "Rondas": "4",
                           "Puntaje Sumado": "50",
                           "Puntaje Restado": "20",
                           "Caracteristicas": "3",
                           "Dificultad": "Normal"}
        # Si no encuentra el archivo en la ruta, lo crea con valores por defecto
        with open(ROOT_CONFIG, 'x') as archivo_json:
            json.dump(dif_por_defecto, archivo_json)
            return dif_por_defecto    


def convert(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


def eventos(evento, ronda_act):
    """
    Funcion que controla la logica y
    eventos que ocurren en el juego
    """
    if evento == 'Pasar':
        ronda_act += 1
    return ronda_act