# modulo para generar la ventana principal
import json
import PySimpleGUI as sg
from ..configuracion.configuracion_pantalla import ventana_configuracion
from ..juego.juego import comenzar

# color seleccionado para la ventana 
sg.theme("LightGreen10")
LayOut = [
         [sg.Button("Configuracion", size=(10, 2)), sg.Text('                                               '), sg.Text('Ingrese un perfil para jugar')],
         [sg.Text('                                                                                         '), sg.Combo('0')],# esto deberia sacar la lista con los usuarios, me falta la lista de usuarios y como mostrarlos
         [sg.Column([[sg.Text("FIGURACE")]],justification='center')],
         [sg.Column([[sg.Button("Jugar", size=(5, 2))]], justification='center')],
         [sg.Text('                                                                             '), sg.Text('Eliga la dificultad')],
         [sg.Text('                                                                                  '), sg.Combo(['Facil', 'Normal', 'Dificil']), sg.Button('OK')],
         [sg.Text(' ')],
         [sg.Button("Perfiles", size=(10, 2)), sg.Text('                   '), sg.Button("Salir", size=(10, 2)), sg.Text('                    '), sg.Button("Puntajes", size=(10, 2))]
         ] 
# lista con acciones para hacer en pantalla, por ahora solo los bottones

def eventos(evento):
    """
    funcion que responde a los eventos que se 
    pueden originar en la llamada del modulo principal
    """
    print(evento[0])
    if evento[0] == 'OK':
        with open ('dificultad.json', 'w') as archivo_config:
            json.dump(evento[0], archivo_config)
    if evento[0] == "Jugar":
        comenzar()
    if evento[0] == "Configuracion":
         ventana_configuracion()
         pass
    if evento[0] == "Puntajes":
         pass
    if evento[0] == "Perfiles":
         pass

def start ():
    ventana = sg.Window('FiguRace', LayOut, size=(500,300))
    # creacion de ventana
    while True:
        evento = ventana.read()
        eventos(evento)
        if evento[0] == "Salir" or evento[0] == sg.WIN_CLOSED:
            break
    # mini prueba de la ventana
    ventana.close()