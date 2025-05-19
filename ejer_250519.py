#
#Progama de temperaturas
#--Menu--
#1.) Registrar temperatura
#2.) Mostrar t° más alta [°C] ; [-30.0 , 50.0]
#3.) Mostrar t° más baja [°C] ; [-30.0 , 50.0]
#4.) Salir
# Manejar excepciones de ingreso
# Hacer loop hasta hacer un ingreso valido
# Si ingresa valor fuera de rango, mostrar "Temperatura debe de estar en [-30.0 , 50.0]"
# Si ingreso es valido, mostrar "Exito en ingreso"
# Despedirse en salida

wfc:bool = True
lista_temperaturas:list[float] = []
opt:int = -1
temperatura_ingresada:float = -100.0

print('\n\t\t---Bienvenido a registro de temperaturas---')

while(wfc):

    opt=-1
    while(opt not in [1,2,3,4]):
        try:
            opt = int(input('\nMenu:\n1.) Registrar temperatura\n2.) Mostrar mayor temperatura\n3.) Mostrar menor temperatura\n4.) Salir\nOpción->'))
        except ValueError: print('¡Mal ingreso!\tDebe ingresar un número')
        except: print('¡ERROR NO MANEJADO!')
        if(opt not in [1,2,3,4]):
            print('Opción no valida')

    match opt:

        case 1:
            temperatura_ingresada = -100.0
            while(temperatura_ingresada>50 or temperatura_ingresada<-30):
                try:
                    temperatura_ingresada = float(input('\nIngrese la nueva temperatura; en un rango de -30.0 - 50.0:\t->'))
                except ValueError: print('¡Mal ingreso!\tDebe ingresar un número')
                except: print('¡ERROR NO MANEJADO!')
                if(temperatura_ingresada>50 or temperatura_ingresada<-30):
                    print("Temperatura debe de estar en [-30.0 , 50.0]")
            lista_temperaturas.append(temperatura_ingresada)
            print("Exito en ingreso")

        case 2:
            try:
                print(f'Mayor temperatura: {max(lista_temperaturas)}')
            except ValueError: print('Lista no tiene ningun ingreso')
            except: print('¡ERROR NO MANEJADO')

        case 3:
            try:
                print(f'Menor temperatura: {min(lista_temperaturas)}')
            except ValueError: print('Lista no tiene ningun ingreso')
            except: print('¡ERROR NO MANEJADO')

        case 4:
            wfc = False

else:
    print('\n\tHasta luego')