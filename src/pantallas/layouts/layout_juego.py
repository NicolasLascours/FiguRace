import PySimpleGUI as sg
import json
import os
import datetime
from ..handlers.handler_juego import abrir_configuracion

# layout de la pantalla del juego
def layouts ():
    """
    funcion que define el diseño de la 
    pantalla del juego 
    """
    config = abrir_configuracion()
    if config['Caracteristicas'] == "1":
        layout = [
            [sg.Text('Volcanes!!'), sg.Text(' '*74), sg.Text('Dificultad')],
            [sg.Text(' '*93), sg.Text(config['Dificultad'])],
            [sg.Text('')],
            [sg.Text('Caracteristicas'), sg.Text('Ronda actual 1'),
             sg.Text('Cantidad de rondas {}'.format(config['Rondas'])),
             sg.Text('Tiempo: ')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text('Pais:')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Button('Opcion 1')],
            [sg.Button('Opcion 2')],
            [sg.Button('Opcion 3')],
            [sg.Button('Opcion 4')],
            [sg.Button('Opcion 5')],
            [sg.Button("Pasar"), sg.Button('OK') ,sg.Text(' '*61),
             sg.Button('Abandonar el juego')],
        ] 
    if config['Caracteristicas'] == "3":
        layout = [
            [sg.Text('Volcanes!!'), sg.Text(' '*74), sg.Text('Dificultad')],
            [sg.Text(' '*93), sg.Text(config['Dificultad'])],
            [sg.Text('')],
            [sg.Text('Caracteristicas'), sg.Text('Ronda actual 1'),
             sg.Text('Cantidad de rondas {}'.format(config['Rondas'])),
             sg.Text('Tiempo: ')],
            [sg.Text('')],
            [sg.Text('Pais: ')],
            [sg.Text('')],
            [sg.Text('Ubicacion: ')],
            [sg.Text('')],
            [sg.Text('Elevacion: ')],
            [sg.Text('')],
            [sg.Button('Opcion 1')],
            [sg.Button('Opcion 2')],
            [sg.Button('Opcion 3')],
            [sg.Button('Opcion 4')],
            [sg.Button('Opcion 5')],
            [sg.Button("Pasar"), sg.Button('OK') ,sg.Text(' '*61),
             sg.Button('Abandonar el juego')],
        ]
    if config['Caracteristicas'] == "5":
        layout = [
            [sg.Text('Volcanes!!'), sg.Text(' '*74), sg.Text('Dificultad')],
            [sg.Text(' '*93), sg.Text(config['Dificultad'])],
            [sg.Text('')],
            [sg.Text('Caracteristicas'), sg.Text('Ronda actual 1'),
             sg.Text('Cantidad de rondas {}'.format(config['Rondas'])),
             sg.Text('Tiempo: ')],
            [sg.Text('')],
            [sg.Text('Pais: ')],
            [sg.Text('Tipo: ')],
            [sg.Text('Ubicacion: ')],
            [sg.Text('Estado: ')],
            [sg.Text('Elevacion: ')],
            [sg.Text('')],
            [sg.Button('Opcion 1')],
            [sg.Button('Opcion 2')],
            [sg.Button('Opcion 3')],
            [sg.Button('Opcion 4')],
            [sg.Button('Opcion 5')],
            [sg.Button("Pasar"), sg.Button('OK') ,sg.Text(' '*61),
             sg.Button('Abandonar el juego')],
        ]
    return layout