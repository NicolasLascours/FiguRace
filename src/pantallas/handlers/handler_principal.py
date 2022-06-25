import json
import csv
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
    with open(ROOT_PERFILES, 'r') as archivo:
        datos = json.load(archivo)
        l =[linea['nick'] for linea in datos]
    return l


def eleccion_data():
    """
    Funcion que da diseño a la interfaz
    para elegir los dataset
    """
    event, values = sg.Window('Elija un dataset para jugar', [[sg.Text('Elegir uno->'), sg.Listbox(['Volcan', 'Fifa', 'Lagos'], 
    size=(20, 3), key='Eleccion')], [sg.Button('Ok')]]).read(close=True)
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


def creacion_csv():
    """
    Funcion que crea el archivo csv de 
    los registros de jugadas
    """
    with open('registro.csv', 'w') as reg:
        writer = csv.writer(reg)
        writer.writerow(["Timestamp", "ID", "Objectos a adivinar", "Evento", "Usuario", "Estado", "Respuesta", "Nivel"])


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
            while not data["Eleccion"]:
                sg.popup_ok('Problemas!', 'Por favor seleccione un dataset.')
                event, data = eleccion_data()
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
