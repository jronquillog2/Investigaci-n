def Menu():

 print ("""************
Calculadora
************
Menu
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Exponente
6) Valor absoluto
7) Circunferencia
8) Area Circulo
9) Area Cuadrado
10) Salir""")
def Calculadora():

    Menu()
    opc = int(input("Selecione Opcion:\n"))
    while (opc >0 and opc <6):
        x = int(input("Ingrese el primer Numero\n"))
        y = int(input("Ingrese el segundo Numero\n"))

        if (opc==1):
            print ("La Suma es:", x+y)
            opc = int(input("Selecione Opcion\n"))

        elif(opc==2):
            print ("La Resta es:",x-y)
            opc = int(input("Selecione Opcion\n"))

        elif(opc==3):
            print ("La Multiplicacion es:",x*y)
            opc = int(input("Selecione Opcion\n"))

        elif(opc==4):
            print ("La Division es:", x/y)
            opc = int(input("Selecione Opcion\n"))

        elif(opc==5):
            print("el resultado es: ",x**y)
            opc = int(input("Selecione Opcion\n"))

    while (opc > 5 and opc < 10):
        x = int(input("Ingrese el Numero\n"))

        if (opc==6):
            n= abs(x)
            print("el valor absoluto de ",x,"es:",n)
            opc = int(input("Selecione Opcion\n"))

        elif (opc==7):
            print('Valor de la circunferencia: ',x*3.1416)
            opc = int(input("Selecione Opcion\n"))

        elif (opc==8):
            print('Valor de area: ',3.1416 * x * x)
            opc = int(input("Selecione Opcion\n"))
            
        elif (opc==9):
            print('Valor de area: ', x*x)
            opc = int(input("Selecione Opcion\n"))

Calculadora()

