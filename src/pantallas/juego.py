import os
import json
import PySimpleGUI as sg
def abrir_archivo ():
    """
    funcion para poder abrir el archivo json
    de las configuraciones del juego
    """
    #ruta = os.path.dirname(os.path.realpath("."))
    ruta_archivo = os.path.join('src', 'layouts','pantallas','configuracion', 'config.json')
    archivo_json = open (ruta_archivo, 'r')
    datos = json.load(archivo_json)
    return datos
    
# aca va para poder abrir el archivo de los dataset para el juego
def archivo_dataset():
    pass

# layout de la pantalla del juego
def layouts ():
    """
    funcion que define el diseño de la 
    pantalla del juego 
    """
    datos = abrir_archivo()
    print(datos)
    layout = [
        [sg.Text('Volcanes!!')],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Text('Caracteristicas'), sg.Text('Cantidad de rondas {}'.format(datos['Rondas']))],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Button("Volver a la pantalla principal")],
        ] 
    return layout

def comenzar():
    lista = layouts()
    # ventana del juego
    ventana = sg.Window('Figurace', lista, size=(500, 300))
    while True:
        evento = ventana.read()
        if evento[0] == sg.WIN_CLOSED or evento[0] == "Volver a la pantalla principal":
            break
    ventana.close()

#abrir_archivo()