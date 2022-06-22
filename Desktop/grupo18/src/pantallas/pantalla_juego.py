from xml.dom.minidom import Element
import PySimpleGUI as sg
from src.objects.partida import Partida
import random
from .layouts.layout_juego import layouts, config_inicial
from .handlers.handler_juego import abrir_configuracion, actualizar_tiempo, eventos, registro_jugadas, actualizacion

def act_completa(ventana, cant, header, datos):
    lista_data = []
    lista_carac = ['', '', '', '', '']
    correcta, lista_data, lista_carac = config_inicial(lista_data, datos, cant, lista_carac)
    actualizacion(ventana, lista_data, cant, header, lista_carac)
    return correcta, lista_data, lista_carac

def comenzar(ROOT_DIR, perfil_actual, data):
    """
    Funcion que realiza la ejecucion de la pantalla del juego
    """
    partida = Partida()
    # ventana del juego
    lista_data = []
    lista_carac = ['', '', '', '', '']
    config = abrir_configuracion()
    lista, cant, datos, correcta, header = layouts(data, lista_data, lista_carac ,config)
    ventana = sg.Window('Figurace', lista, size=(500, 500))
    while True and partida.ronda_actual <= partida.cant_rondas:
        evento = ventana.read(timeout=250)
        if evento[0] != "__TIMEOUT__" and (evento[0] != sg.WIN_CLOSED or evento[0] != "Abandonar el juego"):
            eventos(evento[0], ventana ,partida, ROOT_DIR ,correcta, lista_data, perfil_actual)
            correcta, lista_data, lista_carac = act_completa(ventana, cant, header, datos)
        if evento[0] == sg.WIN_CLOSED or evento[0] == "Abandonar el juego":
            registro_jugadas(evento[0], ROOT_DIR, perfil_actual, correcta, lista_data, '')
            break
        restante = actualizar_tiempo(ventana,partida)
        if evento[0] == "__TIMEOUT__" and restante <= 0:
           registro_jugadas (evento[0], ROOT_DIR, perfil_actual)
           correcta, lista_data, lista_carac = act_completa(ventana, cant, header, datos)
    sg.popup_ok('La cantidad de puntos obtenidos es: ', partida.puntaje())
    if evento[0] != "Abandonar el juego" and evento[0] != sg.WIN_CLOSED:
        registro_jugadas(evento[0], ROOT_DIR, perfil_actual, correcta, lista_data, '')
    ventana.close()