# Ejercicio 7
peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))
imc = peso / (estatura ** 2)
imc_redondeado = round(imc, 2)
print("Tu índice de masa corporal es:", imc_redondeado)
# Ejercicio 8
n = int(input("Introduce el primer número entero (n): "))
m = int(input("Introduce el segundo número entero (m): "))
c = n // m
r = n % m
print(n," entre ",m," da un cociente ",c, "y un restante de ",r)

#Ejercicio 9
cantidad_invertida = float(input("Introduce la cantidad a invertir: "))
interes_anual = float(input("Introduce el interés anual (en porcentaje): "))
numero_anios = int(input("Introduce el número de años: "))
capital_obtenido =round( cantidad_invertida * (1 + interes_anual / 100) ** numero_anios)
capital_formateado = '{:,.2f}'.format(capital_obtenido)
print("El capital obtenido en la inversión es:", capital_formateado)

#Ejercicio 10
payaso=112
muñeca=75
cant_payaso=int(input("Ingrese la cantidad de payasos vendidos:   "))
cant_muñecas=int(input("Ingrese la cantidad de muñecas vendidas:  "  ))
total_peso=(cant_muñecas*muñeca)+(cant_payaso*payaso)
print("El peso total del paquete que sera enviado es de ",total_peso, " grmaos")