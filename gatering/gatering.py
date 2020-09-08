import csv
from pyexcel.cookbook import merge_all_to_a_book
import glob 

def destino_diferenciar(opcion):
    if 'Sucursal[x]' in opcion or 'Sucursal[X]' in opcion:
        return 'Sucursal'
    elif 'Domicilio[x]' in opcion or 'Domicilio[X]' in opcion:
        return 'Domicilio'
    else :
        return 'No indica'

def agencia_diferenciar(opcion):
    if 'EnviosyEnvios[x]' in opcion or 'EnviosyEnvios[X]' in opcion:
        return 'EnviosyEnvios'
    elif 'Starken[x]' in opcion or 'Starken[X]' in opcion:
        return 'Starken'
    elif 'CorreosDeChile[x]' in opcion or 'CorreosDeChile[X]' in opcion:
        return 'CorreosDeChile'
    else:
        return 'No indica'

def tipo_diferenciar(opcion):
    if 'Sobre[x]' in opcion or 'Sobre[X]' in opcion:
        return 'Sobre'
    elif 'Encomienda[x]' in opcion or 'Encomienda[X]' in opcion:
        return 'Encomienda'
    else: 
        return 'No indica'



pedidos = []
archivo = open('pedidos.txt','r',encoding='utf8')
for linea in archivo:
    pedidos.append(linea.strip('\n'))
archivo.close()
print(len(pedidos))
lista_pedidos = []
for numero_pedido in range(int(len(pedidos)/15)):  
    cliente = {}
    for index in range(15):
        info_cliente = pedidos[index + (15*numero_pedido)]
        info_cliente = info_cliente.split(':')
        info_cliente[0] = info_cliente[0].strip(' -')
        if info_cliente[0] == 'Destino':
            info_cliente[1] = destino_diferenciar(info_cliente[1])
        elif info_cliente[0] == 'Agencia':
            info_cliente[1] = agencia_diferenciar(info_cliente[1])
        elif info_cliente[0] == 'Tipo':
            info_cliente[1] = tipo_diferenciar(info_cliente[1])
        elif info_cliente[0] in 'Libro Comun,Libro Mencion,Llavero Comun,Llavero Mencion,Libros de ejercicios,Taco de notas':
            info_cliente[1] = info_cliente[1].strip().strip('[]')
        cliente[info_cliente[0]] = info_cliente[1]
    lista_pedidos.append(cliente)

formato = 'Nombre,Rut,Telefono,Agencia,Tipo,Destino,Direccion,Comuna,Comentario,Libro Comun,Libro Mencion,Llavero Comun,Llavero Mencion,Libros de ejercicios,Taco de notas'
formato_lista = formato.split(',')

listado_pedidos = open('ListadoPedidos.csv','w',encoding='utf8')
listado_pedidos.write(formato)
for cliente in lista_pedidos: 
    informacion_clientes = []
    for num in range(15):
        info = cliente[formato_lista[num]] 
        informacion_clientes.append(info)
    print(informacion_clientes)
    fila = ','.join(informacion_clientes)
    listado_pedidos.write('\n' + fila)
listado_pedidos.close


#merge_all_to_a_book(glob.glob('ListadoPedidos.csv'),"final.xlsx")

print(lista_pedidos)

print(len(lista_pedidos))
