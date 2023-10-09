class Base:
    def __init__(self, letra='unaLetra', valorV=0):
        self._letra = letra
        self._valorV = valorV

    def getLetra(self):
        return self._letra

    def setLetra(self, letra):
        self._letra = letra

    def getValorV(self):
        return self._valorV

    def setValorV(self, valorV):
        self._valorV = valorV

    def __str__(self):
        texto = self.getLetra() + ' --> ' + str(self.getValorV()) + '    '
        return texto


class Secuencia:
    def __init__(self, listaRecibidaBases=[], identificador='sinNombre', descripcion='sinDescripcion'):
        self._listaRecibidaBases = listaRecibidaBases
        self._identificador = identificador
        self._descripcion = descripcion

    def getListaRecibidaBases(self):
        return self._listaRecibidaBases

    def getIdentificador(self):
        return self._identificador

    def setIdentificador(self, identificador):
        self._identificador = identificador

    def getDescripcion(self):
        return self._descripcion

    def setDescripcion(self, descripcion):
        self._descripcion = descripcion

    def __str__(self):
        texto = 'La secuencia es: '
        for base in range(len(self.getListaRecibidaBases())):
            texto = texto + str(self.getListaRecibidaBases()[base])
        texto = texto + '\n' + 'El identificador de la secuencia es: ' + self.getIdentificador() + '\n' + 'La descripción de la secuencia es: ' + self.getDescripcion()
        return texto


# MENU

listaMenu = ['Terminar el programa', 
             'Ingresar una base al sistema', 
             'Ingresar una secuencia', 
             'Ver las secuencias',
             'Ver las bases', 
             'Elegir la secuencia', 
             'Mostrar secuencia seleccionada',
             'Exportar la secuencia seleccionada a formato FASTQ',
             'Validar un archivo FASTQ',
             'Ver secuencias registradas las cuales contengan una base cuyo valor V supere al valor dado']
listaBases = []
listaSecuencias = []
basesCorrectas = ['A', 'T', 'C', 'G', 'U']

