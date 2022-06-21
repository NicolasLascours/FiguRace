import PySimpleGUI as sg
import pandas as pd
from roots import ROOT_PUNTAJES


def handler_puntajes(event):
    """creo el manejador para los eventos que ocurran en la pantalla puntajes"""

    # cargo el csv de puntajes
    puntajes = pd.read_csv(ROOT_PUNTAJES, encoding='utf-8')
    # me quedo primero solo con los estado 'Finalizada'
    puntajes = puntajes[puntajes.Estado == 'Finalizada']

    if event == 'Facil':
        # me quedo con los que sean nivel 'Facil'
        puntajes_facil = puntajes[puntajes.Dificultad == 'Facil']

        # encabezados para la tabla 'mejores puntajes' del layout
        encabezados_max = ['Nick', 'Genero', 'Estado', 'Puntuacion', 'Dificultad']

        # encabezados para la tabla 'mejores puntajes promedio' del layout
        encabezados_promedio = ['Nick', 'Puntuacion Promedio']

        # valores de la tabla 'mejores puntajes' del layout
        puntajes_facil_max = puntajes_facil.sort_values(ascending=False, by=['Puntuacion'], ignore_index=True).head(20)
        valores = puntajes_facil_max.values.tolist()

        # calculo valores para la tabla de 'mejores puntajes promedio' del layout

        # nicks sin repetir
        nicks = list(puntajes_facil.groupby('Nick')['Nick'].unique())
        # cantidad de partidas por jugador
        cantidad_partidas = puntajes_facil.groupby('Nick').size()
        # puntos totales por jugador
        puntos_totales = puntajes_facil.groupby('Nick')['Puntuacion'].sum()
        # promedio de cada jugador
        promedio = list((puntos_totales / cantidad_partidas).round(2))
        # datos para el dataframe a mostrar en la tabla
        datos = {
            'Nick': [x for x in nicks],
            'Puntuacion': [x for x in promedio]
        }
        # armo el dataframe
        puntajes_promedio = pd.DataFrame(data=datos)
        puntajes_promedio = puntajes_promedio.sort_values(ascending=False, by=['Puntuacion'], ignore_index=True).head(
            20)

        # valores para la tabla de promedios en el layout
        valores_promedio = puntajes_promedio.values.tolist()
        # armo el layout
        layout = [
            [sg.Text('Mejores Puntajes Facil')],
            [sg.Table(values=valores, headings=encabezados_max,
                      auto_size_columns=False, col_widths=list(map(lambda x: len(x) + 2, encabezados_max)))],
            [sg.Text('Mejores Puntajes Promedio Facil')],
            [sg.Table(values=valores_promedio, headings=encabezados_promedio,
                      auto_size_columns=False, col_widths=list(map(lambda x: len(x) + 2, encabezados_promedio)))],
            [sg.Button("Volver")]
        ]
        # creo la ventana
        window = sg.Window("Puntajes Facil", layout)
        # creo el bucle
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == "Volver":
                window.close()
                break
    elif event == 'Medio':
        # me quedo con los que sean nivel 'Normal'
        puntajes_normal = puntajes[puntajes.Dificultad == 'Normal']

        # encabezados para la tabla 'mejores puntajes' del layout
        encabezados_max = ['Nick', 'Genero', 'Estado', 'Puntuacion', 'Dificultad']

        # encabezados para la tabla 'mejores puntajes promedio' del layout
        encabezados_promedio = ['Nick', 'Puntuacion Promedio']

        # valores de la tabla 'mejores puntajes' del layout
        puntajes_normal_max = puntajes_normal.sort_values(ascending=False, by=['Puntuacion'], ignore_index=True).head(
            20)
        valores = puntajes_normal_max.values.tolist()

        # calculo valores para la tabla de 'mejores puntajes promedio' del layout
        # nicks sin repetir
        nicks = list(puntajes_normal.groupby('Nick')['Nick'].unique())
        # cantidad de partidas por jugador
        cantidad_partidas = puntajes_normal.groupby('Nick').size()
        # puntos totales por jugador
        puntos_totales = puntajes_normal.groupby('Nick')['Puntuacion'].sum()
        # promedio de cada jugador
        promedio = list((puntos_totales / cantidad_partidas).round(2))

        # datos para el dataframe a mostrar en la tabla
        datos = {
            'Nick': [x for x in nicks],
            'Puntuacion': [x for x in promedio]
        }
        # armo el dataframe
        puntajes_promedio = pd.DataFrame(data=datos)
        puntajes_promedio = puntajes_promedio.sort_values(ascending=False, by=['Puntuacion'], ignore_index=True).head(
            20)

        # valores para la tabla de promedios en el layout
        valores_promedio = puntajes_promedio.values.tolist()
        # armo el layout
        layout = [
            [sg.Text('Mejores Puntajes Normal')],
            [sg.Table(values=valores, headings=encabezados_max,
                      auto_size_columns=False, col_widths=list(map(lambda x: len(x) + 2, encabezados_max)))],
            [sg.Text('Mejores Puntajes Promedio Normal')],
            [sg.Table(values=valores_promedio, headings=encabezados_promedio,
                      auto_size_columns=False, col_widths=list(map(lambda x: len(x) + 2, encabezados_promedio)))],
            [sg.Button("Volver")]
        ]
        # creo la ventana
        window = sg.Window("Puntajes Medio", layout)
        # creo el bucle
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == "Volver":
                window.close()
                break
    elif event == 'Dificil':
        # me quedo con los que sean nivel 'Dificil'
        puntajes_dificil = puntajes[puntajes.Dificultad == 'Dificil']

        # encabezados para la tabla 'mejores puntajes' del layout
        encabezados_max = ['Nick', 'Genero', 'Estado', 'Puntuacion', 'Dificultad']

        # encabezados para la tabla 'mejores puntajes promedio' del layout
        encabezados_promedio = ['Nick', 'Puntuacion Promedio']

        # valores de la tabla 'mejores puntajes' del layout
        puntajes_dificil_max = puntajes_dificil.sort_values(ascending=False, by=['Puntuacion'], ignore_index=True).head(
            20)
        valores = puntajes_dificil_max.values.tolist()

        # calculo valores para la tabla de 'mejores puntajes promedio' del layout
        # nicks sin repetir
        nicks = list(puntajes_dificil.groupby('Nick')['Nick'].unique())
        # cantidad de partidas por jugador
        cantidad_partidas = puntajes_dificil.groupby('Nick').size()
        # puntos totales por jugador
        puntos_totales = puntajes_dificil.groupby('Nick')['Puntuacion'].sum()
        # promedio de cada jugador
        promedio = list((puntos_totales / cantidad_partidas).round(2))

        # datos para el dataframe a mostrar en la tabla
        datos = {
            'Nick': [x for x in nicks],
            'Puntuacion': [x for x in promedio]
        }
        # armo el dataframe
        puntajes_promedio = pd.DataFrame(data=datos)
        puntajes_promedio = puntajes_promedio.sort_values(ascending=False, by=['Puntuacion'], ignore_index=True).head(
            20)

        # valores para la tabla de promedios en el layout
        valores_promedio = puntajes_promedio.values.tolist()
        # armo el layout
        layout = [
            [sg.Text('Mejores Puntajes Dificil')],
            [sg.Table(values=valores, headings=encabezados_max,
                      auto_size_columns=False, col_widths=list(map(lambda x: len(x) + 2, encabezados_max)))],
            [sg.Text('Mejores Puntajes Promedio Dificil')],
            [sg.Table(values=valores_promedio, headings=encabezados_promedio,
                      auto_size_columns=False, col_widths=list(map(lambda x: len(x) + 2, encabezados_promedio)))],
            [sg.Button("Volver")]
        ]
        # creo la ventana
        window = sg.Window("Puntajes Dificil", layout)
        # creo el bucle
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == "Volver":
                window.close()
                break
