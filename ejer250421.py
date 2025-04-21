
#Desarrolle programa en Python que realize estudio social de calificaciones
#Mayor calificacion => mayor descuento
# Nota >6 => 20% descuento
# Nota >5 => 15% descuento
# Nota >4 =>  5% descuento
# Valor de curso = 200k$
# Pregunta la calificación al usuario


notaIngresada = -1.0

print('\t--Bienvenido a Calcula tu descuento--')

while(notaIngresada<1.0 or notaIngresada>7.0):
    try:
        notaIngresada = float(input('Ingrese su calificación:\t->'))
        if (notaIngresada<1.0 or notaIngresada>7.0):
            print('¡Mal ingreso!')
    except:
        print('!Mal ingreso!')
        notaIngresada = -1.0

if(notaIngresada>=6.0):
    print('Precio de curso: $',  200000*0.8 )
elif(notaIngresada>=5.0):
    print('Precio de curso: $',  200000*0.85 )
elif(notaIngresada>=4.0):
    print('Precio de curso: $',  200000*0.95 )
else:
    print('Precio de curso: $',  200000 )