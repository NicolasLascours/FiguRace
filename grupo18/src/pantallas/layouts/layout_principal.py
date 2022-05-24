import PySimpleGUI as sg
# color seleccionado para la ventana
def layouts_prin():
    """
    fucnion que define el diseño de la ventana 
    de la pantalla principal
    """
    # color seleccionado para la ventana 
    sg.theme("LightGreen10")
    # diseño
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
    return LayOut