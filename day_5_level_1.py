print("--- 1. Lista Vacía ---")
lista_vacia = []
print(f"Lista vacía: {lista_vacia}")
print("\n--- 2. Lista con Más de 5 Ítems ---")
mi_lista = ['manzana', 'banana', 'cereza', 'dátil', 'uva', 'kiwi', 'limón']
print(f"Mi lista: {mi_lista}")
print("\n--- 3. Longitud de la Lista ---")
longitud_lista = len(mi_lista)
print(f"La longitud de mi_lista es: {longitud_lista}")
print("\n--- 4. Ítems Específicos de la Lista ---")
primer_item = mi_lista[0]
item_medio = mi_lista[len(mi_lista) // 2]
ultimo_item = mi_lista[-1]
print(f"Primer ítem: {primer_item}")
print(f"Ítem del medio: {item_medio}")
print(f"Último ítem: {ultimo_item}")
print("\n--- 5. Lista con Tipos de Datos Mixtos ---")
mixed_data_types = ["Tu Nombre", 30, 1.75, "Soltero(a)", "Calle Falsa 123"]
print(f"Lista mixed_data_types: {mixed_data_types}")
print("\n--- 6. Lista de Compañías IT ---")
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(f"Lista it_companies: {it_companies}")
print("\n--- 7. Número de Compañías ---")
print(f"Número de compañías en it_companies: {len(it_companies)}")
print("\n--- 8. Primera, Media y Última Compañía ---")
primera_compania = it_companies[0]
compania_media = it_companies[len(it_companies) // 2]
ultima_compania = it_companies[-1]
print(f"Primera compañía: {primera_compania}")
print(f"Compañía del medio: {compania_media}")
print(f"Última compañía: {ultima_compania}")
print("\n--- 9. Modificar una Compañía ---")
it_companies[0] = 'Meta' # Cambiamos 'Facebook' por 'Meta'
print(f"Lista it_companies después de modificar una: {it_companies}")
print("\n--- 10. Añadir una Compañía IT ---")
it_companies.append('Netflix')
print(f"Lista it_companies después de añadir Netflix: {it_companies}")
print("\n--- 11. Insertar Compañía en el Medio ---")
indice_medio = len(it_companies) // 2
it_companies.insert(indice_medio, 'Intel')
print(f"Lista it_companies después de insertar Intel en el medio: {it_companies}")
print("\n--- 12. Cambiar a Mayúsculas (Excluyendo IBM) ---")
indice_google = it_companies.index('Google') # Encontramos el índice de Google
it_companies[indice_google] = it_companies[indice_google].upper()
print(f"Lista it_companies después de cambiar Google a mayúsculas: {it_companies}")
print("\n--- 13. Unir Compañías con '#; ' ---")
compania_unida = ' #; '.join(it_companies)
print(f"Compañías unidas con '#; ': {compania_unida}")
print("\n--- 14. Verificar Existencia de Compañía ---")
compania_a_buscar = 'Apple'
existe_apple = compania_a_buscar in it_companies
print(f"¿Existe '{compania_a_buscar}' en la lista? {existe_apple}")
compania_no_existente = 'Uber'
existe_uber = compania_no_existente in it_companies
print(f"¿Existe '{compania_no_existente}' en la lista? {existe_uber}")
print("\n--- 15. Ordenar la Lista (sort()) ---")
it_companies.sort()
print(f"Lista it_companies ordenada: {it_companies}")
print("\n--- 16. Invertir la Lista (reverse()) ---")
it_companies.reverse()
print(f"Lista it_companies invertida (descendente): {it_companies}")
print("\n--- 17. Cortar las Primeras 3 Compañías ---")
primeras_3 = it_companies[0:3] # O simplemente it_companies[:3]
print(f"Las primeras 3 compañías son: {primeras_3}")
print("\n--- 18. Cortar las Últimas 3 Compañías ---")
ultimas_3 = it_companies[-3:]
print(f"Las últimas 3 compañías son: {ultimas_3}")
print("\n--- 19. Cortar la(s) Compañía(s) del Medio ---")
medio_inicio = (len(it_companies) - 1) // 2 
medio_fin = len(it_companies) // 2 + 1 
compania_o_companias_medio = it_companies[medio_inicio:medio_fin]
print(f"La(s) compañía(s) del medio es/son: {compania_o_companias_medio}")
print("\n--- 20. Eliminar la Primera Compañía ---")
del it_companies[0] 
print(f"Lista it_companies después de eliminar la primera: {it_companies}")
print("\n--- 21. Eliminar la(s) Compañía(s) del Medio ---")
medio_a_eliminar = len(it_companies) // 2
del it_companies[medio_a_eliminar]
print(f"Lista it_companies después de eliminar la(s) del medio: {it_companies}")
print("\n--- 22. Eliminar la Última Compañía ---")
it_companies.pop() 
print(f"Lista it_companies después de eliminar la última: {it_companies}")
print("\n--- 23. Eliminar Todas las Compañías ---")
it_companies.clear() 
print(f"Lista it_companies después de eliminar todas: {it_companies}")
print("\n--- 24. Destruir la Lista ---")
del it_companies 
try:
    print(it_companies)
except NameError:
    print("La lista 'it_companies' ha sido destruida (eliminada de la memoria).")
print("\n--- 25. Unir Listas (front_end y back_end) ---")
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack_temp = front_end + back_end 
print(f"Lista front_end: {front_end}")
print(f"Lista back_end: {back_end}")
print(f"Listas unidas (temporal): {full_stack_temp}")
print("\n--- 26. Copiar, Insertar Python y SQL ---")
full_stack = full_stack_temp.copy() 
indice_redux = full_stack.index('Redux')
full_stack.insert(indice_redux + 1, 'Python')
full_stack.insert(indice_redux + 2, 'SQL') 
print(f"Lista full_stack final: {full_stack}")
print("\n\n--- Ejercicios: Nivel 2 ---")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(f"Lista original de edades: {ages}")
print("\n--- 1. Ordenar, Min y Max Edad ---")
ages.sort()
print(f"Lista de edades ordenada: {ages}")
min_age = ages[0]
max_age = ages[-1]
print(f"Edad mínima: {min_age}")
print(f"Edad máxima: {max_age}")
print("\n--- 2. Añadir Min y Max a la Lista ---")
ages.append(min_age)
ages.append(max_age)
print(f"Lista de edades con min y max añadidos: {ages}")
ages.sort() 
print(f"Lista de edades re-ordenada: {ages}")
print("\n--- 3. Mediana de las Edades ---")
n = len(ages)
if n % 2 == 1: 
    median_age = ages[n // 2]
else: 
    mid1 = ages[n // 2 - 1]
    mid2 = ages[n // 2]
    median_age = (mid1 + mid2) / 2
print(f"La edad mediana es: {median_age}")
print("\n--- 4. Promedio de las Edades ---")
sum_ages = sum(ages)
average_age = sum_ages / n
print(f"La edad promedio es: {average_age:.2f}") 
print("\n--- 5. Rango de las Edades ---")
range_ages = max_age - min_age
print(f"El rango de las edades es: {range_ages}")
print("\n--- 6. Comparar Diferencias Absolutas ---")
diff_min_avg = abs(min_age - average_age)
diff_max_avg = abs(max_age - average_age)
print(f"|Mínimo - Promedio|: {diff_min_avg:.2f}")
print(f"|Máximo - Promedio|: {diff_max_avg:.2f}")
if diff_min_avg == diff_max_avg:
    print("La diferencia absoluta entre (min - promedio) y (max - promedio) es igual.")
elif diff_min_avg < diff_max_avg:
    print("La diferencia absoluta entre (min - promedio) es menor que (max - promedio).")
else:
    print("La diferencia absoluta entre (min - promedio) es mayor que (max - promedio).")
print("\n--- 7. País(es) del Medio ---")
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
num_countries = len(countries)
if num_countries % 2 == 1: 
    middle_country = countries[num_countries // 2]
    print(f"País del medio: {middle_country}")
else:
    middle_country1 = countries[num_countries // 2 - 1]
    middle_country2 = countries[num_countries // 2]
    print(f"Países del medio: {middle_country1}, {middle_country2}")
print("\n--- 8. Dividir Lista de Países ---")
first_half_len = (num_countries + 1) // 2 
first_half_countries = countries[:first_half_len]
second_half_countries = countries[first_half_len:]
print(f"Primera mitad de países: {first_half_countries}")
print(f"Segunda mitad de países: {second_half_countries}")
print("\n--- 9. Desempaquetar Países ---")
country1, country2, country3, *scandic_countries = countries
print(f"Primer país: {country1}")
print(f"Segundo país: {country2}")
print(f"Tercer país: {country3}")
print(f"Países nórdicos (scandic_countries): {scandic_countries}")