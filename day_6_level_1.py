# 1. Crear una tupla vacía
empty_tuple = ()
print("Tupla vacía:", empty_tuple)

# 2. Crear tuplas de hermanos y hermanas
brothers = ('Juan', 'Carlos', 'Miguel')
sisters = ('Ana', 'María', 'Lucía')
print("Hermanos:", brothers)
print("Hermanas:", sisters)

# 3. Unir las tuplas en siblings
siblings = brothers + sisters
print("Todos los hermanos:", siblings)

# 4. Contar cuántos hermanos hay
num_siblings = len(siblings)
print("Número de hermanos:", num_siblings)

# 5. Modificar siblings y añadir padres
parents = ('Pedro', 'Laura')
family_members = siblings + parents
print("Miembros de la familia:", family_members)