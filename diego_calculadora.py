

try:  #<-----Inicio excepcion-------------------------------------------------------------------------------------------------
    while True:
        opciones = 0; #<-----Variable repeticion menu inicial
        while opciones == 0:
            print("----------------Bienvenido--------------");
            print("----------------Calculadora-------------");
            print("  [1] Sumar\n  [2] Restar\n  [3] Multiplicar\n  [4] Dividir\n  [5] par - Impar\n  [6] Factorial\n  [7] Salir");
            opciones = int(input("  ingrese una opcion: "));
            if opciones >= 7 and opciones <= 0:
                print("Selecciono una opcion invalida");
            else:
                break;

        match opciones: #<------ inicio menu opciones con match --------------------------------------------------------------------------------------------
            case 1: #SUMADOR ----------------------------------------------------------------------------------------------------------------------------------------
                opc_suma = 0;  #<------ variable repeticion Sumador
                while opc_suma != 2:
                    total_suma = 0; #<------ variable acumuladora suma
                    numero_suma = int(input("Ingrese cuantos numeros desea sumar: "));
                    if numero_suma >= 0:
                        for sumador in range(numero_suma): #<------ inicio de "for" sumador
                            numeros_suma = float(input(f"Numero {sumador + 1}:\n "));
                            total_suma += numeros_suma;
                        print (f"El resultado es: {total_suma}");
                    else: 
                        print("Error, la cantidad de numeros no puede ser negativa"); #<------ manejo error cantidad negativa de numeros a sumar
                        
                    opc_suma = int(input("¿Desea Volver a sumar?\n [1] Si\n [2] No\n ")); #<----- opcion repetidora de sumador
                    if opc_suma == 1:
                        continue;
                    else:
                        print("****Sumador Finalizado****");
                    break;
            case 2: #RESTADOR -------------------------------------------------------------------------------------------------------------------------------------
                opc_resta = 0;  #<------ variable repeticion Restador
                while opc_resta != 2:
                    total_resta = 0; #<------ variable acumuladora Resta
                    numero_resta = int(input("Ingrese cuantos numeros desea Restar: "));
                    if numero_resta > 0:
                        total_resta = float(input("Numero 1: "));
                        for restador in range(1, numero_resta): #<------ inicio de "for" Restador
                            numeros_resta = float(input(f"Numero {restador + 1}: "));
                            total_resta -= (numeros_resta);
                        print (f"El resultado es: {total_resta}");
                    else: 
                        print("Error, la cantidad de numeros no puede ser negativa"); #<------ manejo error cantidad negativa de numeros a sumar
                        
                    opc_resta = int(input("¿Desea Volver a restar?\n [1] Si\n [2] No\n ")); #<----- opcion repetidora de sumador
                    if opc_resta == 1:
                        continue;
                    else:
                        print("****Restador Finalizado****");
                    break
            case 3: # MULTIPLICACION ----------------------------------------------------------------------------------------------------------------------
                opc_multiplicador = 0;  #<------ variable repeticion multiplicador
                while opc_multiplicador != 2:
                    total_multiplicacion = 1 #<------ variable acumuladora multiplicador , inicia en 1 pues en 0 da 0.
                    numero_multiplicacion = int(input("Ingrese cuantos numeros desea multiplicar: "));
                    if numero_multiplicacion >= 0:
                        for multiplicador in range(numero_multiplicacion): #<------ inicio de "for" multiplicador
                            numeros_multiplicador = float(input(f"Numero {multiplicador + 1}:\n "));
                            total_multiplicacion *= numeros_multiplicador;
                        print (f"El resultado es: {total_multiplicacion}");
                    else: 
                        print("Error, la cantidad de numeros no puede ser negativa"); #<------ manejo error cantidad negativa de numeros
                        
                    opc_multiplicador = int(input("¿Desea Volver a multiplicar?\n [1] Si\n [2] No\n ")); #<----- opcion repetidora de sumador
                    if opc_multiplicador == 1:
                        continue;
                    else:
                        print("****multiplicador Finalizado****");
                    break
            case 4: # DIVISION -----------------------------------------------------------------------------------------------------------------------
                opc_division = 0;  #<------ variable repeticion division
                while True:
                    try:
                        divisor = int(input("Ingrese un divisor: "));
                        dividendo = int(input("Ingrese un dividendo: "));
                        resultado = divisor/dividendo;
                        
                    except ZeroDivisionError: # Manejo error dividir por 0
                        print("Ha ocurrido un error, no puede dividir por 0", ZeroDivisionError);
                    else:
                        print(f"Su resultado es: {resultado}");
                        
                    opc_division = int(input("¿Desea Volver a Dividir?\n [1] Si\n [2] No\n "));#<----- opcion repetidora de Divisor
                    if opc_division == 1:
                        continue;
                    else:
                        print("****Divisor Finalizado****");
                    break;
            case 5: # PAR O IMPAR -----------------------------------------------------------------------------------------------------------------------
                opc_evaluador = 0;  #<------ variable repeticion division
                while True:
                    evaluador = int(input("Ingrese un numero a evaluar: "));
                    if evaluador % 2 == 0:
                        print(f"El numero: {evaluador} es par ");
                    else:
                        print(f"El numero: {evaluador} es impar ");
                    opc_evaluador = int(input("¿Desea Volver a evaluar un numero?\n [1] Si\n [2] No\n ")); #<----- opcion repetidora de par - impar
                    if opc_evaluador == 1:
                        continue;
                    else:
                        print("**** Par - Impar Finalizado****");
                    break;
            case 6: # FACTORIAL ------------------------------------------------------------------------------------------------------------------------
                opc_factorial = 0;  #<------ variable repeticion factorial
                while opc_factorial != 2:
                    total_factorial = 1; #<------ variable acumuladora factorial , inicia en 1 pues en 0 da 0.
                    numero_factorial = int(input("Ingrese el numero a factorizar: "));
                    for factor in range(1,numero_factorial+1): #<------ inicio de "for" factorial
                        total_factorial *= numero_factorial;
                    print (f"El Factorial de {numero_factorial} es: {total_factorial}");
                    opc_factorial = int(input("¿Desea Volver a calcular el factorial?\n [1] Si\n [2] No\n ")); #<----- opcion repetidora de factorial
                    if opc_factorial == 1:
                        continue;
                    else:
                        print("****Factorial Finalizado****");
                    break;
            case _: #<-------------------Termino menu match ----------------------------------------------------------------------------------------------
                print("Termino calculadora");
                break
except ValueError: #Termino excepcion --------------------------------------------------------------------------------------------------------------------------
    print("Ha ocurrido un error, a ingresado un valor incorrecto", ValueError);
    print("----------------------Calculadora Terminada----------------------");