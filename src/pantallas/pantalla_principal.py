# modulo para generar la ventana principal
import PySimpleGUI as sg
from .layouts.layout_principal import layouts_prin
from .handlers.handler_principal import eventos


def start():
    # Diccionario que se manda como parametro por referencia
    perfil_actual = {'nick': ''}

    ventana = sg.Window('FiguRace', layouts_prin(), size=(500, 300))
    # creacion de ventana
    while True:
        evento = ventana.read()
        eventos(evento, ventana, perfil_actual)
        if evento[0] == "Salir" or evento[0] == sg.WIN_CLOSED:
            break
    # mini prueba de la ventana
    ventana.close()
