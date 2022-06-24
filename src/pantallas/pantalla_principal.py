# modulo para generar la ventana principal
import PySimpleGUI as sg
from .layouts.layout_principal import layouts_prin
from .handlers.handler_principal import eventos
from os.path import exists
from .handlers.handler_principal import creacion_csv
from roots import ROOT_REGISTRO


def start():
    #creacion del archivo csv con el registro de las partidas
    if not exists(ROOT_REGISTRO):
        creacion_csv()
    ventana = sg.Window('FiguRace', layouts_prin(), size=(500, 300))
    # creacion de ventana
    while True:
        evento = ventana.read()
        eventos(evento, ventana)
        if evento[0] == "Salir" or evento[0] == sg.WIN_CLOSED:
            break
    # mini prueba de la ventana
    ventana.close()
