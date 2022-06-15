import PySimpleGUI as sg
from src.objects.partida import Partida
from .layouts.layout_juego import layouts
from .handlers.handler_juego import actualizar_tiempo, eventos

def comenzar():
    """
    Funcion que realiza la ejecucion de la pantalla del juego
    """
    puntaje = 0
    partida = Partida()
    # ventana del juego
    lista = layouts()
    ventana = sg.Window('Figurace', lista, size=(500, 500))
    while True and partida.ronda_actual <= partida.cant_rondas:
        evento = ventana.read(timeout=250)
        eventos(evento[0], ventana, partida)
        if evento[0] == sg.WIN_CLOSED or evento[0] == "Abandonar el juego":
            break
        actualizar_tiempo(ventana,partida)
    sg.popup_ok('La cantidad de puntos obtenidos es: ', puntaje)
    ventana.close()
