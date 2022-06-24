import PySimpleGUI as sg
import random
from ..handlers.handler_juego import convert, abrir_volcanes, abrir_lagos, abrir_fifa


# layout de la pantalla del juego

def config_inicial(lista_data, datos, cant, lista_carac):
    for i in range(5):
        lista_data.append(random.choice(list(datos)))
    correcta = lista_data[random.randint(0, 4)]
    for i in range(int(cant)):
        lista_carac[i] = correcta[i]
    return correcta, lista_data, lista_carac


def eleccion(data):
    if data['Eleccion'][0] == 'Volcan':
        header, datos = abrir_volcanes()
        nom = "Volcanes!!"
    elif data['Eleccion'][0] == 'Fifa':
        header, datos = abrir_fifa()
        nom = "Fifa!!"
    elif data['Eleccion'][0] == 'Lagos':
        header, datos = abrir_lagos()
        nom = "Lagos!!"
    return datos, header, nom


def layouts(data, lista_data, lista_carac, config):
    """
    funcion que define el diseño de la
    pantalla del juego
    """
    datos, header, nom = eleccion(data)
    cant = config[config["Dificultad"]]
    correcta, lista_data, lista_carac = config_inicial(lista_data, datos, cant, lista_carac)
    layout = [
        [sg.Text(nom, key='-TITULO-'), sg.Text(' '*74), sg.Text('Dificultad')],
        [sg.Text(' '*93), sg.Text(config['Dificultad'])],
        [sg.Text('')],
        [sg.Text('Ronda actual: 1', key='-RONDAS-'),
        sg.Text('Cantidad de rondas {}'.format(config['Rondas'])),
        sg.Text('Tiempo: {}'.format(convert(int(config['Tiempo']))), key='-TIEMPO-')],
        [sg.Text(' '*45), sg.Text('Puntaje: 0', key='-Puntaje-')],
        [sg.Text('Caracteristicas:')],
        [sg.Text(f'{header[0]}: {lista_carac[0]}', key="CARAC 0")],
        [sg.Text(f'{header[1]}: {lista_carac[1]}', key="CARAC 1")],
        [sg.Text(f'{header[2]}: {lista_carac[2]}', key="CARAC 2")],
        [sg.Text(f'{header[3]}: {lista_carac[3]}', key="CARAC 3")],
        [sg.Text(f'{header[4]}: {lista_carac[4]}', key="CARAC 4")],
        [sg.Button(f'{lista_data[0][5]}', key='OPCION 0')],
        [sg.Button(f'{lista_data[1][5]}', key='OPCION 1')],
        [sg.Button(f'{lista_data[2][5]}', key='OPCION 2')],
        [sg.Button(f'{lista_data[3][5]}', key='OPCION 3')],
        [sg.Button(f'{lista_data[4][5]}', key='OPCION 4')],
        [sg.Button("Pasar"), sg.Text(' '*61),
        sg.Button('Abandonar el juego')],
        ]
    return layout, cant, datos, correcta, header
