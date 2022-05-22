# modulo para generar la ventana principal
import json
import PySimpleGUI as sg
from .layouts.layout_principal import layouts_prin
from .handlers.handler_principal import eventos

def start ():
    ventana = sg.Window('FiguRace', layouts_prin(), size=(500,300))
    # creacion de ventana
    while True:
        evento = ventana.read()
        eventos(evento, ventana)
        if evento[0] == "Salir" or evento[0] == sg.WIN_CLOSED:
            break
    # mini prueba de la ventana
    ventana.close()