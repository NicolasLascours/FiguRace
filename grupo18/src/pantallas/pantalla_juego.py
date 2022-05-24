import PySimpleGUI as sg
    
# aca va para poder abrir el archivo de los dataset para el juego
def archivo_dataset():
    pass

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