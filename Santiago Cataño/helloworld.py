# name = "Santiago"
# age = 23
# isAlive = True
# address = "Avenida Comando"

#HelloWorld = "Hola Mundo"
#print(HelloWorld)

#print(name)
#print(age)
#print(isAlive)
#print(address)

#print(f"Mi nombre es {name}, tengo {age}, años, estoy vivo {isAlive}, gracias a Dios y vivo en {address}")

#print("Santiago" > "santi") da true porque el tipo de dato con mayus es mayor en numero a el tipo de dato santi minus

#Condicionales

# if 20 <= 40:
#     print("Es menor")

# else:
#     print("Es mayor")

#Exercise One

name = "Susana"
name1 = input("¿Cuál es tu nombre? ")
age = int(input("Ingrese su edad: "))
MayorDeEdad = int(input("Ingresa la mayoría de edad de tu país: "))

print(f"Hola, {name1}")
if age >= 18:
    print(f"{name1} Es mayor de edad y tiene {age}")
else: 
    age <= 17
    print(f"{name1} Es menor de edad y tiene {age}")