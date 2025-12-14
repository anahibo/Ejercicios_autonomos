#Ejercicio 1
"""meta = float(input("Ingrese una cantidad meta:"))
total = 0
while total < meta:
    monto = float(input("Ingrese un monto:"))
    total += monto
print (total)"""

#Ejercicio 2
"""num = int(input("Ingrese un número:"))
while num <=42:
    num = int (input("Ingrese un número:"))
print ("El número es mayor a 42 =), ",num)"""

#Ejercicio 3
"""import random
numsecret = random.randint(1, 100)
num = int(input("Ingrese un número:"))
while num != numsecret:
    if num < numsecret:
        print ("El número es mayor")
    else:
        print ("El número es menor:")
    num = int(input("Ingrese un número:"))

print ("Adivinaste el número!!!")"""

#Ejercicio 4
num = int (input("Ingrese un número entre 1 y 10:"))
while num < 1 or num >10:
    num = int(input("Error.Ingrese un número entre 1 y 10:"))
print ("Numero valido", num)