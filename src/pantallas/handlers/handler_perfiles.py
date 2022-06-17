# importo modulos
import json
import PySimpleGUI as sg
from roots import ROOT_PERFILES


def obtener_datos_nick(nick, datos):
    """devuelve la edad y el genero del nick recibido"""
    i = 0
    while i < len(datos):
        if datos[i]["nick"] == nick:
            break
        i += 1
    return datos[i]["edad"], datos[i]["genero"]


def datos_de_perfiles():
    """abre el archivo de perfiles y devuelve los datos que contenga"""
    with open(ROOT_PERFILES, 'r') as archivo:
        datos = json.load(archivo)
    return datos


def handler_perfiles(event):
    """creo el manejador para los eventos que ocurran en la pantalla perfiles"""
    # guardo los datos del json en datos
    datos = datos_de_perfiles()
    # rango de edades que uso para el layout
    edades = list(range(1, 111))

    if event == 'Crear nuevo perfil':
        # creo el layout
        layout = [
            [sg.Text('Ingresá nick'), sg.InputText()],
            [sg.Text('Ingresá edad'), sg.Combo(edades, readonly=True)],
            [sg.Text('Ingresá genero'), sg.Combo(['Masculino', 'Femenino', 'Otro'], readonly=True)],
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
        # creo la lista con los nick existentes
        lista_nicks = list(map(lambda nicks: nicks['nick'], datos))
        # creo el layout
        layout = [
            [sg.Text('Elegi nick de perfil a cambiar'), sg.Combo(lista_nicks, readonly=True, enable_events=True)],
            [sg.Text('Ingresá edad'), sg.Combo(edades, readonly=True, key='EDAD')],
            [sg.Text('Ingresá genero'), sg.Combo(['Masculino', 'Femenino', 'Otro'], readonly=True, key='GENERO')],
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

            if event == 'Ok':
                # si un campo se dejo vacio, aviso que debe completarse
                if values[0] == "" or values['EDAD'] == "" or values['GENERO'] == "":
                    sg.popup_ok("Debe completar todos los campos")
                else:
                    # guardo los datos ingresados
                    nombre = values[0]
                    edad = values['EDAD']
                    genero = values['GENERO']
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
            if values[0] != "":
                datos_nick = obtener_datos_nick(values[0], datos)
                window['EDAD'].update(value=datos_nick[0])
                window['GENERO'].update(value=datos_nick[1])
        # cierro la ventana
        window.close()
