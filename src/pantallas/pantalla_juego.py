import PySimpleGUI as sg
import os
from .layouts.layout_juego import layouts
from .handlers.handler_juego import eventos
from .handlers.handler_juego import abrir_configuracion
from .handlers.handler_juego import abrir_dificultad

def comenzar():
    """
    Funcion que realiza la ejecucion de la pantalla del juego
    """
    puntaje = 0
    ronda_act = 1
    try:
        ruta_archivo = os.path.join('config.json')
        archivo_json = open(ruta_archivo, 'r')
    except FileNotFoundError:
        sg.popup_error('Parece que no pusiste las configuraciones... Intentalo de nuevo')
    # ventana del juego
    else:
        lista = layouts()
        ventana = sg.Window('Figurace', lista, size=(500, 500))
        while True and ronda_act <= 10:
            evento = ventana.read()
            ronda_act = eventos (evento[0], ronda_act)
            if evento[0] == sg.WIN_CLOSED or evento[0] == "Abandonar el juego":
                break
            ventana.refresh()
        sg.popup_ok('La cantidad de puntos obtenidos es: ', puntaje)
        ventana.close()