# Ejercicio de triangulos N.1: Dados 3 numeros a, b, c, verificar si pueden formar los lados de un triangulo.

#input
print("\n----------------------------------------------------------------------------------------------------------")
print("-----------Para determinar si 3 numeros pueden formar un lado, ingrese los valores para a, b, y c --------")
print("----------------------------------------------------------------------------------------------------------\n")
a=int(input("\n Ingrese el valor de a: "))
b=int(input("\n Ingrese el valor de b "))
c=int(input("\n Ingrese el valor de c "))
print(" ")

#processing 
if a>0 and b>0 and c>0:
    if a+b>c and a+c>b and b+c>a:
        print("\n Los valores ingresados pueden formar un triangulo \n")
    else:
        print("\n Los valores ingresados NO pueden formar un triangulo \n")
else:
    print("\n Los valores ingresados NO pueden formar un triangulo, uno de ellos es menor o igual a cero \n")