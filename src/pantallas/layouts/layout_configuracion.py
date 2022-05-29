import PySimpleGUI as sg
# layout del programa


def layout():
    """funcion que tiene el diseño de 
    la pantalla de configuraciones 
    """
    # layout de la pantalla de configuracion 
    layout = [
           [sg.Text('Tiempo limite por ronda')],
           [sg.Combo(['30', '60', '90', '120'], key="Tiempo")], 
           [sg.Text('Cantidad de rondas')],
           [sg.Combo(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], key='Rondas')], 
           [sg.Text('Puntaje a sumar por respuesta correcta')],
           [sg.Combo(['10', '30', '50', '60', '80', '100'], key='Puntaje Sumado')],
           [sg.Text('Puntaje a restar por respuesta incorrecta')],
           [sg.Combo(['10', '30', '50', '60', '80', '100'], key='Puntaje Restado')],
           [sg.Text('Cantidad de caracteristicas a mostrar en pantalla')],
           [sg.Combo(['1', '3', '5'], key='Caracteristicas')],  # verificar datos del dataset, o sea si son 5 columnas
                                                                # en el data set se puede hacer hasta 5
           [sg.Submit(), sg.Text('    '), sg.Button('Volver')]
           ]
    return layout
