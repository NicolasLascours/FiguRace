import PySimpleGUI as sg
import json
from ..handlers.handler_juego import abrir_configuracion


def abrir_archivo():
    """
    funcion para poder abrir el archivo json
    de las configuraciones del juego
    """
    with open('config.json', 'r') as archivo:
        datos = json.load(archivo)
    return datos

# layout de la pantalla del juego


def layouts():
    """
    funcion que define el diseño de la 
    pantalla del juego 
    """
    dato = abrir_archivo()
    datos = abrir_configuracion()
    layout = [
        [sg.Text('Volcanes!!'), sg.Text('        '), sg.Text('Dificultad')],
        [sg.Text('                               '), sg.Text()],
        [sg.Text('')],
        [sg.Text('Caracteristicas'), sg.Text('Cantidad de rondas {}'.format(dato['Rondas']))],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Button("Abandonar el juego"), sg.Text('              '), sg.Button('Pasar de ronda')],
        ] 
    return layout
