import random

wfc:bool = True
#puntajes_almacenados:list[int] = [ random.randint(1,10_000) for x in range(1,11) ]
puntajes_almacenados:list[int] = [ 100 , 200 , 50 ]
puntaje_ingresado:int = -1
opt:int = -1
mensaje_menu:str = '\nMenu:'+'\n1.)Ingresar puntaje/'+'\n2.)Mostrar mayor puntaje'+'\n3.)Mostrar promedio'+'\n4.)Salir'\


print('\n\t\t---Registro de puntajes de Epic---')

while(wfc):
    opt = puntaje_ingresado = -1

    while(opt not in [1,2,3,4]):
        try:
            opt = int(input(mensaje_menu+'\nIngrese opción:\t->'))
        except ValueError:  print('¡Mal ingreso! Debe ingresar un número')
        except TypeError as e:
            print('¡ERROR NO CONSIDERADO!')
            print(f'Bad input: {repr(e)}')
        if (opt not in [1,2,3,4]):
            print('¡Mal ingreso! Opción no permitida')
        
    match opt:
        case 1:
            while(puntaje_ingresado<1 or puntaje_ingresado>10_000):
                try:
                    puntaje_ingresado = int(input('Ingrese puntaje:\t->'))
                except ValueError:  print('¡Mal ingreso! Debe ingresar un número')
                except TypeError as e:
                    print('¡ERROR NO CONSIDERADO!')
                    print(f'Bad input: {repr(e)}')
                if (puntaje_ingresado<1 or puntaje_ingresado>10_000):
                    print('¡Mal ingreso! Puntaje debe estar entre 1 y 10.000')
            puntajes_almacenados.append(puntaje_ingresado)
        case 2:
            if( len(puntajes_almacenados)!=0 ):
                print('Mayor puntaje:' , max(puntajes_almacenados) )
            else:
                print('Sin puntaje')
        case 3:
            if( len(puntajes_almacenados)!=0 ):
                print('Puntaje promedio:' , sum(puntajes_almacenados)/len(puntajes_almacenados) )
            else:
                print('Sin puntaje')
        case 4: wfc = False

else:
    print('Hasta luego')