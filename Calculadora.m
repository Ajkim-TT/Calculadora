datasource = "CALCULOS";
username = "postgres";
password = "ajkimtepaz";
tablename = "operaciones";
%conn = postgresql(datasource,username,password);
while 1
    try
        opp = input('Ingrese la operación\n1.Suma\n2.Resta\n3.Multiplicacion\n4.División\n5.Salir\n');
        switch opp
            case 1|'S'
                val1 = input('Ingrese el primer sumando ');
                val2 = input('Ingrese el segundo sumando ');
                val3 = val1+val2;
                %valor1 = string(val1);
                %valor2 = string(val2);
                %valor3 = string(val3);
                %sprintf('El valor de la suma es %d', val3)
                %data =5 table("Suma",valor1,valor2,valor3,["operacion" "valor1" "valor2" "resultado"]);
                %sqlwrite(conn,tablename,data);
            case 2
                val1 = input('Ingrese el minuendo ');
                val2 = input('Ingrese el sustraendo ');
                val3 = val1-val2;
                sprintf('El valor de la resta es %d', val3)
            case 3
                val1 = input('Ingrese el primer factor ');
                val2 = input('Ingrese el segundo factor ');
                val3 = val1*val2;
                sprintf('El valor de la multiplicación es %d', val3)
            case 4
                val1 = input('Ingrese el numerador ');
                val2 = input('Ingrese el denominador ');
                val3 = val1/val2;
                sprintf('El valor de la división es %d', val3)
            case 5 
                sprintf('Gracias por utilizar el programa');
                return
        end
    catch
        sprintf('El caracter ingresado no es un numero');
    end 
end