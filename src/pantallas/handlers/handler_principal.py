import json
import PySimpleGUI as sg
from ..pantalla_configuracion import ventana_configuracion
from ..pantalla_juego import comenzar
from ..pantalla_puntajes import ventana_puntajes
from ..pantalla_perfiles import ventana_perfiles
from src.pantallas.handlers.handler_juego import abrir_configuracion, abrir_perfil_actual


def elegir_perfil():
     """
     Funcion que genera una lista con los nick de 
     los jugadores para luego en la pantalla puedan
     ser elegidos
     """
     l = []
     with open('perfiles.json', 'r') as archivo:
          datos = json.load(archivo)
          for linea in datos:
                l.append(linea['nick']) 
     return l  

def cargar_config(dif):
     """
     Funcion que carga las configuraciones para
     cada dificultad
     """
     with open('config.json', 'r') as archivo:
          dicc = json.load(archivo)
     with open('config.json', 'w') as archivo: # configuraciones por defecto para cada dificultad
          if dif == 'Facil':
               dicc['Puntaje Sumado'] = '100'
               dicc['Puntaje Restado'] = '10'
               dicc['Caracteristicas'] = '5'
               dicc['Dificultad'] = "Facil"
          if dif == 'Normal':
               dicc['Puntaje Sumado'] = '50'
               dicc['Puntaje Restado'] = '20'
               dicc['Caracteristicas'] = '3'
               dicc['Dificultad'] = "Normal"
          if dif == 'Dificil':
               dicc['Puntaje Sumado'] = '10'
               dicc['Puntaje Restado'] = '50'
               dicc['Caracteristicas'] = '1'
               dicc['Dificultad'] = "Dificil"
          json.dump(dicc, archivo)
          sg.popup_ok('Se han actualizado las configuraciones para la dificultad ', dif)

def eventos(evento, ventana):
    """
    funcion que responde a los eventos que se 
    pueden originar en la llamada del modulo principal
    """
    if evento[0] == '-OK DIFI-':
         cargar_config(evento[1]['-COMBO DIFICULTAD-'])
    if evento[0] == '-OK PERF-':     
         with open('perfil_actual.json', 'w') as archivo:
              perf = {}
              perf['nick'] = evento[1]['-COMBO PERFILES-']
              json.dump(perf, archivo)
    if evento[0] == "Jugar":
         ventana.Hide()
         comenzar()
         ventana.UnHide()
    if evento[0] == "Configuracion":
         ventana.Hide()
         ventana_configuracion()
         config = abrir_configuracion()
         ventana['-COMBO DIFICULTAD-'].update(value=config['Dificultad'])
         ventana.UnHide()
    if evento[0] == "Puntajes":
         ventana.Hide()
         ventana_puntajes()
         ventana.UnHide()
    if evento[0] == "Perfiles":
         ventana.Hide()
         ventana_perfiles()
         perfil = abrir_perfil_actual()
         ventana['-COMBO PERFILES-'].update(
              value=perfil['nick'], values=elegir_perfil())
         ventana.UnHide()