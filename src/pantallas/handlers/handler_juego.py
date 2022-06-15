import json
from roots import ROOT_VOLCANS, ROOT_LAGOS, ROOT_FIFA, ROOT_CONFIG
import csv
import time

def abrir_volcanes():
    """
    Abre el datasets de volcanes y retorna el encabezado
    y una lista con las filas de archivo
    """
    with open(ROOT_VOLCANS, encoding='utf_8') as dataset:
        csvreader = csv.reader(dataset, delimiter=',')
        header, data = next(csvreader), list(csvreader)
    return header, data


def abrir_lagos():
    """
    Abre el datasets de lagos y retorna el encabezado
    y una lista con las filas de archivo
    """
    with open(ROOT_LAGOS, encoding='utf_8') as dataset:
        csvreader = csv.reader(dataset, delimiter=',')
        header, data = next(csvreader), list(csvreader)
    return header, data


def abrir_fifa():
    """
    Abre el datasets de fifa y retorna el encabezado
    y una lista con las filas de archivo
    """
    with open(ROOT_FIFA, encoding='utf_8') as dataset:
        csvreader = csv.reader(dataset, delimiter=',')
        header, data = next(csvreader), list(csvreader)
    return header, data


def abrir_configuracion():
    """
    Abre el archivo json de las configuraciones del juego y retorna los datos.
    En caso de no encontrar el archivo, lo crea en la direccion correcta y lo
    carga con una dificultad por defecto.
    """
    try:
        with open(ROOT_CONFIG, 'r') as archivo_json:
            datos = json.load(archivo_json)
            return datos
    except FileNotFoundError:
        dif_por_defecto = {"Tiempo": "60",
                           "Rondas": "4",
                           "Puntaje Sumado": "50",
                           "Puntaje Restado": "20",
                           "Caracteristicas": "3",
                           "Dificultad": "Normal"}
        # Si no encuentra el archivo en la ruta, lo crea con valores por defecto
        with open(ROOT_CONFIG, 'x') as archivo_json:
            json.dump(dif_por_defecto, archivo_json)
            return dif_por_defecto    


def convert(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


def actualizar_tiempo(ventana, partida):
    """ Funcion que actualiza el tiempo y en cazo de terminarse
    avanza a la siguiente ronda y reinicia el tiempo """
    transcurrido = int(time.time() - partida.tiempo_ronda_inicial)
    restante = partida.tiempo_por_ronda - transcurrido
    if restante <= 0:
        ventana['-TIEMPO-'].update(f'Tiempo: {convert(0)}')
        partida.incrementar_ronda()
        if partida.ronda_actual <= partida.cant_rondas:
            # NUEVA RONDA POR FIN DEL TIEMPO (HABRÍA QUE PONER LAS NUEVAS OPCIONES)
            ventana['-RONDAS-'].update(f'Ronda actual: {partida.ronda_actual}')
            ventana['-TIEMPO-'].update(f'Tiempo: {convert(partida.tiempo_por_ronda)}')
            partida.tiempo_ronda_inicial = time.time()
    else:
        ventana['-TIEMPO-'].update(f'Tiempo: {convert(restante)}')


def eventos(evento, ventana, partida):
    """
    Funcion que controla la logica y
    eventos que ocurren en el juego
    """
    if evento == 'Pasar':
        partida.incrementar_ronda()
        if partida.ronda_actual <= partida.cant_rondas:
            # NUEVA RONDA POR PASAR (HABRÍA QUE PONER LAS NUEVAS OPCIONES)
            ventana['-RONDAS-'].update(f'Ronda actual: {partida.ronda_actual}')
            ventana['-TIEMPO-'].update(f'Tiempo: {convert(partida.tiempo_por_ronda)}')
            partida.tiempo_ronda_inicial = time.time()
    elif (evento == '-OPCION 1-' or evento == '-OPCION 2-' or evento == '-OPCION 3-' 
            or evento == '-OPCION 4-' or evento == '-OPCION 5-'): 
        print(f'SELECCIONÓ {evento}') # ACA SE VERIFICARÍA LA OPCION SELECCIONADA