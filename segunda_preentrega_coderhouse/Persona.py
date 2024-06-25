from typing import Any

#Defino la clase persona, para luego practicar herencia con Cliente, teniendo en cuenta en un futuro implementar la clase Proveedor. 
class Persona:

    def __init__(self, nombre, apellido, dni, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono

    def __str__(self):
        return f"Nombre y Apellido: {self.nombre} {self.apellido}.\nDni: {self.dni}.\nTeléfono: {self.telefono}"


#Defino la clase Cliente que hereda de Persona, con los atributos propios de dirección, estado, id, cantidad de compras y cuenta corriente. 
class Cliente(Persona):
    ultimo_id = 0 #inicializo ultimo id para generar un id autoincremental

    def __init__(self, nombre, apellido, dni, telefono, direccion):
        super().__init__(nombre, apellido, dni, telefono)
        self.direccion = direccion
        self.estado = 1# 0 = BAJA | 1 = ALTA
        self.id = Cliente.autoincremental() #El user no tendrá acceso a establecer el id, este será autoincremental. 
        self.cant_compras = 0 #Las compras y cta cte se inicializan en 0, serán manejadas desde el menú por el user. 
        self.total_cta = 0 

    #METODOS
    @classmethod 
    def autoincremental(cls): #Método para sumar +1 al id de la clase cada vez que se genere una instancia de ésta. 
        cls.ultimo_id += 1
        return cls.ultimo_id

    def imprimir(self):
        print("\n-------[ Ficha Cliente ]-------")
        print(f"""
ID: {self.id}.
Nombre: {self.nombre}.
Apellido: {self.apellido}. 
Dni: {self.dni}.
Teléfono: {self.telefono}.
Dirección: {self.direccion}.
Cantidad de compras: {self.cant_compras}.
Total Gastado: ${self.total_cta}.""")
        if self.estado == 0:
            print("Estado: BAJA")
        else:
            print("Estado: ALTA")

    def agregar_compra(self):
        self.cant_compras += 1
    
    def cargar_total(self, monto):
        self.total_cta += monto

    #GET
    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)
    
    #SET
    def __setattr__(self, name: str, value: Any) -> None:
        return super().__setattr__(name, value)
    
    


