import PySimpleGUI as sg
# layout del programa


def layout():
    """funcion que tiene el diseño de
    la pantalla de configuraciones
    """
    # layout de la pantalla de configuracion
    layout = [
           [sg.Text('Tiempo limite por ronda')],
           [sg.Combo(['30', '60', '90', '120'], key="Tiempo", readonly=True)],
           [sg.Text('Cantidad de rondas')],
           [sg.Combo(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            key='Rondas', readonly=True)],
           [sg.Text('Puntaje a sumar por respuesta correcta')],
           [sg.Combo(['10', '30', '50', '60', '80', '100'],
            key='Puntaje Sumado', readonly=True)],
           [sg.Text('Puntaje a restar por respuesta incorrecta')],
           [sg.Combo(['10', '30', '50', '60', '80', '100'],
            key='Puntaje Restado', readonly=True)],
           [sg.Text('Cantidad de caracteristicas facil')],
           [sg.Combo(['1', '2', '3', '4', '5'], key="Facil", readonly=True)],
           [sg.Text('Cantidad de caracteristicas normal')],
           [sg.Combo(['1', '2', '3', '4', '5'], key="Normal", readonly=True)],
           [sg.Text('Cantidad de caracteristicas dificil')],
           [sg.Combo(['1', '2', '3', '4', '5'], key="Dificil", readonly=True)],
           [sg.Submit(), sg.Text('    '), sg.Button('Volver')]
           ]
    return layout
