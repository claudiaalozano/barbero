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
