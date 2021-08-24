Nombre=[]
Cedula=[]
Celular=[]



menuprincipal=int(input('Menú Principal: \n 1- Ver planilla \n 2- Insertar \n 3- Borrar \n 4- Modificar \n 0- Salir \n'))


while menuprincipal !=0:

    if menuprincipal==1:
        print('Codigo |     Nombre        |   Puesto       | Telefono')
        for x in range(len(Codigo)):
            print(Codigo[x], "       ",Nombre[x],"          ",Puesto[x], "        ",Telefono[x], "        ")

    elif menuprincipal==2:
        print('Llena los siguientes datos: ')
        Codigo.append(input('Codigo de la persona'))
        Nombre.append(input('Nombre de la persona'))
        Puesto.append(input('Puesto de la persona'))
        Telefono.append(input('Teléfono de la persona'))
    
    elif menuprincipal==3:
        print('Eliminando persona')
        cod=input('Ingresa el codigo a eliminar')
        for i in range(len(Codigo)-1,-1,-1):
            if Codigo[i]==cod:
                Codigo.pop(i)
                Nombre.pop(i)
                Puesto.pop(i)
                Telefono.pop(i)
        
        print('Persona eliminada')

    elif menuprincipal==4:
        print('Modificando persona')
        cod=input('Ingresa el codigo a modificar')

        for x in range(len(Codigo)):
            if Codigo[x]==cod:
                Nombre[x]=input('Cuál es el nuevo nombre? ')
                Puesto[x]=input('Cuál es el nuevo puesto? ')
                Telefono[x]=int(input('Cual es el teléfono? '))
        print('Persona modificada')

    else:
        print('Por favor digita una opción correcta')

    
    menuprincipal=int(input('Menú Principal: \n 1- Ver planilla \n 2- Insertar \n 3- Borrar \n 4- Modificar \n 0- Salir \n'))

