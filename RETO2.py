print ('Bienvenidos al sistema de Descuentos de Matrícula')

BeneficioEdad=0
BeneficioPuntaje=0
BeneficioIngresos=0
BeneficioTotal=0
Nombre=input('Digite el nombre completo: ')
Edad=int(input('Digite la edad en años: '))
Puntaje=int(input('Digite el puntaje obtenido en el examen de 0 a 100 (números enteros): '))
Ingresos=float(input('Digite el número decimal de salarios mínimos mensuales que tiene de ingreso familiar: '))

print(f"El nombre completo registrado es: {Nombre}")
print(f"La edad registrada es: {Edad}")
print(f"El puntaje obtenido en el examen registrado es: {Puntaje}")
print(f"El número decimal de salarios mínimos mensuales que tiene de ingreso familiar registrado es: {Ingresos}")

if Edad>=15 and Edad<=18 :
    BeneficioEdad=25
    print(f'Su descuento de matrícula por edad es: {BeneficioEdad}%')
elif Edad>=19 and Edad<=21 :
    BeneficioEdad=15
    print(f'Su descuento de matrícula por edad es: {BeneficioEdad}%')
elif Edad>=22 and Edad<=25 :
    BeneficioEdad=10
    print(f'Su descuento de matrícula por edad es: {BeneficioEdad}%')
elif Edad<=14 or Edad>=26 :
    print('No tiene ningún apoyo por edad')

if Ingresos>1 and Ingresos<=2 :
    BeneficioIngresos=20
    print(f'Su descuento de matrícula por ingreso familiar es: {BeneficioIngresos}%')

elif Ingresos>2 and Ingresos<=3 :
    BeneficioIngresos=10
    print(f'Su descuento de matrícula por ingreso familiar es: {BeneficioIngresos}%')

elif Ingresos>3 and Ingresos<=4 :
    BeneficioIngresos=5
    print(f'Su descuento de matrícula por ingreso familiar es: {BeneficioIngresos}%')

elif Ingresos>4 :
    print('No tiene ningún apoyo por ingreso familiar')

if Puntaje>=80 and Puntaje<86 :
    BeneficioPuntaje=30
    print(f'Su descuento de matrícula por puntaje es: {BeneficioPuntaje}%')

elif Puntaje>=86 and Puntaje<91 :
    BeneficioPuntaje=35
    print(f'Su descuento de matrícula por puntaje es: {BeneficioPuntaje}%')

elif Puntaje>=91 and Puntaje<96 :
    BeneficioPuntaje=40
    print(f'Su descuento de matrícula por puntaje es: {BeneficioPuntaje}%')

elif Puntaje>=96 and Puntaje<=100 :
    BeneficioPuntaje=45
    print(f'Su descuento de matrícula por puntaje es: {BeneficioPuntaje}%')

elif Puntaje>100 :
    print('El puntaje máximo es de 100')

elif Puntaje<80 :
    print('No tiene ningún apoyo por puntaje')

BeneficioTotal=BeneficioEdad+BeneficioIngresos+BeneficioPuntaje
print(f'Su descuento total a recibir de matrícula es: {BeneficioTotal}%')






