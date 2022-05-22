#zona de imports
import PySimpleGUI as sg
from .layouts.layout_configuracion import layout
from .handlers.handler_configuracion import evento_config
import json

def verificar_json(values): # cambiar por if's
    """ 
    este modulo verifica si se ingresaron todas las
    configuraciones requeridas
    """
    b = True 
    if values['Tiempo'] == '30' or values['Tiempo'] == '60' or values['Tiempo'] == '90' or values['Tiempo'] == '120':
        pass
    else:
        sg.PopupError('Se ha ingresado un valor para el tiempo que esta incorrecto')
        b = False
    if values['Rondas'] == '1' or values['Rondas'] == '2' or values['Rondas'] == '3' or values['Rondas'] == '4' or values['Rondas'] == '5' or values['Rondas'] == '6' or values['Rondas'] == '7' or values['Rondas'] == '8' or values['Rondas'] == '9' or values['Rondas'] == '10':
        pass
    else:
        sg.PopupError('Se ha ingresado un valor para las rondas que esta incorrecto')
        b = False
    if values['Puntaje Sumado'] == '10' or values['Puntaje Sumado'] == '30' or values['Puntaje Sumado'] == '50' or values['Puntaje Sumado'] == '60' or values['Puntaje Sumado'] == '80' or values['Puntaje Sumado'] == '100':
        pass
    else:
        sg.PopupError('Se ha ingresado un valor para el valor de puntaje correcto el cual esta incorrecto')
        b = False
    if values['Puntaje Restado'] == '10' or values['Puntaje Restado'] == '30' or values['Puntaje Restado'] == '50' or values['Puntaje Restado'] == '60' or values['Puntaje Restado'] == '80' or values['Puntaje Restado'] == '100':
        pass
    else:
        sg.PopupError('Se ha ingresado un valor para los puntajes restados de los cual esta incorrecto')
        b = False
    if values['Caracteristicas'] == '1' or values['Caracteristicas'] == '3' or values['Caracteristicas'] == '5':
        pass
    else:
        sg.PopupError('Se ha ingresado un valor para las caracticas el cual esta incorrecto')
        b = False
    return b 

def ventana_configuracion(): # arreglar el false y el for 
    """
    funcion que ejecuta la ventana con su 
    diseño propio, con todas las funcionalidades 
    requeridas para la configuracion del juego
    """
    sg.theme('LightBlue4')
    # variable ventana con las caracteristicas de la misma
    lista = layout()
    ventana = sg.Window('Configuracion', lista, size=(350, 300)) # ventana variable que tiene los layout y el tamaño de pantalla
    # ejecucion del while
    while True:
      ventana.refresh()
      evento, values = ventana.read()
      if evento == sg.WIN_CLOSED or evento == 'Volver': # cuando se pueda hacer que cuando aprete volver vuelva a la pantalla inicial del juego
          break
      b = verificar_json(values)
      evento_config(b, evento, values)
    ventana.close()

# puede pasar que el usuario no ingrese una configuracion, por lo tanto, hay que ver si se puede dar que se le de una configuracion por defecto o se le obligue a insertar una 
# insertar los datos dentro de un archivo json, mucho cuidado aca porque puede que no o que si exista ya un archivo json