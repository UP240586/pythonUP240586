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