import PySimpleGUI as sg
from ..handlers.handler_juego import abrir_configuracion
from ..handlers.handler_juego import abrir_volcanes
from ..handlers.handler_juego import abrir_fifa
from ..handlers.handler_juego import abrir_lagos
from ..handlers.handler_juego import convert


# layout de la pantalla del juego


def layouts():
    """
    funcion que define el diseño de la
    pantalla del juego
    """
    config = abrir_configuracion()
    header_volcan, data_volcan = abrir_volcanes()
    if config['Caracteristicas'] == "1":
        layout = [
            [sg.Text('Volcanes!!'), sg.Text(' '*74), sg.Text('Dificultad')],
            [sg.Text(' '*93), sg.Text(config['Dificultad'])],
            [sg.Text('')],
            [sg.Text('Caracteristicas'), sg.Text('Ronda actual: 1', key='-RONDAS-'),
             sg.Text('Cantidad de rondas {}'.format(config['Rondas'])),
             sg.Text('Tiempo: {}'.format(convert(int(config['Tiempo']))), key='-TIEMPO-')],
            [sg.Text(' '*45), sg.Text('Puntaje: 0')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text('Año:{}'.format(data_volcan[0][0]))],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Button('{}'.format(data_volcan[2][5]), key='-OPCION 1-')],
            [sg.Button('{}'.format(data_volcan[3][5]), key='-OPCION 2-')],
            [sg.Button('{}'.format(data_volcan[0][5]), key='-OPCION 3-')],
            [sg.Button('{}'.format(data_volcan[1][5]), key='-OPCION 4-')],
            [sg.Button('{}'.format(data_volcan[4][5]), key='-OPCION 5-')],
            [sg.Button("Pasar"), sg.Button('OK'), sg.Text(' '*61), # REVISAR QUE CAPAZ EL "OK" ESTÁ DE MÁS
             sg.Button('Abandonar el juego')],
        ]
    if config['Caracteristicas'] == "3":
        layout = [
            [sg.Text('Volcanes!!'), sg.Text(' '*74), sg.Text('Dificultad')],
            [sg.Text(' '*93), sg.Text(config['Dificultad'])],
            [sg.Text('')],
            [sg.Text('Caracteristicas'), sg.Text('Ronda actual: 1', key='-RONDAS-'),
             sg.Text('Cantidad de rondas {}'.format(config['Rondas'])),
             sg.Text(('Tiempo: {}'.format(convert(int(config['Tiempo'])))), key='-TIEMPO-')],
            [sg.Text(' '*45), sg.Text('Puntaje: 0')],
            [sg.Text('Año: {}'.format(data_volcan[0][0]))],
            [sg.Text('')],
            [sg.Text('Indice de explosividad volcanica: {}'.format(data_volcan[0][1]))],
            [sg.Text('')],
            [sg.Text('Tipo de volcan {}'.format(data_volcan[0][2]))],
            [sg.Text('')],
            [sg.Button('{}'.format(data_volcan[2][5]), key='-OPCION 1-')],
            [sg.Button('{}'.format(data_volcan[3][5]), key='-OPCION 2-')],
            [sg.Button('{}'.format(data_volcan[0][5]), key='-OPCION 3-')],
            [sg.Button('{}'.format(data_volcan[1][5]), key='-OPCION 4-')],
            [sg.Button('{}'.format(data_volcan[4][5]), key='-OPCION 5-')],
            [sg.Button("Pasar"), sg.Button('OK'), sg.Text(' '*61),
             sg.Button('Abandonar el juego')],
        ]
    if config['Caracteristicas'] == "5":
        layout = [
            [sg.Text('Volcanes!!'), sg.Text(' '*74), sg.Text('Dificultad')],
            [sg.Text(' '*93), sg.Text(config['Dificultad'])],
            [sg.Text('')],
            [sg.Text('Caracteristicas'), sg.Text('Ronda actual: 1', key='-RONDAS-'),
             sg.Text('Cantidad de rondas {}'.format(config['Rondas'])),
             sg.Text(('Tiempo: {}'.format(convert(int(config['Tiempo'])))), key='-TIEMPO-')],
            [sg.Text(' '*45), sg.Text('Puntaje: 0')],
            [sg.Text('Año: {}'.format(data_volcan[0][0]))],
            [sg.Text('Bandera terremoto: {}'.format(data_volcan[0][4]))],
            [sg.Text('Tipo de volcan: {}'.format(data_volcan[0][2]))],
            [sg.Text('Indice de explosividad volcanica: {}'.format(data_volcan[0][1]))],
            [sg.Text('Bandera Tsunami: {}'.format(data_volcan[0][3]))],
            [sg.Text('')],
            [sg.Button('{}'.format(data_volcan[2][5]), key='-OPCION 1-')],
            [sg.Button('{}'.format(data_volcan[3][5]), key='-OPCION 2-')],
            [sg.Button('{}'.format(data_volcan[0][5]), key='-OPCION 3-')],
            [sg.Button('{}'.format(data_volcan[1][5]), key='-OPCION 4-')],
            [sg.Button('{}'.format(data_volcan[4][5]), key='-OPCION 5-')],
            [sg.Button("Pasar"), sg.Button('OK'), sg.Text(' '*61),
             sg.Button('Abandonar el juego')],
        ]
    return layout
