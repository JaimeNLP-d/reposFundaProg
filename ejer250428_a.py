
# Programa en Python
# Que genere un numero aleatorio dentro de un rango(dos numeros) definido por el usuario. 
# Dividir el numero generado entre 4 
# El usuario de adivinar el numero generado. Máximo 3 intentos

#1. Ingreso de ambos datos
#2. El primer numero debe ser menor al segundo
#3. Generación del número aleatorio dentro del rango ingresado
#4. Del numero aleatorio, se debe generar un nuevo numero que es el '/4' del aleatorio.
#5. Redondear el numero'/4' al próximo entero
#6. Intentos de usuario: 3. 
#   6.1. Si acertara: se muestra mensaje de felicitacion.
#   6.2. Si se equivoca 1ra vez: muestra mensaje de si es mayor o menor.
#   6.3. Si se equivoca 2da vez: muestra mensaje de si es mayor o menor.
#   6.2. Si se equivoca 3ra vez: muestra mensaje de 'Perdiste'.

import random

n1_ingresado , n2_ingresado = -1 , -1
n_intentado = -1
n_misterioso = 0

print("\t\t---¡Bienvenido a adivinar tu subnumero!--\n")

while(n1_ingresado==-1 and n2_ingresado==-1):
    try:
        n1_ingresado = int(input("Ingrese un entero positivo para menor valor:\t->"))
        n2_ingresado = int(input("Ingrese un entero positivo para mayor valor:\t->"))
    except:
        print('¡Mal ingreso!\n')
    if( n2_ingresado>n1_ingresado ):
        break
    else:
        print('¡Mal ingreso!\n')
    n1_ingresado , n2_ingresado = -1 , -1

print(n1_ingresado, '---' , n2_ingresado)

n_misterioso = random.randrange( n1_ingresado , n2_ingresado)
n_misterioso = round( n_misterioso/4 )
print('Número misterioso generado')

for intento in range(3):
    n_intentado=-1
    while(n_intentado==-1):
        try:
            n_intentado = int(input(f'\nIntento número {intento+1} :\t->'))
        except:
            print('¡Mal ingreso!')
    
    if(n_intentado==n_misterioso):
        print('¡¡¡Felicitaciones!!! Número encontrado')
        break
    else:
        comparado = 'mayor' if n_intentado<n_misterioso else 'menor'
        print(f'Fallaste!\t--El número misterioso es {comparado} a tu número\n')
else:
    print('Perdiste :( ')
