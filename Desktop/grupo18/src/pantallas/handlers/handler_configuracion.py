import json
import PySimpleGUI as sg
from roots import ROOT_CONFIG

def evento_config(b, evento, values):
    """
    funcion que verifica el evento realizado en la pantalla y 
    lo carga en el archivo config.json
    """
    if evento == 'Submit':
        if b:
            with open(ROOT_CONFIG, 'w') as archivo_json:
                json.dump(values, archivo_json)
            sg.popup_ok('Las configuraciones han sido guardadas con exito')
