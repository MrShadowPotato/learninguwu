import sys


with open('pedidos.txt', 'r', encoding='utf8') as archivo:
    lineas = archivo.readlines()

if len(lineas) % 15 != 0:
    print('Error. El numero de lineas del archivo no es un multiplo de 15')
    sys.exit()

cantidad_pedidos = int(len(lineas) / 15)

for num_pedido in range(cantidad_pedidos):
    pedido = []
    for index in range(15):
        
