nombre = "Marco"
apellido = "Cruz"
edad = 18
ciudad = "Mexico"
print("Datos:")
print(f"Nombre: {type(nombre)}")
print(f"Apellido: {type(apellido)}")
print(f"Edad: {type(edad)}")
print(f"ciudad: {type(ciudad)}")
print()
print("Longitud del nombre:", len(nombre))
print("name longer than last name:", len(nombre) > len(apellido))
print()
num1 = 2
num2 = 7

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
residuo = num2 % num1
exp = num1 ** num2
floor_division = num1 // num2

print("Total:", suma)
print("Difference:", resta)
print("Producto:", multiplicacion)
print("Division:", division)
print("Residuo:", residuo)
print("Exponencial:", exp)
print("Floor Division:", floor_division)
print()
R = 20
pi = 3.1416
Perimetro = R*2
area_del_curculo = pi*(R**2)
print(area_del_curculo)
print()
circunferencia_del_circulo = pi*Perimetro
print(circunferencia_del_circulo)
print()
# 13-14
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
pais = input("Ingrese su país: ")
edad = int(input("Ingrese su edad: "))  

print("\nDatos del usuario:")
print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")
print(f"País: {pais}")
print(f"Edad: {edad}")