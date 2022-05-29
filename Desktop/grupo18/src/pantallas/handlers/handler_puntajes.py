import PySimpleGUI as sg


def handler_puntajes(event):
    """creo el manejador para los eventos que ocurran en la pantalla puntajes"""

    if event == 'Facil':
        # invento puntajes solo para probar el funcionamiento
        puntajes_facil = [
            ["AAA", 1500],
            ['BBB', 1200],
            ['CCC', 900],
            ['DDD', 700]
        ]
        # nombro las columnas de la tabla
        columnas = ["nick", "puntos"]
        # armo el layout
        layout = [
            [sg.Table(values=puntajes_facil, headings=columnas, max_col_width=35,
                      auto_size_columns=True,
                      row_height=35)],
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
        # invento puntajes solo para probar el funcionamiento
        puntajes_medio = [
            ["AAA", 1500],
            ['BBB', 1200],
            ['CCC', 900],
            ['DDD', 700]
        ]
        # nombro las columnas de la tabla
        columnas = ["nick", "puntos"]
        # armo el layout
        layout = [
            [sg.Table(values=puntajes_medio, headings=columnas, max_col_width=35,
                      auto_size_columns=True,
                      row_height=35)],
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
        # invento puntajes solo para probar el funcionamiento
        puntajes_dificil = [
            ["AAA", 1500],
            ['BBB', 1200],
            ['CCC', 900],
            ['DDD', 700]
        ]
        # nombro las columnas de la tabla
        columnas = ["nick", "puntos"]
        # armo el layout
        layout = [
            [sg.Table(values=puntajes_dificil, headings=columnas, max_col_width=35,
                      auto_size_columns=True,
                      row_height=35)],
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
