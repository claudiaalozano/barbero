from barbero import *
if __name__ == '__main__':
    barbero= threading.Thread(target=cortar_pelo)
    clientes= threading.Thread(target=añadir_cliente)
    barbero.start()
    clientes.start()
    clientes.join()