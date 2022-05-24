# importo modulos
import json
import PySimpleGUI as sg

def abrir_archivo ():
    """
    Funcion para obtener los puntajes
    """
    with open ('perfiles.json', 'r') as archivo:
        datos = json.load(archivo)
    l = []
    for linea in datos:
        tupla = (linea['nick'], linea['puntaje']) 
        l.append(tupla)
    sorted(l)
    return l

def layout_puntajes():
    """
    crea el layout para la pantalla puntajes
    """
    # creo el layout
    layout = [
             [sg.popup_scrolled(abrir_archivo(), title='Puntajes de jugadores')]
             ]
    return layout