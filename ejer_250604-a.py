
#
# Programa en Python de calificaciones
# Asignaturas: Matematicas, Castellano y Base de Datos 1
# Datos estudiante: Nombre, asignatura inscrita, calificacion, carrera
# Información debe imprimirse en un .txt
#
#

ingreso_calificacion = -1.0
ingreso_string = ''
ficha_estudiante:dict = {}

while(ingreso_string==''):
    ingreso_string = input('Ingrese nombre:\t\t->')
ficha_estudiante['Nombre'] = ingreso_string
ingreso_string=''
while(ingreso_string==''):
    ingreso_string = input('Ingrese carrera:\t->')
ficha_estudiante['Carrera'] = ingreso_string

for asignatura in ['Matemáticas', 'Castellano' , 'Base de Datos 1']:
    ingreso_calificacion = -1.0
    while(ingreso_calificacion<1 or ingreso_calificacion>7):
        try:
            ingreso_calificacion = float(input(f'Ingrese calificación de {asignatura}:\t->'))
        except ValueError: print('¡Mal ingreso! Debe ingresar un número')
        except Exception as e:
            print('ERROR NO CONSIDERADO')
            print(repr(e))
        else:
            if (ingreso_calificacion<1 or ingreso_calificacion>7): print('¡Mal ingreso! Debe ser un número entre 1 y 7')
    ficha_estudiante[asignatura] = ingreso_calificacion


with open("ficha.txt" , 'w') as ficha:
    for campo,valor in ficha_estudiante.items():
        ficha.write(f'{campo} : {valor}\n')