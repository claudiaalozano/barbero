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
        else:
            for i in list(Barbero.clientes):
                mutex.acquire()
                Barbero.estado = "Cortando pelo"
                print("El barbero está cortando el pelo al cliente", i)
                sleep(2)
                print("Terminó de cortar el pelo al cliente", i)
                Barbero.clientes.popleft()
                mutex.release()
                sleep(0.1)
            Barbero.estado = "Durmiendo"

#función añadir cliente
def añadir_cliente():
    global numero_clientes
    while numero_clientes<= 15:
        sleep(0.5)
        a = randint(1, 10)
        if a <= 6:
            if Barbero.estado == "Durmiendo":
                
                Barbero.clientes.append(numero_clientes)
                print("El cliente", numero_clientes, "despierta al barbero")
                sleep(0.4)

            else:
                if len(Barbero.clientes) >= 7:
                    print("Cola mayor a 7 personas, esperando a que uno acabe")
                    print("Cola clientes:" + str(len(Barbero.clientes)) + "/" + str(7))
                    mutex.acquire()
                    Barbero.clientes.append(numero_clientes)
                    print("Cliente añadido a la cola.")
                    numero_clientes += 1
                    mutex.release()
                    sleep(0.4)
                else:
                    numero_clientes += 1
                    print(f"Cliente número {numero_clientes} que visita la tienda.")
                    Barbero.clientes.append(numero_clientes)
                    print("Cliente añadido a la cola.")
                    print("Cola clientes:" + str(len(Barbero.clientes)) + "/" + str(7))
                    sleep(0.4)
        
        