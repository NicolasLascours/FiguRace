import json
import PySimpleGUI as sg
from roots import ROOT_REGISTRO, ROOT_VOLCANS, ROOT_LAGOS, ROOT_FIFA, ROOT_CONFIG, ROOT_PERFILES
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
                           "Facil": "5",
                           "Normal": "3",
                           "Dificil": "2",
                           "Dificultad": "Normal"}
        # Si no encuentra el archivo en la ruta, lo crea con valores por defecto
        with open(ROOT_CONFIG, 'x') as archivo_json:
            json.dump(dif_por_defecto, archivo_json)
            return dif_por_defecto    


 ##["Timestamp", "ID", "Objectos a adivinar", "genero" ,"Evento", "Usuario", "Estado", "Texto Ingresado", "Respuesta", "Nivel"]
def registro_jugadas(evento, perfil_actual, correcta, lista_data, respuesta, partida):
    """
    Funcion que actualiza los eventos que ocurren en
    el juego y los guarda en un archico csv
    """
    config = abrir_configuracion()
    with open(ROOT_PERFILES, 'r') as reg:
        perfiles = json.load(reg)
        i = 0
        while i < len(perfiles) and (perfiles[i]['nick'] != perfil_actual):
            i += 1
        gen = perfiles[i]['genero']
    with open(ROOT_REGISTRO, 'a', encoding='utf_8') as reg:
        writer = csv.writer(reg)
        if evento == '__TIMEOUT__':
            writer.writerow([time.time(), partida.uuid, partida.cant_rondas, gen, 'Intento', perfil_actual, "timeout", "", correcta[5], config["Dificultad"]])
        elif evento == "Correcta":
            writer.writerow([time.time(), partida.uuid, partida.cant_rondas, gen, 'Intento', perfil_actual, "ok", lista_data[respuesta][5], correcta[5], config["Dificultad"]])
        elif evento == "Pasar":
            writer.writerow([time.time(), partida.uuid, partida.cant_rondas, gen, 'Intento', perfil_actual, "Omision", '', correcta[5], config["Dificultad"]])
        elif evento == "Incorrecta":
            writer.writerow([time.time(), partida.uuid, partida.cant_rondas, gen, 'Intento', perfil_actual, "error", lista_data[respuesta][5], correcta[5], config["Dificultad"]])
        elif evento == "Abandonar el juego" or evento == sg.WIN_CLOSED:
            writer.writerow([time.time(), partida.uuid, partida.cant_rondas, gen, 'fin', perfil_actual, "cancelada", '', '', config["Dificultad"]])
        else:
            writer.writerow([time.time(), partida.uuid, partida.cant_rondas, gen, 'fin', perfil_actual, "finalizada", '', '', config["Dificultad"]])


def inicializacion_partida(perfil_actual, dif, uui):
    config = abrir_configuracion()
    with open(ROOT_PERFILES, 'r') as reg:
        perfiles = json.load(reg)
        i = 0
        while i < len(perfiles) and (perfiles[i]['nick'] != perfil_actual):
            i += 1
        gen = perfiles[i]['genero']
    with open(ROOT_REGISTRO, 'a') as reg:
        writer = csv.writer(reg)
        writer.writerow([time.time(), uui, config["Rondas"], gen, "inicio_partida", perfil_actual, '', '', '', dif])


def convert(seconds):
    """
    Funcion que convierte el tiempo ingresado 
    en minutos y seg
    """
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
    return restante


def actualizar_partida(ventana, partida):
    partida.incrementar_ronda()
    if partida.ronda_actual <= partida.cant_rondas:
        ventana['-RONDAS-'].update(f'Ronda actual: {partida.ronda_actual}')
        ventana['-TIEMPO-'].update(f'Tiempo: {convert(partida.tiempo_por_ronda)}')
        partida.tiempo_ronda_inicial = time.time()


def actualizacion(ventana, lista_data, cant, header, lista_carac):
    for i in range(5):
        ventana["OPCION "+str(i)].update(f'{lista_data[i][5]}')
    for i in range(int(cant)):
        ventana["CARAC "+str(i)].update(f"{header[i]}: {lista_carac[i]}")


def eventos(evento, ventana, partida, correcta, lista_data, perfil_actual):
    """
    Funcion que controla la logica y
    eventos que ocurren en el juego
    """
    if evento == 'Pasar':
        if partida.ronda_actual <= partida.cant_rondas:
            actualizar_partida(ventana, partida)
            ventana["-Puntaje-"].update(f'Puntaje: {partida.puntaje()}')
            registro_jugadas(evento, perfil_actual, correcta, lista_data, '', partida)
    elif (evento == 'OPCION 0' or evento == 'OPCION 1' or evento == 'OPCION 2' 
            or evento == 'OPCION 3' or evento == 'OPCION 4'): 
            respuesta = int(evento[-1])
            if lista_data[respuesta][5] == correcta[5]:
                partida.incrementar_puntaje()
                registro_jugadas("Correcta", perfil_actual, correcta, lista_data, respuesta, partida)
            else:
                partida.decrementar_puntaje()
                registro_jugadas("Incorrecta", perfil_actual, correcta, lista_data, respuesta, partida)
            ventana['-Puntaje-'].update(f'Puntaje: {partida.puntaje()}')
            actualizar_partida(ventana, partida)
