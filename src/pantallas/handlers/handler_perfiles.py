# importo modulos
import json
import PySimpleGUI as sg
from roots import ROOT_PERFILES

def handler_perfiles(event):
    """creo el manejador para los eventos que ocurran en la pantalla perfiles"""

    if event == 'Crear nuevo perfil':
        # creo el layout
        layout = [
            [sg.Text('Ingresá nick'), sg.InputText()],
            [sg.Text('Ingresá edad'), sg.InputText()],
            [sg.Text('Ingresá genero'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]
        # creo la ventana
        sg.theme('LightBlue4')
        window = sg.Window("Crear Perfil", layout, margins=(200, 150))
        # bucle
        while True:
            event, values = window.read()

            if event == "Cancel" or event == sg.WIN_CLOSED:
                break
            # me guardo los datos ingresados
            dato = {"nick": values[0], "edad": values[1], "genero": values[2]}
            # abro el json y me quedo con los datos
            with open(ROOT_PERFILES, 'r') as archivo:
                datos = json.load(archivo)
            # verifico si el nick existe en los datos del json
            encontre = False
            i = 0
            while i < len(datos) and not encontre:
                if datos[i]["nick"] == dato["nick"]:
                    encontre = True
                    break
                i += 1
            # si existe el nick, aviso que se vuelva a ingresar otro
            if encontre:
                sg.popup_ok("El nick ya existe ingrese otro")
            # si un campo se dejo vacio, aviso que debe completarse
            elif values[0] == "" or values[1] == "" or values[2] == "":
                sg.popup_ok("Debe completar todos los campos")
            # si el nick no existe entonces creo el nuevo perfil
            else:
                # agrego los datos nuevos
                datos.append(dato)
                # abro el json y lo reescribo con la informacion nueva
                with open(ROOT_PERFILES, 'w') as archivo:
                    json.dump(datos, archivo)
                sg.popup_ok("El perfil se creo con exito")
                break
        # cierro ventana
        window.close()

    elif event == 'Editar uno existente':
        # abro json para tomar los datos y crear una lista de nicks
        with open(ROOT_PERFILES, 'r') as archivo:
            datos = json.load(archivo)
        # creo la lista con los nick existentes
        lista_nicks = list(map(lambda nicks: nicks['nick'], datos))
        # creo el layout
        layout = [
            [sg.Text('Elegi nick de perfil a cambiar'), sg.Combo(lista_nicks)],
            [sg.Text('Ingresá edad'), sg.InputText()],
            [sg.Text('Ingresá genero'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]
        # creo la ventana
        sg.theme('LightBlue4')
        window = sg.Window("Editar Perfil", layout, margins=(200, 150))
        # bucle
        while True:
            event, values = window.read()

            if event == "Cancel" or event == sg.WIN_CLOSED:
                break
            # guardo los datos ingresados
            nombre = values[0]
            edad = values[1]
            genero = values[2]
            # si un campo se dejo vacio, aviso que debe completarse
            if nombre == "" or edad == "" or genero == "":
                sg.popup_ok("Debe completar todos los campos")
            else:
                # abro el json y me quedo con los datos
                with open(ROOT_PERFILES, 'r') as archivo:
                    datos = json.load(archivo)
                # busco el nick en los datos del json
                encontre = False
                i = 0
                while i < len(datos) and not encontre:
                    if datos[i]["nick"] == nombre:
                        encontre = True
                        break
                    i += 1
                # cuando lo encuentro modifico los datos viejos con los nuevos
                if encontre:
                    datos[i]["edad"] = edad
                    datos[i]["genero"] = genero
                    # guardo los datos nuevos en el json
                    with open(ROOT_PERFILES, 'w') as archivo:
                        json.dump(datos, archivo)
                sg.popup_ok("El perfil se modifico con exito")
                break
        # cierro la ventana
        window.close()
