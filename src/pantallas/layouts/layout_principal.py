import PySimpleGUI as sg
from ..handlers.handler_juego import abrir_configuracion
from ..handlers.handler_principal import elegir_perfil
# color seleccionado para la ventana


def layouts_prin():
    """
    funcion que define el diseño de la ventana
    de la pantalla principal
    """
    # color seleccionado para la ventana
    sg.theme("LightGreen10")
    # diseño
    config = abrir_configuracion()
    layout = [
        [sg.Button("Configuracion",
         size=(10, 2)), sg.Text(' '*47),
         sg.Text('Ingrese un perfil para jugar')],
        [sg.Text(' '*78),  sg.Combo(elegir_perfil(), readonly=True,
         key='-COMBO PERFILES-', size=(12, 1))],
        [sg.Column([[sg.Text("FIGURACE")]], justification='center')],
        [sg.Column([[sg.Button("Jugar", size=(5, 2))]],
         justification='center')],
        [sg.Text(' '*77), sg.Text('Elija la dificultad')],
        [sg.Text(' '*78), sg.Combo(['Facil', 'Normal', 'Dificil'],
         default_value=config['Dificultad'],
         readonly=True, key='-COMBO DIFICULTAD-', size=(12, 1)),
         sg.Button('OK', key='-OK DIFI-')],
        [sg.Text(' '*86)],
        [sg.Button("Perfiles", size=(10, 2)), sg.Text(' '*19),
         sg.Button("Salir", size=(10, 2)), sg.Text(' '*20), 
         sg.Button("Puntajes", size=(10, 2))]
        ]
    return layout
