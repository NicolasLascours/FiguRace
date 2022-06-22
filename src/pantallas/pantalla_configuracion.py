# zona de imports
import PySimpleGUI as sg
from .layouts.layout_configuracion import layout
from .handlers.handler_configuracion import evento_config


def verificar_json(values):
    """
    esta funcion verifica si se ingresaron todas las
    configuraciones requeridas
    """
    b = True
    if (values['Tiempo'] == '' or values['Rondas'] == '' or values['Puntaje Sumado'] == '' or
            values['Puntaje Restado'] == '' or values["Facil"] == '' or values["Normal"] == '' or
            values["Dificil"] == ''):
        sg.popup_ok('Problemas!', 'Debe seleccionar un valor en todas las casillas.')
        b = False
    return b


def ventana_configuracion(dif): 
    """
    funcion que ejecuta la ventana con su
    diseño propio, con todas las funcionalidades
    requeridas para la configuracion del juego
    """
    sg.theme('LightBlue4')
    # variable ventana con las caracteristicas de la misma
    lista = layout()
    # ventana variable que tiene los layout y el tamaño de pantalla
    ventana = sg.Window('Configuracion', lista, size=(450, 400))
    # ejecucion del while
    while True:
        evento, values = ventana.read()
        if evento == sg.WIN_CLOSED or evento == 'Volver':
            break
        b = verificar_json(values)
        values['Dificultad'] = dif
        evento_config(b, evento, values)
    ventana.close()
