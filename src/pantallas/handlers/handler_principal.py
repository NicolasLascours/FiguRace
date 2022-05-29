import json
import PySimpleGUI as sg
from src.pantallas.handlers.handler_juego import abrir_configuracion
from ..pantalla_configuracion import ventana_configuracion
from ..pantalla_juego import comenzar
from ..pantalla_puntajes import ventana_puntajes
from ..pantalla_perfiles import ventana_perfiles

def elegirperfil():
     """
     Funcion que genera una lista con los nick de 
     los jugadores para luego en la pantalla puedan
     ser elegidos
     """
     l = []
     with open ('perfiles.json', 'r') as archivo:
          datos = json.load(archivo)
          for linea in datos:
                l.append(linea['nick']) 
     return l  

def cargarConfig(dif):
     """
     Funcion que carga las configuraciones para
     cada dificultad
     """
     print(dif)
     with open ('config.json', 'r') as archivo:
           dicc = json.load(archivo)
     with open  ('config.json', 'w') as archivo: # configuraciones por defecto para cada dificultad
          if dif == 'Facil':
               dicc['Puntaje Sumado'] = '100'
               dicc['Puntaje Restado'] = '10'
               dicc['Caracteristicas'] = '5'
          if dif == 'Normal':
               dicc['Puntaje Sumado'] = '50'
               dicc['Puntaje Restado'] = '20'
               dicc['Caracteristicas'] = '3'
          if dif == 'Dificil':
               dicc['Puntaje Sumado'] = '10'
               dicc['Puntaje Restado'] = '50'
               dicc['Caracteristicas'] = '1'
          json.dump(dicc, archivo)
          sg.popup_ok('Se han actualizado las configuraciones para la dificultad ', dif)

def eventos(evento, ventana):
    """
    funcion que responde a los eventos que se 
    pueden originar en la llamada del modulo principal
    """
    if evento[0] == 'OK':
         cargarConfig(evento[1][1])
    if evento[0] == 'ok':
         with open ('perfil_actual.json', 'w') as archivo:
              json.dump(evento[1][0], archivo)
    if evento[0] == "Jugar":
         ventana.Hide()
         comenzar()
         ventana.UnHide()
    if evento[0] == "Configuracion":
         ventana.Hide()
         ventana_configuracion()
         ventana.UnHide()
    if evento[0] == "Puntajes":
         ventana.Hide()
         ventana_puntajes()
         ventana.UnHide()
    if evento[0] == "Perfiles":
         ventana.Hide()
         ventana_perfiles()
         ventana.UnHide()