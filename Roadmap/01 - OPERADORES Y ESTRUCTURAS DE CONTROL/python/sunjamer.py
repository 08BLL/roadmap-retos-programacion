"""
operadores
"""

# operadores aritméticos

print ("aqui operadors")

print(f"Suma 10 + 3 = {10 + 3}")
print(f"resta 8 - 4 = {8 - 4}")
print(f"multiplicar 2 * 10 = {2 * 10}")
print(f"división de 14 / 5 = {14 / 5}")
print(f"módulo de 14 / 5 = {14 % 5}")
print(f"exponente de 2 ** 5 = {2 ** 5}")
print(f"division entera 14 // 5 = {14 // 5}")

# operadores de comparación

print(f"igualdad 8 == 4 es {8 == 4}")
print(f"es diferente 14 != 5 = {14 != 5}")
print(f"es 14 > 5 {14 > 5}")
print(f"es 14 < 5 {14 < 5}")
print(f"es 14 >= 5 {14 >= 5}")
print(f"es 14 <= 5 {14 <= 5}")


# operadores logicos

print(f"AND es 7 + 5 = 12 and 9 - 6 == 3 {7 + 5 == 12 and 9 - 6 == 3}")
print(f"OR es 7 + 5 = 12 OR 9 - 6 == 4 {7 + 5 == 12 or 9 - 6 == 4}")
print(f"NOT 7 + 5 = 12 or 9 - 6 == 3 {not (9 + 6 == 3 or 7 + 5 == 12)}")

# operadores de asignación
print ("aqui asignacion")
my_variable = 33   # asignación de valor a variable
print(my_variable)
my_variable+=3
print(my_variable)
my_variable-=8
print(my_variable)
my_variable*=3
print(my_variable)
my_variable/=2
print(my_variable)
my_variable%=2
print(my_variable)
my_variable//=1
print(my_variable)
my_variable=0b01000
my_variable&=0b10101
print(bin(my_variable))
my_variable|=0b01100
print(bin(my_variable))
my_variable|=0b0101
print(bin(my_variable))

# operadores de comparación

my_variable = 7
print (7 > 5)
print (7 >= 5)
print (7 < 5)
print (7 > 5)
print (7 <= 5)
print (7 == 5)
print (7 != 5)


# estructuras de control

# while

index = 0
while index <= 10:
    if index == 5 or index == 7:
        index+=1
        continue
    print (index)
    index+=1




# for

my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in my_numbers:
    print (number)

print ("salimos del for")

lenguaje = "Python"
for letra in lenguaje:
    print (letra)
print ("salimos del segundo for")











# ejercicios
"""
my_age = 46
my_weight = 70.3
my_complex_variable = 5j+1

print("Entra la base del triangulo")
base = int(input ())
print("Entra la altura del triangulo")
height = int(input())
area = 0.5*base*height
print(f"El area del triangulo es {area}")

"""



