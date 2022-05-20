# importo modulos a usar
from layouts import layout_puntajes
from handlers import handler_puntajes
import PySimpleGUI as sg

# creo ventana puntajes
sg.theme('LightBlue4')
window = sg.Window("Puntajes", layout_puntajes.layout_puntajes(), margins=(200, 150))

# creo el bucle
while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Volver":
        break
    else:
        # llamo al modulo handler pasandole el evento que se produjo
        handler_puntajes.handler_puntajes(event)
# cierro la ventana
window.close()
