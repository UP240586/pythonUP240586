ages = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Convertir ages a set y comparar longitudes
ages_set = set(ages)
print("Longitud de la lista:", len(ages))
print("Longitud del set:", len(ages_set))
print("¿La lista es más grande?", len(ages) > len(ages_set))

# 2. Diferencias entre tipos de datos
print("\nDiferencias entre tipos de datos:")
print("String: Secuencia inmutable de caracteres, se define con comillas")
print("List: Secuencia mutable ordenada, se define con corchetes []")
print("Tuple: Secuencia inmutable ordenada, se define con paréntesis ()")
print("Set: Colección no ordenada y mutable de elementos únicos, se define con llaves {}")

# 3. Contar palabras únicas en una frase
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print("\nFrase original:", sentence)
print("Palabras únicas:", unique_words)
print("Número de palabras únicas:", len(unique_words))