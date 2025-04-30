
# Programa en Python que simule juego predictivo del clima.
# Usuario debe adivinar la temperatura generada con base en un rango proporcionado
# Solicitar a usuario que ingrese dos numeros int que represente un numero de grados posibles
# Primer numero > segundo numero
# Calcular temperatura promedio ajustada MEDIANTRE EL SIGUIENTE Procedimiento: 
#   Prom = (n1+n2)/2
# Ajuste climatico = (n2-n1)*0.25
# Usar random.uniform (promedio - ajuste , promedio + ajuste) -> De esta forma se ajusta la temperatura
# El usuario tiene 3 oportunidades para adivinar el número

import random


temp_1 = temp_2 = -100.0
temperatura_misteriosa = -100.0
temperatura_adivinada = -100.0

print('\t\t---Bienvenido a Adivinandoi a temperaturta--\n')

while(temp_1==-100.0 and temp_2==-100.0):
    try:
        temp_1 = float(input('Ingrese la temperatura mayor:\t->'))
        temp_2 = float(input('Ingrese la temperatura menor:\t->'))
    except:
        print('¡Mal ingreso!\n')
    if(temp_1>temp_2):
        break
    else:
        print('¡Mal ingreso!')
    temp_1 = temp_2 = -100.0

temp_prom = (temp_1+temp_2)/2
temp_ajuste = (temp_2-temp_1)*0.24
ajuste_final = random.uniform( temp_prom-temp_ajuste , temp_prom+temp_ajuste )

for intento in range(3):
    while(temperatura_adivinada==-100.0):
        try:
            temperatura_adivinada = float(input('Ingrese su intento:\t->'))
        except:
            print('¡Mal ingreso!')
    
    if (temperatura_adivinada==ajuste_final):
        print('¡¡¡Felicidades por enconmtrar la temperatura!!!')
        break
    else:
        print('Fallo :/ Intentelo nuevamente')
else:
    print('Perdiste :(')