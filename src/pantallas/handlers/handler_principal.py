import json
import csv
import os
import time
import uuid
import PySimpleGUI as sg
from ..pantalla_configuracion import ventana_configuracion
from ..pantalla_juego import comenzar
from ..pantalla_puntajes import ventana_puntajes
from ..pantalla_perfiles import ventana_perfiles
from src.pantallas.handlers.handler_juego import abrir_configuracion
from roots import ROOT_PERFILES, ROOT_CONFIG, ROOT_REGISTRO

def elegir_perfil():
    """
    Funcion que genera una lista con los nick de 
    los jugadores para luego en la pantalla puedan
    ser elegidos
    """
    l = []
    with open(ROOT_PERFILES, 'r') as archivo:
        datos = json.load(archivo)
        for linea in datos:
            l.append(linea['nick'])
    return l

def eleccion_data():
    event, values = sg.Window('Elija un dataset para jugar', [[sg.Text('Elegir uno->'), sg.Listbox(['Volcan', 'Fifa', 'Lagos'], 
    size=(20, 3), key='Eleccion')],[sg.Button('Ok')]]).read(close=True)
    return event, values

def cargar_config(dif):
    """
    Funcion que carga las configuraciones para
    cada dificultad
    """
    with open(ROOT_CONFIG, 'r') as archivo:
        dicc = json.load(archivo)
    with open(ROOT_CONFIG, 'w') as archivo:
        if dif == 'Facil':
            dicc['Dificultad'] = "Facil"
        if dif == 'Normal':
            dicc['Dificultad'] = "Normal"
        if dif == 'Dificil':
            dicc['Dificultad'] = "Dificil"
        json.dump(dicc, archivo)
        sg.popup_ok('Se ha actualizado la dificultad a ', dif)


def inicializacion_partida (perfil_actual, dif):
    with open (ROOT_REGISTRO, 'a') as reg:
        writer = csv.writer(reg)
        writer.writerow([time.time(), uuid.uuid4(), "inicio_partida", perfil_actual, '', '', '', dif])


def creacion_csv():
    with open ('registro.csv', 'w') as reg:
        writer = csv.writer(reg)
        writer.writerow(["Timestamp", "ID", "Evento", "Usuario", "Estado", "Texto Ingresado", "Respuesta", "Nivel"])

def eventos(evento, ventana):
    """
    funcion que responde a los eventos que se 
    pueden originar en la llamada del modulo principal
    """
    if evento[0] == '-OK DIFI-':
        config = cargar_config(evento[1]['-COMBO DIFICULTAD-'])
    if evento[0] == "Jugar":
        perfil_actual = evento[1]['-COMBO PERFILES-']
        if perfil_actual != '':
            ventana.Hide()
            event, data = eleccion_data()
            while (not data["Eleccion"]):
                sg.popup_ok('Problemas!','Por favor seleccione un dataset.')    
                event, data = eleccion_data()
            inicializacion_partida(perfil_actual, evento[1]['-COMBO DIFICULTAD-'])
            comenzar(perfil_actual, data)
            ventana.UnHide()
        else:
            sg.popup_ok('Antes de jugar debe seleccionar un perfil')
    if evento[0] == "Configuracion":
        ventana.Hide()
        ventana_configuracion(evento[1]['-COMBO DIFICULTAD-'])
        config = abrir_configuracion()
        ventana['-COMBO DIFICULTAD-'].update(value=config['Dificultad'])
        ventana.UnHide()
    if evento[0] == "Puntajes":
        ventana.Hide()
        ventana_puntajes()
        ventana.UnHide()
    if evento[0] == "Perfiles":
        ventana.Hide()
        ventana_perfiles()
        ventana['-COMBO PERFILES-'].update(values=elegir_perfil())
        ventana.UnHide()