from segunda_preentrega_coderhouse.Persona import Cliente

#FUNCIONES DE REGISTRO, BUSQUEDA, ALTA, BAJA, MODIFICACIÓN Y LISTAR.

#función para cargar un nuevo cliente por consola.
def registro(): 
    print("\n-------[ Nuevo Cliente ]-------")
    nombre = input("\n♥ Nombre: ")
    apellido = input("♥ Apellido: ")

    while True:
        try:
            dni = input("♥ Dni: ")
            dni = int(dni)
            break
        except ValueError:
            print("**Tipo de dato inválido! Ingresa un entero")

    while True:
        try:
            telefono = input("♥ Teléfono: ")
            telefono = int(telefono)
            break
        except ValueError:
            print("**Tipo de dato inválido! Ingresa un entero")

    direccion = input("♥ Dirección: ")
    nuevo_cliente = Cliente(nombre, apellido, dni, telefono, direccion)
    return nuevo_cliente

#función para buscar un cliente en la lista de clientes.
def buscar_cliente(clientes): 
    print("\n-------[ Buscar Cliente ]-------")
    op = -1
    buscado = -1
    try:
        op = int(input("\n1- Nombre y Apellido.\n2- Dni.\nIndica el método de búsqueda: "))
        while op <= 0 or op >= 3:
            op = int(input("**Ingresa una opción válida: "))
    except ValueError:
        print("**Tipo de dato inválido! Ingresa un número.")

    if op == 1: #Busqueda por nombre y apellido
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        for i, cliente in enumerate(clientes):
            if cliente.nombre == nombre and cliente.apellido == apellido:
                buscado = i
    elif op == 2: #Busqueda por DNI
        dni = int(input("Ingresa el DNI del cliente: "))
        for i, cliente in enumerate(clientes):
            if cliente.dni == dni:
                buscado = i
    
    if buscado == -1:
        print("**El cliente no existe!")

    return buscado

#Funciones de Alta y Baja lógica. Cambian el estado del cliente, si está en baja no será mostrado al listar ni se le podrán cargar compras. 
def alta(clientes, pos):
    if pos == -1:
        pass
    else:
        clientes[pos].estado = 1
        print(f"{clientes[pos].nombre} {clientes[pos].apellido} fue dado de alta!")

def baja(clientes, pos):
    if pos == -1:
        pass
    else:
        clientes[pos].estado = 0
        print(f"{clientes[pos].nombre} {clientes[pos].apellido} fue dado de baja!")

#Función para modificar clientes. 
def modificar_cliente(clientes, pos):
    print("\n-------[ Modificación Cliente ]-------")
    print("**Rellene los campos que desee cambiar, los vacíos no serán tomados en cuenta y prevalecerá el dato original.")
    nombre = input("♥ Nombre: ")
    apellido = input("♥ Apellido: ")

    dni = None
    try:
        dni_input = input("♥ Dni: ")
        if dni_input:
            dni = int(dni_input)
    except ValueError:
        print("**Tipo de dato inválido! Ingresa un entero")

    telefono = None
    try:
        telefono_input = input("♥ Teléfono: ")
        if telefono_input:
            telefono = int(telefono_input)
    except ValueError:
        print("**Tipo de dato inválido! Ingresa un entero")

    direccion = input("♥ Dirección: ")
    #Validación de campos y asignaciones. 
    if len(nombre) > 0:
        clientes[pos].nombre = nombre
    if len(apellido) > 0:
        clientes[pos].apellido = apellido
    if dni is not None:
        clientes[pos].dni = dni
    if telefono is not None:
        clientes[pos].telefono = dni
    if len(direccion) > 0:
        clientes[pos].direccion = direccion

    print(f"{clientes[pos].nombre} {clientes[pos].apellido} fue modificado!")

#Funcion para listar los clientes.
def listar(clientes):
    for cliente in clientes:
        if cliente.estado == 1: #si el cliente está dado de alta se mostrará. 
            print(f"{cliente.id}- {cliente.nombre} {cliente.apellido} - Total gastado: ${cliente.total_cta} - Compras realizadas: {cliente.cant_compras}")

#Función para cargar compras a los clientes.
def cargar_compra(cliente, monto):
    if cliente.estado == 1:
        cliente.agregar_compra()
        cliente.cargar_total(monto)
    else:
        print("El cliente está dado de baja, no se pueden cargar compras.")


