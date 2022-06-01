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
    header_volcan, data_volcan = abrir_volcanes()
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
            [sg.Text('Pais:{}'.format(data_volcan[0][0]) )],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Button('{}'.format(data_volcan[2][5]))],
            [sg.Button('{}'.format(data_volcan[3][5]))],
            [sg.Button('{}'.format(data_volcan[0][5]))],
            [sg.Button('{}'.format(data_volcan[1][5]))],
            [sg.Button('{}'.format(data_volcan[4][5]))],
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
            [sg.Text('Año: {}'.format(data_volcan[0][0]))],
            [sg.Text('')],
            [sg.Text('Tipo de volcan: {}'.format(data_volcan[0][1]))],
            [sg.Text('')],
            [sg.Text('Nombre y ciudad: {}'.format(data_volcan[0][2]))],
            [sg.Text('')],
            [sg.Button('{}'.format(data_volcan[2][5]))],
            [sg.Button('{}'.format(data_volcan[3][5]))],
            [sg.Button('{}'.format(data_volcan[0][5]))],
            [sg.Button('{}'.format(data_volcan[1][5]))],
            [sg.Button('{}'.format(data_volcan[4][5]))],
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
            [sg.Text('Año: {}'.format(data_volcan[0][0]))],
            [sg.Text('Bandera terremoto: {}'.format(data_volcan[0][4]))],
            [sg.Text('Nombre y ciudad: {}'.format(data_volcan[0][2]))],
            [sg.Text('Indice de explosividad volcanica: {}'.format(data_volcan[0][1]))],
            [sg.Text('Bandera Tsunami: {}'.format(data_volcan[0][3]))],
            [sg.Text('')],
            [sg.Button('{}'.format(data_volcan[2][5]))],
            [sg.Button('{}'.format(data_volcan[3][5]))],
            [sg.Button('{}'.format(data_volcan[0][5]))],
            [sg.Button('{}'.format(data_volcan[1][5]))],
            [sg.Button('{}'.format(data_volcan[4][5]))],
            [sg.Button("Pasar"), sg.Button('OK') ,sg.Text(' '*61),
             sg.Button('Abandonar el juego')],
        ]
    return layout