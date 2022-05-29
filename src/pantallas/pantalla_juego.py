import PySimpleGUI as sg
from .layouts.layout_juego import layouts


# aca va para poder abrir el archivo de los dataset para el juego
def archivo_dataset():
    pass


def comenzar():
    """
    Funcion que realiza la ejecucion de la pantalla del juego
    """
    lista = layouts()
    puntaje = 0
    # ventana del juego
    ventana = sg.Window('Figurace', lista, size=(500, 300))
    while True:
        evento = ventana.read()
        if evento[0] == sg.WIN_CLOSED or evento[0] == "Volver a la pantalla principal":
            break
    sg.popup_ok('La cantidad de puntos obtenidos es: ', puntaje)
    ventana.close()

# abrir_archivo()
