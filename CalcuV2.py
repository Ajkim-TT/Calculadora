from os import system
import psycopg2

conexion1 = psycopg2.connect("dbname=CALCULOS user=postgres password=ajkimtepaz")
cursor1=conexion1.cursor()

while True:
    try:
        print('Operación Matemática')
        print('1 o "S". Suma')
        print('2 o "R". Resta')
        print('3 o "M". Multiplicación')
        print('4 o "D". División')
        print('5 o "X". Salir')
        Operacion = input()
        Opp = int(Operacion)
        STRI = str(Opp)
        if Opp == 1 or STRI == 'S':
            system("cls")
            print('Se ha seleccionado Suma')
            print('+++++++++++++++++++++++')
            print('Ingrese el primer sumando')
            val1 = input()
            valor1 = float(val1)
            print('Ingrese el segundo sumando')
            val2 = input()
            valor2 = float(val2)
            val3 = valor1 + valor2
            valor1 = str(valor1)
            valor2 = str(valor2)
            valor3 = str(val3)
            print('El resultado de la suma es: ' + valor3)
            sql="insert into operaciones(operacion, valor1, valor2, resultado) values (%s,%s,%s,%s)"
            datos=("Suma",valor1,valor2,valor3)
            cursor1.execute(sql, datos)
            conexion1.commit()
        elif Opp == (2 or 'R'):
            system("cls")
            print('Se ha seleccionado Resta')
            print('------------------------')
            print('Ingrese el minuendo')
            val1 = input()
            valor1 = float(val1)
            print('Ingrese el sustraendo')
            val2 = input()
            valor2 = float(val2)
            val3 = valor1-valor2
            valor1 = str(valor1)
            valor2 = str(valor2)
            valor3 = str(val3)
            print('El resultado de la resta es: ' + valor3)
            sql="insert into operaciones(operacion, valor1, valor2, resultado) values (%s,%s,%s,%s)"
            datos=("Resta",valor1,valor2,valor3)
            cursor1.execute(sql, datos)
            conexion1.commit()
        elif Opp == (3 or 'M'):
            system("cls")
            print('Se ha seleccionado Multiplicación')
            print('*********************************')
            print('Ingrese el primer factor')
            val1 = input()
            valor1 = float(val1)
            print('Ingrese el segundo factor')
            val2 = input()
            valor2 = float(val2)
            val3 = valor1*valor2
            valor1 = str(valor1)
            valor2 = str(valor2)
            valor3 = str(val3)
            print('El resultado de la multiplicacion es: ' + valor3)
            sql="insert into operaciones(operacion, valor1, valor2, resultado) values (%s,%s,%s,%s)"
            datos=("Multiplicacion",valor1,valor2,valor3)
            cursor1.execute(sql, datos)
            conexion1.commit()
        elif Opp == (4 or 'D'):
            system("cls")
            print('Se ha seleccionado Division')
            print('///////////////////////////')
            print('Ingrese el numerador')
            val1 = input()
            valor1 = float(val1)
            print('Ingrese el denominador')
            val2 = input()
            valor2 = float(val2)
            
            if valor2 == 0:
                valor1 = str(valor1)
                print('El resultado de la division es: infinito')
                sql="insert into operaciones(operacion, valor1, valor2, resultado) values (%s,%s,%s,%s)"
                datos=("Resta",valor1,"0","Infinito")
                cursor1.execute(sql, datos)
                conexion1.commit()
            else:
                val3 = valor1/valor2
                valor1 = str(valor1)
                valor2 = str(valor2)
                valor3 = str(val3)
                print('El resultado de la division es: ' + valor3)
                sql="insert into operaciones(operacion, valor1, valor2, resultado) values (%s,%s,%s,%s)"
                datos=("Multiplicacion",valor1,valor2,valor3)
                cursor1.execute(sql, datos)
                conexion1.commit()
        elif Opp == (5 or 'X'):
            system("cls")
            print('Gracias por usar nuestro programa')
            exit()
  
    except ValueError:
        print("ESE NO ES UN NUMERO. PILLO")
