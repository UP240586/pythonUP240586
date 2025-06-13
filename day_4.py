print("--- 1. Concatenación de Cadenas ---")
cadena1 = "Treinta"
cadena2 = "Días"
cadena3 = "De"
cadena4 = "Python"
resultado1 = cadena1 + " " + cadena2 + " " + cadena3.lower() + " " + cadena4
print(f"El resultado de unir 'Treinta Días De Python' es: {resultado1}")

cadena5 = "Codificación"
cadena6 = "Para"
cadena7 = "Todos"
resultado2 = cadena5 + " " + cadena6 + " " + cadena7
print(f"El resultado de unir 'Codificación Para Todos' es: {resultado2}")
print("\n--- 2. Declaración de Variables y Longitud ---")
empresa = "Codificación para Todos" 
print(f"La variable 'empresa' contiene: '{empresa}'")
print(f"La longitud de la cadena 'empresa' es: {len(empresa)} caracteres")
print("\n--- 3. Manipulación de Mayúsculas y Minúsculas ---")
print(f"En mayúsculas: {empresa.upper()}")
print(f"En minúsculas: {empresa.lower()}")
print(f"Capitalizado: {empresa.capitalize()}")
print(f"En formato título: {empresa.title()}")
print(f"Mayúsculas/Minúsculas invertidas: {empresa.swapcase()}")
print("\n--- 4. Cortar (Slice) y Unir Partes de Cadenas ---")
palabras = empresa.split()
print(f"Las palabras de '{empresa}' son: {palabras}")
sin_primera_palabra = " ".join(palabras[1:])
print(f"Cadena sin la primera palabra: {sin_primera_palabra}")
print("\n--- 5. Búsqueda de Subcadenas ---")
print(f"¿'Codificación' está en '{empresa}'? {'Codificación' in empresa}")
print(f"La posición de 'Codificación' (usando find) es: {empresa.title().find('Codificación')}")
try:
    print(f"La posición de 'Codificación' (usando index) es: {empresa.title().index('Codificación')}")
except ValueError:
    print("La subcadena 'Codificación' no se encontró con .index() (sensible a mayúsculas/minúsculas).")
print("\n--- 6. Reemplazar Palabras ---")
cadena_original = "Coding For All"
nueva_cadena = cadena_original.replace("Coding", "Python")
print(f"'{cadena_original}' reemplazando 'Coding' por 'Python': {nueva_cadena}")

frase1 = "Python for Everyone"
frase1_modificada = frase1.replace("Everyone", "All")
print(f"'{frase1}' reemplazando 'Everyone' por 'All': {frase1_modificada}")
print("\n--- 7. Dividir Cadenas (Split) ---")
frase2 = "Coding For All"
dividida_espacio = frase2.split()
print(f"'{frase2}' dividida por espacios: {dividida_espacio}")

empresas_str = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
divididas_coma = empresas_str.split(", ")
print(f"'{empresas_str}' dividida por comas y espacios: {divididas_coma}")
print("\n--- 8. Acceder a Caracteres por Índice ---")
print(f"El primer carácter de '{frase2}' (índice 0) es: {frase2[0]}")
ultimo_indice = len(frase2) - 1
print(f"El último índice de '{frase2}' es: {ultimo_indice}")
print(f"El último carácter de '{frase2}' es: {frase2[ultimo_indice]}")
print(f"El último carácter (usando -1) es: {frase2[-1]}")
print(f"El carácter en el índice 10 de '{frase2}' es: {frase2[10]}")
print("\n--- 9. Creación de Acrónimos ---")
palabras_py = "Python For Everyone".split()
acronimo_py = "".join([p[0].upper() for p in palabras_py]) 
print(f"Acrónimo de 'Python For Everyone': {acronimo_py}")

palabras_cf = "Coding For All".split()
acronimo_cf = "".join([p[0].upper() for p in palabras_cf])
print(f"Acrónimo de 'Coding For All': {acronimo_cf}")
print("\n--- 10. Encontrar Posiciones de Subcadenas (index, rfind) ---")
print(f"La primera 'C' en '{frase2}' está en el índice: {frase2.index('C')}")
print(f"La primera 'F' en '{frase2}' está en el índice: {frase2.index('F')}")

frase3 = "Coding For All People"
print(f"La última 'l' en '{frase3}' está en el índice (usando rfind): {frase3.rfind('l')}")
print("\n--- 11. Manejo de la palabra 'because' ---")
frase_because = "No se puede terminar una oración con because because because es una conjunción"
posicion_primera_because = frase_because.find("because")
print(f"La primera 'because' está en el índice (usando find): {posicion_primera_because}")
posicion_ultima_because = frase_because.rindex("because")
print(f"La última 'because' está en el índice (usando rindex): {posicion_ultima_because}")
corte_because = frase_because[posicion_primera_because : posicion_primera_because + 23]
print(f"Fragmento 'because because because': '{corte_because}'")
print("\n--- 12. Verificación de Inicio y Fin de Cadenas ---")
cadena_check = "Coding For All"
print(f"¿'{cadena_check}' empieza con 'Coding'? {cadena_check.startswith('Coding')}")
print(f"¿'{cadena_check}' termina con 'coding'? {cadena_check.endswith('coding')}")
print(f"¿'{cadena_check}' (en minúsculas) termina con 'coding'? {cadena_check.lower().endswith('coding')}")
print("\n--- 13. Eliminar Espacios Extra (Strip) ---")
cadena_espacios = '   Codificación Para Todos      '
print(f"Cadena original con espacios: '{cadena_espacios}'")
print(f"Cadena sin espacios extra: '{cadena_espacios.strip()}'")
print("\n--- 14. Validación de Nombres de Variables (isidentifier) ---")
print(f"¿'30DaysOfPython' es un nombre válido de variable? {'30DaysOfPython'.isidentifier()}")
print(f"¿'thirty_days_of_python' es un nombre válido de variable? {'thirty_days_of_python'.isidentifier()}")
print("\n--- 15. Unir Elementos de una Lista ---")
librerias_python = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(f"Librerías unidas con '# ': {' # '.join(librerias_python)}")
print("\n--- 16. Caracteres de Escape ---")
print("Estoy disfrutando este desafío.\nSolo me pregunto qué sigue.")
print("Nombre\tEdad\tPaís\tCiudad")
print("Asabeneh\t250\tFinlandia\tHelsinki")
print("\n--- 17. Formato de Cadenas (f-strings) ---")
radius = 10
area = 3.14 * radius ** 2
print(f"El área de un círculo con radio {radius} es {int(area)} metros cuadrados.")

num1 = 8
num2 = 6
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2:.2f}")
print(f"{num1} % {num2} = {num1 % num2}") 
print(f"{num1} // {num2} = {num1 // num2}") 
print(f"{num1} ** {num2} = {num1 ** num2}") 