from segunda_preentrega_coderhouse.ABM import *
from segunda_preentrega_coderhouse.Persona import *

#Menúes y llamados a funciones para gestionar el programa desde la consola. 

def cabecera():
    print("\n[ Segunda pre-entrega curso PYTHON - Coder House ]")
    print("[ Estudiante: Yas'z Escobar Tomé. ]")

#Menú general
def menu(): 
    op = -1
    print("""\n---------------[ MENÚ ]---------------
\n1- Nuevo Cliente.
2- Alta | Baja | Modificación.
3- Cargar Compra.
4- Mostrar Cliente.
5- Listar Clientes.
0- Salir.""")
    try:
        op = int(input("\nElije una opción: "))
        while op < 0 or op >= 6: 
            op = int(input("**Ingresa una opción válida: "))  
    except ValueError:  
        print("**Tipo de dato inválido! Ingresa un número.") 
    return op



#Menú alta | baja | modificación
def menu_abm():
    op = -1 
    print("""\n---------------[ A B M ]---------------
\n1- Alta.
2- Baja.
3- Modificación.
0- Volver al menú anterior.""")
    try:
        op = int(input("\nElije una opción: "))
        while op < 0 or op >= 4:
            op = int(input("**Ingresa una opción válida: "))
    except ValueError:
        print("**Tipo de dato inválido! Ingresa un número.")
    return op

def programa_abm(clientes):
    pos = -1
    abm = -1
    abm = menu_abm()
    
    if abm == 0:
        pass
    else:
        pos = buscar_cliente(clientes)
        if abm == 1: #Alta
            alta(clientes, pos)
        elif abm == 2: #Baja
            baja(clientes, pos)
        elif abm == 3: #Modificación
            modificar_cliente(clientes, pos)


def programa(clientes):
    cabecera()
    op = -1
    
    while op != 0:
        op = menu()
        if op == 1: #Nuevo cliente.
            clientes.append(registro())
            print("Cliente registrado con éxito!")
            clientes[-1].imprimir()
        elif op == 2: #ABM
            programa_abm(clientes)
        elif op == 3: #Cargar Compra
            pos = buscar_cliente(clientes)
            monto = float(input("Ingresa el monto de la compra: "))
            cargar_compra(clientes[pos], monto)
        elif op == 4: #Mostrar Cliente
            pos = buscar_cliente(clientes)
            if pos != -1:
                clientes[pos].imprimir()
            else:
                pass
        elif op == 5: #Listar Cliente. 
            listar(clientes)
        elif op == 0: #Salir
            print("\n--------------------------------------")
            print("   ¡Gracias por probar mi programa!\n   Hasta lueguito.. ;)")
            print("--------------------------------------")   
