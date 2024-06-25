"""
###SEGUNDA PRE-ENTREGA CURSO PYTHON - CODER HOUSE
##Comisión: 57815
##Estudiante: Escobar Tomé Yas'z.

##Objetivo:
#Practicar el concepto de Clases y Objetos.

##Consigna:
#- Crear un programa que permita el modelamiento de Clientes en una página de compras. Se debe utilizar el concepto de POO y lo aprendido en clase. 
#- Se evaluará el uso correcto de atributos y métodos.
#- Utilizar los conceptos aprendidos en la clase 14 y crear un paq. redistribuible con el programa creado. 

##Sugerencias:
#- La clase Cliente debe tener mínimo 4 atributos y 2 métodos. 
#- Se debe utilizar el método __str__() para darle nombre a los objetos.
#- Para crear el paquete distribuible también como adicional el archivo de la Pre-Entrega #1.
#- Es opcional el uso de herencia.  
# """

#---------------------------------------------------------------------------------------------------------------------------------------------
#Importaciones de módulos.
from segunda_preentrega_coderhouse.menu import *
from segunda_preentrega_coderhouse.archivos import *

#Creación de la lista de clientes, será cargada con los datos del archivo.
clientes = []
cargar_clientes(clientes)

#Ejecución del programa que se encargará de mostrar menúes y llamar funciones. 
programa(clientes)

#Al finalizar el programa, se guardan los clientes en el archivo y se cierra el archivo. 
guardar_clientes(clientes)



