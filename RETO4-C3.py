#TÍTULO DEL PROGRAMA
print('BIENVENIDO AL SISTEMA DE REGISTRO DE NÓMINA DE DOCENTES CONTRATADOS POR HORAS')

#SE DECLARAN LAS VARIABLES

HTSemana=[]
HorasTSemana=[]
option='Si'

#Se realiza un while para el ingreso de datos dependiendo de lo que la persona quiera ingresar
while option=='Si':
    #Se definen las variables guardando el dato que se ingresa por teclado
    Nombre=input('Digite el nombre completo del docente: ')
    ValorHorasTSemana=input('Ingrese el valor de por hora de trabajo: ')

    for i in [1, 2, 3, 4]:
             HTSemana=input(f'Ingrese las horas trabajadas en la Semana {i}: ')
             HorasTSemana.append(HTSemana)

    print(HorasTSemana)
    
    def SumaSalarioBruto(HorasTSemana):
        if SumaSalarioBruto==[]:
            suma=0
            return 
        else:
            suma= HorasTSemana[0] + SumaSalarioBruto(HorasTSemana[1:])
        
        return suma 
    
    print(SumaSalarioBruto(HorasTSemana))



    #SalarioTotalBruto=sum(HorasTSemana.append(HTSemana))

    #def SumaSalarioBruto (HorasTSemana):
        #Suma=0
        #for x in HorasTSemana:
        #    Suma +=x
        #return Suma
    
    #print(SumaSalarioBruto (HorasTSemana))
    #SalarioTotalBruto=sum[HorasTSemana]
    #print(SalarioTotalBruto)

    

    #Se usa el .append para almacenar los datos ingresados por teclado en las listas

    
    #Se decalaran los if para almacenar los datos con errores
    def SalarioBruto():
        if HorasTSemana<40:
           SalarioBruto=ValorHorasTSemana*HorasTSemana
 

        if HorasTSemana>40:
           VHorasExtras=(1.5*ValorHorasTSemana)*(HorasTSemana-40)
           SalarioBruto=(ValorHorasTSemana*40)+VHorasExtras
    
        Parafiscales=0.09*SalarioBruto
        Prima=0.0833*SalarioBruto
        Cesantias=0.0833*SalarioBruto
        IntCesantias=0.01*SalarioBruto
        Vacaciones=0.0417*SalarioBruto
        DescuentoSalud=0.04*SalarioBruto
        DescuentoPension=0.04*SalarioBruto

    #print('El numero de total de días que duró la salida de campo fueron ', SalarioTotalBruto)


    option=input('Desea realizar más registros para otros docentes? (Escriba "Si" en caso de de desear ingresar más datos) ')

