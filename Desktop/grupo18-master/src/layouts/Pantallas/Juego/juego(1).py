import os
import json
import PySimpleGUI as sg
def abrir_archivo ():
    """funcion para poder abrir el archivo json
    de las configuraciones del juego"""
    ruta = os.path.dirname(os.path.realpath("."))
    ruta_archivo = os.path.join(ruta, 'Configuracion', 'config.json')
    archivo_json = open (ruta_archivo, 'r')
    datos = json.load(archivo_json)
    return datos
    # aca va para poder abrir el archivo de los dataset para el juego
# layout de la pantalla del juego
layout = [
         [sg.Text('Volcanes!!')],
         [sg.Text('')],
         [sg.Text('')],
         [sg.Text('Caracteristicas')],
         [sg.Text('')],
         [sg.Text('')],
         [sg.Text('')],
         [sg.Button("""Volver a la pantalla principal""")],
         ] 
# ventana del juego
ventana = sg.Window('Figurace', layout, size=(500, 300))

while True:
    evento = ventana.read()
    if evento[0] == sg.WIN_CLOSED:
        break

ventana.close()

#abrir_archivo()