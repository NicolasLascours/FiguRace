# modulo para generar la ventana principal
#import configuracion_pantalla # tratar de arreglar esto
import PySimpleGUI as sg
# color seleccionado para la ventana 

sg.theme("LightGreen10")
LayOut = [
         [sg.Button("Configuracion", size=(10, 2)), sg.Text('                                               '), sg.Text('Ingrese un perfil para jugar')],
         [sg.Text('                                                                                         ')],# esto deberia sacar la lista con los usuarios, me falta la lista de usuarios y como mostrarlos
         [sg.Column([[sg.Text("FIGURACE")]],justification='center')],
         [sg.Column([[sg.Button("Jugar", size=(5, 2))]], justification='center')],
         [sg.Text('')],
         [sg.Text('')],
         [sg.Text('')],
         [sg.Button("Perfiles", size=(10, 2)), sg.Text('                   '), sg.Button("Salir", size=(10, 2)), sg.Text('                    '), sg.Button("Puntajes", size=(10, 2))]
         ] 
# lista con acciones para hacer en pantalla, por ahora solo los bottones
ventana = sg.Window('FiguRace', LayOut, size=(500,300))
# creacion de ventana
while True:
     evento = ventana.read()
     if evento[0] == "Jugar" and evento[1] == None:
        sg.popup_error()
     if evento[0] == "Configuracion":
         pass
     if evento[0] == "Puntajes":
         pass
     if evento[0] == "Perfiles":
         pass
     if evento[0] == "Salir" or evento[0] == sg.WIN_CLOSED:
         break
# mini prueba de la ventana
ventana.close()