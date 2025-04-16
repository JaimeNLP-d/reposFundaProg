
#Programa es interface de una revista.
#1.- Pide usuario y contraseña.
#2.- Registra nuevo usuario: nombre, usuario, edad, contraseña
#3.- Si(18>) -> acepta // SiNo(18>)
#4.- 

ListaParesAuth = []
respuestaIC = ''
respuestaSN = ''
wfc = True
name = ''
password = ''
edad = ''
tuplaAuth = ('','')

print('\t\t-Bienvenido a <nombre_pagina>-')

while (wfc):
    respuestaIC = ''
    respuestaSN = ''
    name = ''
    password = ''
    edad = ''

    #------------------------------------
    while( respuestaIC!='I' and respuestaIC!='i' and respuestaIC!='C'and respuestaIC!='c' ):
        respuestaIC = input('Ingresar(I) / Crear cuenta(C)\t')
        if ( respuestaIC!='I' and respuestaIC!='i' and respuestaIC!='C'and respuestaIC!='c' ):
            print('¡Mal Ingreso!')
    #------------------------------------


    #------------------------------------
    if (respuestaIC=='I' or respuestaIC=='i'):
        name = input('Ingrese nombre:\t->')
        password = input('Ingrese contraseña:\t->')
        tuplaAuth = (name, password)
        if (tuplaAuth in ListaParesAuth):
            print(f'Entrada aceptada. Bienvenido, {name}')
        else:
            print('Credenciales no aceptadas')
    #------------------------------------


    #------------------------------------
    if (respuestaIC=='C' or respuestaIC=='c'):
        name = input('Ingrese nombre:\t->')
        password = input('Ingrese contraseña:\t->')
        while(type(edad)!=int):
            try:
                edad = int(input('Ingrese edad:\t->'))
            except:
                print('¡Mal ingreso!')
        
        if(edad>=18):
            print('Registro correcto')
            ListaParesAuth.append((name,password))
        else:
            print('No cumple con la edad requerida')
    #------------------------------------


    for i in ListaParesAuth:
        print(i)
    
    #------------------------------------
    while( respuestaSN!='S' and respuestaSN!='s' and respuestaSN!='N'and respuestaSN!='n' ):
        respuestaSN = input('¿Desea hacer otra operación?(S/N)')
        if ( respuestaSN!='S' and respuestaSN!='s' and respuestaSN!='N'and respuestaSN!='n' ):
            print('¡Mal Ingreso!')
    #------------------------------------
    
    if (respuestaSN=='N' or respuestaSN=='n'):
        wfc = False