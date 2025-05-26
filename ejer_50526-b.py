#
# Programa de sistema simple de venta entradas de cine
# Progama debe comenzar con 70 entradas
# 
# Menu/Pasos:
#1.) Da bienvenida
#2.) Mostrar entradas disponibles
#3.) Mostrar entradas no disponibles
#4.) Preguntar cantidad de entradas a comprar
#5.) Salir. Mensaje de despedida


import random

##Cambiar 'indice' a 'indice+1' para "simular" asientos desde el 1 al 70. Ahora mismo se asumirá que los asientos van del 0 al 69

#Función que retorna una lista con los indices de todos los elementos que tengan '0'
def entradas_disponibles(lista_estados:list[int])->list[int]:
    return [ indice for indice,valor in enumerate(lista_estados) if valor==0 ]

#Función que retorna una lista con los indices de todos los elementos que tengan '1'
def entradas_ocupadas(lista_estados:list[int])->list[int]:
    return [ indice for indice,valor in enumerate(lista_estados) if valor==1 ]


total_entradas:int = 15
opt:int
wfc:bool = True
cantidad_entradas = entrada_seleccionada = -1
lista_entradas_a_comprar:list[int] = []

estado_asientos = [ random.randint(0,1) for x in range(1,total_entradas+1) ]
#print(len(estado_asientos))
#lista_prueba_total:list[int] = [1,1,1,0,0,1,0]

print('\n\t\t---Bienvenido a Venta de Entradas---')

lista_asientos_disponibles = entradas_disponibles(estado_asientos)
print(f'\nAsientos disponibles: {lista_asientos_disponibles}')
print(f'\nAsientos no disponibles: {entradas_ocupadas(estado_asientos)}')

while(cantidad_entradas<0):
    try:
        cantidad_entradas = int(input('\nIngrese cantidad de entradas a comprar:\t->'))
    except ValueError: print('¡Mal Ingreso! Deben ser números')
    except: print('ERROR NO CONSIDERADO')
    if(cantidad_entradas<0):
        print('Mal ingreso! Debe ser un número positivo')

lista_entradas_a_comprar.clear()
for compra_entrada in range(1,cantidad_entradas+1):
    entrada_seleccionada=-1
    while(entrada_seleccionada not in lista_asientos_disponibles):
        try:
            entrada_seleccionada = int(input(f'\nIngrese entrada {compra_entrada} a comprar:\t->'))
        except ValueError: print('¡Mal Ingreso! Deben ser números')
        except:  print('ERROR NO CONSIDERADO')
        if(entrada_seleccionada not in lista_asientos_disponibles):
            print('Debe ser un asiento disponible')
        elif(entrada_seleccionada in lista_entradas_a_comprar):
            print('Ya tiene seleccionada esta entrada')
            entrada_seleccionada=-1
    lista_entradas_a_comprar.append(entrada_seleccionada)

for asiento in lista_entradas_a_comprar:
    estado_asientos[asiento] = 1

print('\n\tTransacción realizada')
print(f'\nAsientos disponibles: {entradas_disponibles(estado_asientos)}')
print(f'\nAsientos no disponibles: {entradas_ocupadas(estado_asientos)}')