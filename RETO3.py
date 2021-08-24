#TÍTULO DEL PROGRAMA
print('BIENVENIDO AL SISTEMA DE REGISTRO DE TEMPERATURAS')

#SE DECLARAN LAS VARIABLES
ListaTempereatura=[]
ListaTMax=[]
ListaTmin=[]
ErroresTMayores=[]
ErroresTMenores=[]
ErroresTMayMen=[]
option='Si'


#Se realiza un while para el ingreso de datos dependiendo de lo que la persona quiera ingresar
while option=='Si':
    #Se definen las variables guardando el dato que se ingresa por teclado
    TMax=int(input('Ingrese la temperatura máxima del día en grados (La temperatura máxima y la temperatura mínima igual a 0 no será válida e indicará que se han terminao los datos de la salida de campo): '))
    TMin=int(input('Ingrese la temperatura mínima del día en grados (La temperatura máxima y la temperatura mínima igual a 0 no será válida e indicará que se han terminao los datos de la salida de campo): '))
    #Se usa el .append para almacenar los datos ingresados por teclado en las listas
    ListaTempereatura.append((TMax,TMin))
    ListaTMax.append(TMax)
    ListaTmin.append(TMin)

    #Se decalaran los if para almacenar los datos con errores
    if TMax>35:
       ETMayor=1
       ErroresTMayores.append(ETMayor)

    if TMin<5:
       ETMin=1
       ErroresTMenores.append(ETMin)

    if TMin<5 and TMax>35:
       ETMayorMin=1
       ErroresTMayMen.append(ETMayorMin)

    if TMax==0 and TMin==0 == False:
        ListaTempereatura.pop(-1)
        ErroresTMenores.pop(-1)
      
        ListaTmin.pop(-1)
        ListaTMax.pop(-1)
        break




    #Se captura el valor ingresado por teclado para saber si se siguen almancenando más datos o no
        
    option=input('Desea llenar más datos? (Escriba "Si" en caso de de desear ingresar más datos) ')


#Se muestra en pantalla con el print lo solicitado en el reto
print(ListaTempereatura) 
print('El numero de total de días que duró la salida de campo fueron ', len(ListaTempereatura))



print('El numero de días con errores por temperaturas mayores a 35 grados son: ', len(ErroresTMayores))


print('El numero de días con errores por temperaturas menores a 5 grados son: ', len(ErroresTMenores))

print('El numero de días con ambos errores en simultáneo son: ', len(ErroresTMayMen))

#Se hace operación del total de errores   
ErroresTotales=((len(ErroresTMayores))+(len(ErroresTMenores)))

print('El numero total de errores por temperaturas mayores a 35 y menores a 5 grados son: ', ErroresTotales)

#Se hace la operación de porcentaje con regla de 3
perrores=(100*(ErroresTotales))/(len(ListaTempereatura))
#Se hacen las operaciones para los promedios
meanMax=sum(ListaTMax)/len(ListaTMax)
meanMin=sum(ListaTmin)/len(ListaTmin)

print('La temperatura media máxima es: ', meanMax)
print('La temperatura media mínima es: ', meanMin)
print(f'El porcentaje de días que se reportaron errores respecto del total de días reportados es: {perrores}%')