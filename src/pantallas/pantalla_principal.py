# modulo para generar la ventana principal
import PySimpleGUI as sg
from .layouts.layout_principal import layouts_prin
from .handlers.handler_principal import eventos
from os.path import exists
import os
from .handlers.handler_principal import creacion_csv


def start():
    #creacion del archivo csv con el registro de las partidas
    ROOT_DIR = os.path.abspath(os.curdir)
    if not exists(os.path.join(ROOT_DIR, 'Registro.csv')):
        creacion_csv()
    ventana = sg.Window('FiguRace', layouts_prin(), size=(500, 300))
    # creacion de ventana
    while True:
        evento = ventana.read()
        eventos(evento, ventana, ROOT_DIR)
        if evento[0] == "Salir" or evento[0] == sg.WIN_CLOSED:
            break
    # mini prueba de la ventana
    ventana.close()
