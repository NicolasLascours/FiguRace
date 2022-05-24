import PySimpleGUI as sg
import json
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
           [sg.Combo(['1', '3', '5'], key='Caracteristicas')], # verificar datos del dataset, o sea si son 5 columnas en el data set se puede hacer hasta 5 
           [sg.Submit(), sg.Text('    '), sg.Button('Volver')]
           ]

def ventana_configuracion():
    sg.theme('LightBlue4')
    # variable ventana con las caracteristicas de la misma
    ventana = sg.Window('Configuracion', layout(), size=(350, 300)) # ventana variable que tiene los layout y el tamaño de pantalla
    # ejecucion del while
    while True:
      ventana.refresh()
      evento, values = ventana.read()
      if (evento == 'Submit'):
         with open ('config.json', 'w') as archivo_json:
             json.dump(values, archivo_json)
         sg.popup_ok('Las configuraciones han sido guardadas con exito')
      if evento == sg.WIN_CLOSED or evento == 'Volver': # cuando se pueda hacer que cuando aprete volver vuelva a la pantalla inicial del juego
          break
    ventana.close()

ventana_configuracion()

# puede pasar que el usuario no ingrese una configuracion, por lo tanto, hay que ver si se puede dar que se le de una configuracion por defecto o se le obligue a insertar una 
# insertar los datos dentro de un archivo json, mucho cuidado aca porque puede que no o que si exista ya un archivo json