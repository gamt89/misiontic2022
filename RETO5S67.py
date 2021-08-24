
def estrellas():
    print('*****************************************************************************')

import re

#TÍTULO DEL PROGRAMA
print('')
estrellas()
print('')
print('BIENVENIDO A LA AGENDA DE BENEFICIARIOS DEL PROYECTO MINTIC')
print('')
estrellas()
print('')

def crearArchivo():
    archivo=open('agenda.txt','w')
    archivo.close()

def conseguirDatos():
    nombre = input('Digite el nombre completo del beneficiario a registrar: \n')
    cedula = input('Ingrese el número de cédula del beneficiario a registrar: \n')
    celular = input('Ingrese el número de celular del beneficiario a registrar: \n')
    paquete=[nombre,cedula,celular]
    archivo=open('agenda.txt','a')
    archivo.write('\n')
    archivo.write(nombre)
    archivo.write('\n')
    archivo.write(cedula)
    archivo.write('\n')
    archivo.write(celular)
    archivo.write('\n')
    archivo.close

    return nombre, cedula, celular, paquete, archivo

def buscar():
    option2='Si'
    while option2=='Si':
        #datos=conseguirDatos()
        try:
            palabra=input('Desea realizar la búsqueda de algún beneficiario? (Escriba "Si" en caso de desearlo): ')
            with open('/Users/guillermoandresmolina/Python Tareas/agenda.txt','r',encoding='utf-8') as texto:
                for x in texto:
                    buscar=re.search(palabra,x)
                    print(buscar)
            if buscar:
                print('La palabra', palabra, 'ha sido encontrada.')

            else:
                print('La palabra', palabra, 'no ha sido encontrada.')
        
        except FileNotFoundError:
            print('El archivo no existe.')

        option2=input('Desea realizar más búsquedas de otros beneficiarios? (Escriba "Si" en caso de desearlo): ')



option='Si'

while option=='Si':
    datos=conseguirDatos()
    
    print("------------------------------------------------")

    busqueda=buscar()

    print("------------------------------------------------")





    option = input('Desea realizar más registros para otros beneficiarios? No debe haber otro beneficiario con la misma cédula (Escriba "Si" en caso de desear ingresar más datos): ')


estrellas()
print("¡MUCHÍSIMAS GRACIAS POR USAR NUESTRO SISTEMA!")
estrellas()







