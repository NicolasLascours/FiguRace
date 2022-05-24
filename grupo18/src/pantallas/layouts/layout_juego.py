import PySimpleGUI as sg
import json
import os

def abrir_archivo ():
    """
    funcion para poder abrir el archivo json
    de las configuraciones del juego
    """
    ruta_archivo = os.path.join('config.json')
    archivo_json = open (ruta_archivo, 'r')
    datos = json.load(archivo_json)
    return datos

# layout de la pantalla del juego
def layouts ():
    """
    funcion que define el diseño de la 
    pantalla del juego 
    """
    datos = abrir_archivo()
    layout = [
        [sg.Text('Volcanes!!')],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Text('Caracteristicas'), sg.Text('Cantidad de rondas {}'.format(datos['Rondas']))],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Button("Volver a la pantalla principal")],
        ] 
    return layout