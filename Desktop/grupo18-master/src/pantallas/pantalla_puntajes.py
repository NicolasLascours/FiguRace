# importo modulos a usar
from .layouts.layout_puntajes import layout_puntajes
from .handlers.handler_puntajes import handler_puntajes
import PySimpleGUI as sg

def ventana_puntajes():
    # creo ventana puntajes
    sg.theme('LightBlue4')
    window = sg.Window("Puntajes", layout_puntajes(), margins=(200, 150))
    # creo el bucle
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Volver":
            break
    # cierro la ventana
    window.close()
