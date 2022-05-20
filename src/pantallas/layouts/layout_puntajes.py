# importo modulos
import PySimpleGUI as sg


def layout_puntajes():
    """crea el layout para la pantalla puntajes"""
    # creo el layout
    layout = [
        [sg.Column([[sg.Button('Facil', size=(10, 2))],
                    [sg.Button('Medio', size=(10, 2))],
                    [sg.Button('Dificil', size=(10, 2))]], justification='left')],
        [sg.Column([[sg.Button("Volver", size=(10, 2))]], justification='right')]
    ]
    return layout
