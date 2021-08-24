#TÍTULO DEL PROGRAMA
print('BIENVENIDO AL SISTEMA DE REGISTRO DE NÓMINA DE DOCENTES CONTRATADOS POR HORAS')

#SE DECLARAN LAS VARIABLES
option='Si'

#Se realiza un while para el ingreso de datos dependiendo de lo que la persona quiera ingresar
while option=='Si':
    #Se definen las variables guardando el dato que se ingresa por teclado
    Nombre=input('Digite el nombre completo del docente: ')
    ValorHorasTSemana=input('Ingrese el valor de por hora de trabajo: ')
    HorasTSemana1=input('Ingrese las horas trabajadas en la Semana 1: ')
    HorasTSemana2=input('Ingrese las horas trabajadas en la Semana 2: ')
    HorasTSemana3=input('Ingrese las horas trabajadas en la Semana 3: ')
    HorasTSemana4=input('Ingrese las horas trabajadas en la Semana 4: ')
    #Se usa el .append para almacenar los datos ingresados por teclado en las listas

    
    #Se decalaran los if para almacenar los datos con errores
    def SalarioBruto():
        if HorasTSemana1<40:
           SalarioBruto=ValorHorasTSemana*HorasTSemana1
 

        if HorasTSemana1>40:
           VHorasExtras=(1.5*ValorHorasTSemana)*(HorasTSemana1-40)
           SalarioBruto=(ValorHorasTSemana*40)+VHorasExtras
    
        Parafiscales=0.09*SalarioBruto
        Prima=0.0833*SalarioBruto
        Cesantias=0.0833*SalarioBruto
        IntCesantias=0.01*SalarioBruto
        Vacaciones=0.0417*SalarioBruto
        DescuentoSalud=0.04*SalarioBruto
        DescuentoPension=0.04*SalarioBruto


    option=input('Desea realizar más registros para otros docentes? (Escriba "Si" en caso de de desear ingresar más datos) ')




#print(f'El porcentaje 2 de días que se reportaron errores respecto del total de días reportados es: {perrores2}%')
