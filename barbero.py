import threading
from time import sleep
from random import randint
from collections import deque

#creo la clase barbero
class Barbero():
    clientes = deque()
    estado ="Durmiendo"

numero_clientes = 0
mutex = threading.Semaphore()

#función cortar pelo
def cortar_pelo():
    global numero_clientes
    while True:
        if len(Barbero.clientes) == 0:
            print("El barbero está durmiendo")
            if numero_clientes >= 15:
                break