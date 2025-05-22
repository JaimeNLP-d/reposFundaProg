
# Programa con menu
#1.)Ingresar numero ; [1,100] ; a fallo: 'Debe ingresar un numero entero'
#2.)Mostrar mayor ; si no hay número guardado: 'Primero debe ingresar un valor'
#3.)Mostrar promedio ; si no hay número guardado: 'Primero debe ingresar un valor'
#4.)Salir ; poner mensaje
#
#


lista_numeros:list[int] = []
opt = numero_ingreso = -1
wfc:bool = True

print('\n\t\t---Bienvenido a listando números--')

while(wfc):

    opt = -1
    numero_ingreso = -1
    while(opt not in [1,2,3,4]):
        try:
            opt = int(input('\n1.) Ingrese un número entre 1 y 100\n2.) Mostrar mayor\n3.) Mostrar promedio\n4.)Salir\nIngrese una opción:\t->'))
        except ValueError: print('¡Mal ingreso! Debe ingresar un número entero')
        except: print('ERROR NO CONSIDERADO')
        if(opt not in [1,2,3,4]):
            print('¡Mal ingreso! Opción no valida')

    match opt:

        case 1:
            while(numero_ingreso<1 or numero_ingreso>100):
                try:
                    numero_ingreso = int(input('Número a ingresar:\t->'))
                except ValueError: print('¡Mal ingreso! Debe ingresar un número entero')
                except: print('ERROR NO CONSIDERADO')
                if(numero_ingreso<1 or numero_ingreso>100):
                    print('El número debe estar entre 1 y 100')
                else:
                    lista_numeros.append(numero_ingreso)

        case 2:
            if(len(lista_numeros) == 0):
                print('No hay números guardados')
            else:
                print(max(lista_numeros))

        case 3:
            if(len(lista_numeros) == 0):
                print('No hay números guardados')
            else:
                print( sum(lista_numeros) / len(lista_numeros) )

        case 4:
            wfc = False

else:
    print('Hasta luego')