import threading
import time

# Prof. Gustavo Wagner, gugawag@gmail.com
# IFPB - Sistemas Operacionais
# Explicacao: programa desenvolvido para demonstrar condicao de disputa. Metodos p1 e p2, indefinidamente, incrementam
#             a variavel global 'numero'. Como nao hah exclusao mutua, pode haver condicao de corrida.


mutex = threading.Semaphore(1)
numero = 0

# Codigo estah pulando numeros, e repetindo numeros entre threads


def p1():
    global numero
    while numero < 30:
        mutex.acquire()
        numero += 1
        print('P1:', numero)
        mutex.release()


def p2():
    global numero
    while numero < 30:
        mutex.acquire()
        numero += 1
        print('P2:', numero)
        mutex.release()


#time.sleep(1)  # usado apenas para forcar trocar contexto entre threads e visualizar condicao de disputa
t_p1 = threading.Thread(target=p1)
t_p2 = threading.Thread(target=p2)
t_p1.start()
t_p2.start()
t_p1.join()
t_p2.join()
