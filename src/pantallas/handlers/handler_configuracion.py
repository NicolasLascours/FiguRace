import json
import PySimpleGUI as sg
def evento_config(b, evento, values):
    """
    funcion que verifica el evento realizado en la pantalla
    """
    if (evento == 'Submit'):
        if b == True:
            with open ('config.json', 'w') as archivo_json:
                json.dump(values, archivo_json)
            sg.popup_ok('Las configuraciones han sido guardadas con exito')