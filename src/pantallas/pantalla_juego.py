import PySimpleGUI as sg
from src.objects.partida import Partida
from .layouts.layout_juego import layouts, config_inicial
from .handlers.handler_juego import abrir_configuracion, actualizar_tiempo, eventos
from .handlers.handler_juego import inicializacion_partida, registro_jugadas, actualizacion
from roots import ROOT_PUNTAJES
from .handlers.handler_perfiles import datos_de_perfiles, obtener_datos_nick
import csv


def guardar_partida(perfil_actual, estado, puntaje, dificultad):
    """Funcion que guarda los datos de una partida en el csv de puntajes"""
    datos = datos_de_perfiles()
    informacion = obtener_datos_nick(perfil_actual, datos)
    with open(ROOT_PUNTAJES, 'a', encoding='utf_8') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([perfil_actual, informacion[0]["genero"], estado, puntaje, dificultad])


def act_completa(ventana, cant, header, datos):
    """
    Funcion que realiza la actualizacion completa
    de la pantalla
    """
    lista_data = []
    lista_carac = ['', '', '', '', '']
    correcta, lista_data, lista_carac = config_inicial(lista_data, datos, cant, lista_carac)
    actualizacion(ventana, lista_data, cant, header, lista_carac)
    return correcta, lista_data, lista_carac


def comenzar(perfil_actual, data):
    """
    Funcion que realiza la ejecucion de la pantalla del juego
    """
    # ventana del juego
    lista_data = []
    lista_carac = ['', '', '', '', '']
    partida = Partida()
    config = abrir_configuracion()
    inicializacion_partida(perfil_actual, config['Dificultad'], partida.uuid)
    lista, cant, datos, correcta, header = layouts(data, lista_data, lista_carac, config)
    ventana = sg.Window('Figurace', lista, size=(500, 500))
    while True and partida.ronda_actual <= partida.cant_rondas:
        evento = ventana.read(timeout=250)
        if evento[0] != "__TIMEOUT__" and (evento[0] != sg.WIN_CLOSED or evento[0] != "Abandonar el juego"):
            eventos(evento[0], ventana, partida, correcta, lista_data, perfil_actual)
            correcta, lista_data, lista_carac = act_completa(ventana, cant, header, datos)
        if evento[0] == sg.WIN_CLOSED or evento[0] == "Abandonar el juego":
            registro_jugadas(evento[0], perfil_actual, correcta,  partida)
            guardar_partida(perfil_actual, "Cancelada", partida.puntaje(), config["Dificultad"])
            break
        restante = actualizar_tiempo(ventana, partida, evento[0], perfil_actual, correcta)
        if evento[0] == "__TIMEOUT__" and restante <= 0:
           correcta, lista_data, lista_carac = act_completa(ventana, cant, header, datos)
    sg.popup_ok('La cantidad de puntos obtenidos es: ', partida.puntaje())
    if partida.ronda_actual > partida.cant_rondas:
        registro_jugadas(evento[0], perfil_actual, correcta, partida)
        guardar_partida(perfil_actual, "Finalizada", partida.puntaje(), config["Dificultad"])
    ventana.close()
