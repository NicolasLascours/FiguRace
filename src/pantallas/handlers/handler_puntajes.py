

def handler_puntajes(event):
    """creo el manejador para los eventos que ocurran en la pantalla puntajes"""

    if event == 'Facil':
        # muestro puntajes de facil
        return print('puntajes facil')
    elif event == 'Medio':
        # muestro puntajes de medio
        return print('puntajes medio')
    elif event == 'Dificil':
        # muestro puntajes de dificil
        return print('puntajes dificil')
