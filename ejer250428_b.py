
# Programa en Python que calcule el subsidio de gas según el quintil de ingresos
# Condiciones socioeconomicas: Quintiles de ingreso: "1 = Menores ingresos" ; 5 = "Mayores ingresos"
# Condiciones laborales: Se considera si la persona esta 'Desempleada' o 'Empleada'
#
#
# Quintil
#        |  1o2  |  1o2  |  3  |  3  |  4o5  |
#
# Condición laboral
#        |  Desempleado  |  Empleado  |  Desempleado  |  Empleado  |  Cualquiera  |
#
# Subsidio de gas
#        |  10_000  |  8_000  |  6_000  |  4_000  |  1_500  |

ing_quintil = -1
ing_situacion = ''

print('\t\t--Bienvenido a calculadora de subsidio de gas--')

while(ing_quintil not in [1,2,3,4,5]):
    try:
        ing_quintil = int(input('\nIngrese su quintil:\t->'))
    except:
        print('¡Mal ingreso!')
    if( ing_quintil not in [1,2,3,4,5] ):
        print('Quintil no reconocido')

while( ing_situacion!='E' and ing_situacion!='e' and ing_situacion!='D' and ing_situacion!='d' ):
    ing_situacion = input('\nIngrese su situación laboral\nEmpleado(E) / Desempleado(D):\t->')
    if ( ing_situacion!='E' and ing_situacion!='e' and ing_situacion!='D' and ing_situacion!='d' ):
        print('¡Mal ingreso!')
ing_situacion = ing_situacion.upper()

if (ing_quintil in [1,2]) and ing_situacion=='D':
    print('Subsidio de gas: $10.000')
elif (ing_quintil in [1,2]) and ing_situacion=='E':
    print('Subsidio de gas: $8.000')
elif (ing_quintil == 3) and ing_situacion=='D':
    print('Subsidio de gas: $6.000')
elif (ing_quintil == 3) and ing_situacion=='E':
    print('Subsidio de gas: $4.000')
elif (ing_quintil in [4,5]):
    print('Subsidio de gas: $1.500')
else:
    print('ERROR no considerado')