salir = False
while not salir:

    for n in range(len(listaMenu)):
        print(f'Opción {n}) {listaMenu[n]}')
    print('\n')
    opcion = int(input('Por favor, ingrese una opción: '))

    if opcion == 0:
        salir = True

    elif opcion == 1:   # Agregar una base
        letraBase = input('Ingrese la letra correspondiente a la base: ')
        valorV = int(input('Ingrese el valor V correspondiente a la base: '))
        unaBase = Base(letraBase, valorV)

        if valorV < 1 or valorV > 100:  # Verifico que el valor V sea el correcto
            print('Error: el valor V que usted ingresó no se encuentra en el rango válido')
        elif letraBase not in basesCorrectas:
            print('Usted ha ingresado una base inválida, las bases correctas son: A, T, C, G o U')
        elif unaBase in listaBases:
            print('Error: la base que usted ingresó ya se encuentra en el sistema')
        else:
            print('Base válida')
            listaBases.append(unaBase)
        print('\n')
        
    elif opcion == 2:   # Agregar una secuencia
        listaAuxiliarBases = []
        if not listaBases:
            print('No hay bases ingresadas al sistema hasta el momento')
        else:
            salida = False
            esta = True
            while esta:  # cuando el identificador existe entra de nuevo al while, esta=True
                esta = False
                identificador = input('Ingrese el identificador único de la secuencia deseada: ')
                for secu in range(len(listaSecuencias)):
                    if identificador == listaSecuencias[secu].getIdentificador():
                        esta = True
                if esta:
                    print('El identificador ya existe')
            descripcion = input('Ingrese la descripción que desee para su secuencia: ')
            while not salida:
                for n in range(len(listaBases)):
                    print(f'{n}) {listaBases[n]}')
                print('Escriba un negativo para salir\n')
                opcionBase = int(input('Ingrese la opción correspondiente a la base que desea para su secuencia: '))
                if opcionBase < 0:
                    salida = True
                else:
                    letraBase = listaBases[opcionBase]
                    listaAuxiliarBases.append(letraBase)
            unaSecuencia = Secuencia(listaAuxiliarBases, identificador, descripcion)
            listaSecuencias.append(unaSecuencia)


                
    elif opcion == 3:  # Ver las secuencias
        if not listaSecuencias:
            print('No hay secuencias ingresadas al sistema hasta el momento')
        else:
            for n, secuencia in enumerate(listaSecuencias):
                print(f'{n}) {secuencia}')
            print('\n')



    elif opcion == 4:  # Ver lista de bases
        if not listaBases:
            print('No hay bases ingresadas al sistema hasta el momento')
        else:
            for n, base in enumerate(listaBases):
                print(f'{n}) {base}')
            print('\n')



    elif opcion == 5:  # elegir secuencia
        if not listaSecuencias:
            print('No hay secuencias ingresadas al sistema hasta el momento\n')
        else:
            for n, secuencia in enumerate(listaSecuencias):
                print(f'{n}) {secuencia}')
            posicionElegida = int(input('Ingrese la posición de la secuencia con la que desea trabajar: '))
            print('\n')
            secuenciaElegida = listaSecuencias[posicionElegida]



    elif (opcion == 6):       #mostrar secuencia seleccionada
        if (listaSecuencias == []):
            print ('No hay secuencias ingresadas al sistema hasta el momento' + '\n')
        else:
            try:
                print ('Su secuencia seleccionada es: ' + str (secuenciaElegida) + '\n')
            except:
                print ('No hay ninguna secuencia seleccionada, para seleccionar una secuencia ingrese 5' + '\n')
                

    elif (opcion == 7):              # secuencia elegida a FASTQ
        try:
            nombreArchivo = raw_input ('Ingrese la ruta y el nombre que desee que se ubique su archivo: ')
            archivo = open (nombreArchivo, 'w')
            #1era linea:
            archivo.write ('@' + secuenciaElegida.getIdentificador() + '|' + secuenciaElegida.getDescripcion() + '\n')  
            #2da linea:
            for letra in range (len (secuenciaElegida.getListaRecibidaBases() ) ):  
                archivo.write (secuenciaElegida.getListaRecibidaBases()[letra].getLetra() )
            archivo.write ('\n')
            #3era linea:
            archivo.write ('+' + secuenciaElegida.getIdentificador() + '|' + secuenciaElegida.getDescripcion() + '\n')  
            #4ta linea:
            for base in range (len (secuenciaElegida.getListaRecibidaBases() ) ):  
                valorV = secuenciaElegida.getListaRecibidaBases()[base].getValorV()
                print (valorV)
                q = chr (valorV + 33)
                archivo.write (q)
            archivo.close()
            print ('La operación ha sido realizada con éxito' + '\n')
        except:
            print ('No hay ninguna secuencia seleccionada, para seleccionar una secuencia ingrese 5' + '\n')


    elif (opcion == 8):        
        try:        # con el try verifico que el archivo exista, sino existe va a haber un error y se va al except
            nroLineas = 0
            letrasInvalidas = 0
            condicion1 = False
            condicion2 = False
            condicion3 = False
            condicion4 = False
            rutaArchivo = input ('Ingrese la ruta y el nombre correspondiente al archivo que desea validar: ')

            archivo8 = open (rutaArchivo, 'r')    
            print ('El archivo existe')
            for linea in archivo8:               # Cuento el nro de lineas del archivo
                nroLineas = nroLineas+1
            archivo8.close()

            archivo8 = open (rutaArchivo, 'r')
            linea1 = archivo8.readline()
            linea2 = archivo8.readline()
            linea3 = archivo8.readline()
            linea4 = archivo8.readline()
            archivo8.close()
            
            archivo8 = open (rutaArchivo, 'r')
            for letra in range (len(linea2)-1):
                if (linea2[letra] not in basesCorrectas):
                    letrasInvalidas = letrasInvalidas + 1
            archivo8.close()
                    
            if (nroLineas == 4):
                condicion1 = True
                print ('El archivo tiene 4 lineas')
            if (linea1[0] == '@' in linea1):
                condicion2 = True
                print ('La primer linea del archivo comienza con un @')
            if (letrasInvalidas == 0): 
                condicion3 = True
                print ('El archivo contiene bases válidas')            
            if (len (linea4) == len (linea2)-1):   
                condicion4 = True
                print ('El archivo contiene la misma cantidad de bases que de valores q' + '\n')
            if (condicion1 == True and condicion2 == True and condicion3 == True and condicion4 == True):
                print ('Conclusión: El formato es correcto' + '\n')
            else:
                print ('Conclusión: El formato NO es correcto ya que no cumple con los 4 requisitos para que sea así' + '\n')

        except:
            print ('Error, por favor, verifique que la ruta del archivo sea la correcta' + '\n')
            
            
    elif (opcion == 9):       # mostrar las secuencias las cuales tengan una base (o más) con un valor V mayor al valor dado
        listaSecuenciasMayores = []
        if (listaSecuencias == []):
            print ('No hay secuencias ingresadas al sistema hasta el momento' + '\n')
        else:
            valor = int (input ('Ingrese un valor: '))
            print ('\n')
            for sec in range (len (listaSecuencias)):
                for base in range (len(listaSecuencias[sec].getListaRecibidaBases() )): 
                    if (listaSecuencias[sec].getListaRecibidaBases()[base].getValorV() > valor):
                        if (listaSecuencias[sec] not in listaSecuenciasMayores):   #pongo este if xa asegurarme de que no agregue mas de una vez a la misma secuencia
                            listaSecuenciasMayores.append(listaSecuencias [sec])
            if (listaSecuenciasMayores == []):
                print ('No hay secuencias con la característica pedida' + '\n')
            else:
                for n in range (len(listaSecuenciasMayores)):
                    print ( str(listaSecuenciasMayores[n]) + '\n')
                

    else:
        print ('\n' + 'Opción no válida' + '\n')


