def conseguirDatos():
        
        nombre=[]
        cedula=[]
        celular=[]
        
        nombre.append(input('Digite el nombre completo del beneficiario a registrar: \n'))
        cedula.append(input('Ingrese el número de cédula del beneficiario a registrar: \n'))
        celular.append(input('Ingrese el número de celular del beneficiario a registrar: \n'))
        archivo=open('agenda.txt','a')
        archivo.write('\n')
        archivo.write(nombre)
        archivo.write('\n')
        archivo.write(cedula)
        archivo.write('\n')
        archivo.write(celular)
        archivo.write('\n')
        archivo.close
