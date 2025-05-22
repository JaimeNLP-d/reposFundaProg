#
# Programa con menu; DirectTv
#1.) Navegar dentro de peliculas
#2.) Grabar pelicula
#3.)Configurar decofificador
#4.)Salir
#


opt:int = -1
wfc:bool = True

print('\n\t\t---Bienvenido a DirectTV--')

while(wfc):
    
    opt=-1
    while(opt not in [1,2,3,4]):
        try:
            opt = int(input('\n1.) Navegar dentro de peliculas\n2.) Grabar pelicula\n3.) Configurar decofificador\n4.)Salir\nIngrese una opción:\t->'))
        except ValueError:
            print('¡Mal ingreso! Debe ingresar un número entero')
        if(opt not in [1,2,3,4]):
            print('¡Mal ingreso! Opción no valida')
    
    match opt:
        case 1:
            print('\n\t*Navegando catalogo*')
        case 2:
            print('\n\t*Grabando pelicula*')
        case 3:
            print('\n\t*Configurando decodificador*')
        case 4:
            wfc = False

else:
    print('Hasta luego')