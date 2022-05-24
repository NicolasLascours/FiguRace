from ..pantalla_configuracion import ventana_configuracion
from ..pantalla_juego import comenzar
from ..pantalla_puntajes import ventana_puntajes
from ..pantalla_perfiles import ventana_perfiles

def eventos(evento, ventana):
    """
    funcion que responde a los eventos que se 
    pueden originar en la llamada del modulo principal
    """
    if evento[0] == 'OK':
        with open ('dificultad.json', 'w') as archivo_config:
            json.dump(evento[0], archivo_config)
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