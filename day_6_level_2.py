# 1. Desempaquetar siblings y parents
brothers = ('Juan', 'Carlos', 'Miguel')
sisters = ('Ana', 'María', 'Lucía')
siblings = brothers + sisters
father = 'Pedro'
mother = 'Laura'
family_members = siblings + (father, mother)
print(family_members)
*siblings, father, mother = family_members
print("\nDesempaquetado:")
print("Hermanos:", siblings)
print("Padre:", father)
print("Madre:", mother)

# 2. Crear tuplas de alimentos
fruits = ('manzana', 'banana', 'naranja')
vegetables = ('zanahoria', 'espinaca', 'brócoli')
animal_products = ('leche', 'huevos', 'carne')

# 3. Unir las tuplas de alimentos
food_stuff_tp = fruits + vegetables + animal_products
print("\nComida (tupla):", food_stuff_tp)

# 4. Convertir la tupla a lista
food_stuff_lt = list(food_stuff_tp)
print("Comida (lista):", food_stuff_lt)

# 5. Obtener el/los elementos del medio
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 1:
    middle_item = food_stuff_lt[middle_index]
    print("Elemento del medio:", middle_item)
else:
    middle_items = food_stuff_lt[middle_index-1:middle_index+1]
    print("Elementos del medio:", middle_items)

# 6. Primeros y últimos tres elementos
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("Primeros tres:", first_three)
print("Últimos tres:", last_three)

# 7. Eliminar la tupla food_stuff_tp
del food_stuff_tp
try:
    print(food_stuff_tp)
except NameError:
    print("La tupla food_stuff_tp ha sido eliminada correctamente")

# 8. Verificar si elementos están en tupla
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("\n¿Estonia es un país nórdico?", 'Estonia' in nordic_countries)
print("¿Islandia es un país nórdico?", 'Iceland' in nordic_countries)