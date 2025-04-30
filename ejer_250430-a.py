#
# Programa calcula subsicio mensual de transporte estudiantil para estudiantes Duoc 2025
# Considera puntaje de admision
# Considera lugar de residendcia
# Condiciones academicas: Puntaje admición Duoc [450,850]
# Condiciones biográficas: Distancia del hogar a cede San Joaquin
# Beneficios:
#     |  Puntaje de admisión  |  Distancia de Hogar  |  Subsidio  |
#     |  >700  |  >20Km  |  $180_000  |
#     |  >700  |  [10Km , 20Km]  |  $130_000  |
#     |  ]600,700]  |  >20Km  |  $100_000  |
#     |  ]600,700]  |  [10Km , 20Km]  |  $80_000  |
# Bono adicional: Si el estudiante vive en una zona rural debe indicar "Sí" o "No". De ser positivo recibirá un bono de 40k$
# Si su puntaje es mayor a 550, recibira un bono de 20k$
# Requisitos del programa: solicitar puntaje de admisión, la distancia ( en kilometros), y si su recidencia es rural o no
# Calcula el subcidio base según al condición
# Verificar si corresponde a alguno de los bonos
# Mostrar en pantalla el subsidio

ingr_distancia = ingr_puntaje = -1
respuesta_SN = ''
bono_R = 40_000
bono_P = 20_000
bono_X = 0
mens_re = 'Sin bono'
mens_bo = 'Su bono es de $'

print("\t\t---Bienvenido a calculadora de subsidio---")

while(ingr_puntaje==-1):
    try:
        ingr_puntaje = int(input('Ingrese el puntaje de admisión:\t->'))
    except:
        print('¡Mal ingreso!\n')
        ingr_puntaje = -1

while(ingr_distancia==-1):
    try:
        ingr_distancia = int(input('Ingrese el distancia a cede San Joaquin (en Kilometros):\t->'))
    except:
        print('¡Mal ingreso!\n')
        ingr_distancia = -1

while( respuesta_SN!='S' and respuesta_SN!='s' and respuesta_SN!='N' and respuesta_SN!='n' ):
    respuesta_SN = input('¿Pertenece a una zona rural?(S/N):\t->')
    if( respuesta_SN!='S' and respuesta_SN!='s' and respuesta_SN!='N' and respuesta_SN!='n' ):
        print('¡Mal ingreso!\n')

bono_X = bono_X+bono_R if respuesta_SN.upper()=='S' else bono_X
bono_X = bono_X+bono_P if ingr_puntaje>750 else bono_X
#print(bono_X)

if(ingr_puntaje<600 or ingr_distancia<10):
    print(mens_re)
elif( (ingr_puntaje>600 and ingr_puntaje<=700) and (ingr_distancia>=10 and ingr_distancia<=20) ):
    print(mens_bo + str(80_000+bono_X) )
elif( (ingr_puntaje>600 and ingr_puntaje<=700) and (ingr_distancia>20) ):
    print(mens_bo + str(100_000+bono_X) )
elif( (ingr_puntaje>700) and (ingr_distancia>=10 and ingr_distancia<=20) ):
    print(mens_bo + str(130_000+bono_X) )
elif( (ingr_puntaje>700) and (ingr_distancia>20) ):
    print(mens_bo + str(180_000+bono_X) )
else:
    print('ERROR no considerado')