from segunda_preentrega_coderhouse.ABM import *

#Gestión de archivos. 

#Si el archivo de clientes existe lo leemos para cargar la lista de clientes.
def cargar_clientes(clientes):
    try:
        with open('archivo_clientes.txt', 'r') as file:
            for line in file: #Por cada línea del archivo creamos a cada cliente.
                datos_cliente = line.strip().split(',')
                nombre = datos_cliente[0]
                apellido = datos_cliente[1]
                dni = int(datos_cliente[2])
                telefono = datos_cliente[3]
                direccion = datos_cliente[4]
                estado = int(datos_cliente[5])
                id = int(datos_cliente[6])
                cant_compras = int(datos_cliente[7])
                total_cta = float(datos_cliente[8])

                cliente = Cliente(nombre, apellido, dni, telefono, direccion)
                cliente.estado = estado
                cliente.id = id
                cliente.cant_compras = cant_compras
                cliente.total_cta = total_cta

                clientes.append(cliente)               
    except FileNotFoundError:
        print("Ups! No se encontró el archivo.")

#Función para guardar el arreglo de clientes en el archivo antes de cerrar el programa.
def guardar_clientes(clientes):
    with open('archivo_clientes.txt', 'w') as file:
        for cliente in clientes:
            file.write(f"{cliente.nombre},{cliente.apellido},{cliente.dni},{cliente.telefono},{cliente.direccion},{cliente.estado},{cliente.id},{cliente.cant_compras},{cliente.total_cta}\n")
