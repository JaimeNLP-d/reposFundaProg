#
# Programa calcula el area de varios triangulos.
# Ingreso: número de triangulos a calcular
# Por cada triangulo, se ingresa 'base' y 'altura' (números coherentes); tipo float
# Area = (base * altura) / 2
#
#

cantidad_triangulos:int = -1
base = altura = -1.0
suma_area:float = 0


print("\n\t\t---Bienvenido a suma de areas---")

while(cantidad_triangulos<0):
    try:
        cantidad_triangulos = int(input('\nIngrese cantidad de triangulos:\t->'))
    except ValueError:
        print('¡Mal Ingreso! Debe ingresar un numero entero')
    except:
        print('ERROR NO ESPERADO')
    if(cantidad_triangulos<0):
        print('Cantidad de trieangulos debe ser positiva')

for iteracion_triangulo in range(1 , cantidad_triangulos+1):
    base = altura = -1.0
    while( base<=0 or altura<=0 ):
        try:
            altura = float(input(f"\nIngrese altura de {iteracion_triangulo}° triangulo:\t->"))
            base = float(input(f"\nIngrese base de {iteracion_triangulo}° triangulo:\t->"))
        except ValueError:
            print("¡Mal ingreso de datos! Deben ser números")
        except:
            print('\nERROR NO ESPERADO')
        if( base<=0 or altura<=0 ):
            print('Ambos valores deben ser positivos')
    
    suma_area += base * altura / 2

print(f'\n\tLa suma de los triangulos es : {suma_area}')