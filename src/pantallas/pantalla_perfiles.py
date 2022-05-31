# importo modulos a usar
from .layouts.layout_perfiles import layout_perfiles
from .handlers.handler_perfiles import handler_perfiles
import PySimpleGUI as sg


def ventana_perfiles():
    """"Crea y ejecuta la pantalla de perfiles"""
    # creo ventana perfiles
    sg.theme('LightBlue4')
    window = sg.Window("Perfiles", layout_perfiles(), margins=(200, 150))
    # creo el bucle
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Volver":
            break
        else:
            window.Hide()
            # llamo al modulo handler pasandole el evento que se produjo
            handler_perfiles(event)
            window.UnHide()
    # cierro la ventana
    window.close()
