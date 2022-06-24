import time
from src.pantallas.handlers.handler_juego import abrir_configuracion
import uuid

class Partida:

    def __init__(self):
        self._configuracion = abrir_configuracion()
        self._tiempo_partida_inicial = time.time()
        self._tiempo_ronda_inicial = time.time()
        self._ronda_actual = 1
        self._uuid = uuid.uuid4()
        self._puntaje = 0
    
    @property
    def cant_rondas(self):
        return int(self._configuracion['Rondas'])

    @property
    def tiempo_por_ronda(self):
        return int(self._configuracion['Tiempo'])

    @property
    def tiempo_partida_inicial(self):
        return self._tiempo_partida_inicial

    @property
    def tiempo_ronda_inicial(self):
        return self._tiempo_ronda_inicial 
    
    @tiempo_ronda_inicial.setter
    def tiempo_ronda_inicial(self,value):
        self._tiempo_ronda_inicial = value
    
    @property
    def ronda_actual(self):
        return self._ronda_actual

    @property
    def uuid(self):
        return self._uuid

    def puntaje(self):
        return self._puntaje

    def incrementar_ronda(self):
        self._ronda_actual += 1

    def incrementar_puntaje(self):
        self._puntaje += int(self._configuracion['Puntaje Sumado'])

    def decrementar_puntaje(self):
        self._puntaje -= int(self._configuracion['Puntaje Restado'])