# importo modulos
import PySimpleGUI as sg


def layout_perfiles():
    """crea el layout para la pantalla perfiles"""
    # creo el layout
    layout = [
        [sg.Column([[sg.Button('Crear nuevo perfil', size=(10, 2))],
                    [sg.Button('Editar uno existente', size=(10, 2))]], justification='left')],
        [sg.Column([[sg.Button("Volver", size=(10, 2))]], justification='right')]
    ]
    return layout
