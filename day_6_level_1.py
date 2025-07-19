empty_tuple = tuple()

brotherstpl = ('Erick', 'Alejandro', 'Pedro', 'Daniel', 'Rene', 'Sergio' )
sisterstpl = ('Cinthya', 'Karen', 'Pilar')

siblingstpl = brotherstpl + sisterstpl
print(siblingstpl)

print('Tengo ', len(siblingstpl), ' hermanos y hermanas en total')

parentstpl = ('Hector', 'Candy')
family_memberstpl = siblingstpl + parentstpl
print(family_memberstpl)
del family_memberstpl

fruitptl = ('Strawberry', 'Banana', 'Mango', 'Pineapple', 'Apple', 'Orange')
vegetablestpl = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animalProductstpl = ('Jam', 'Sausage', 'Milk', 'Chesse', 'Cream', 'Meat')

foodStuffTpl = fruitptl + vegetablestpl + animalProductstpl

print(foodStuffTpl[0:8] + foodStuffTpl[9:])
print(foodStuffTpl[3:-3])

del foodStuffTpl
print ('La fruta banana esta en el tuple (Fruits)? ','Banana' in fruitptl)

nordicCountries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia es un pais Nordico? ', 'Estonia' in nordicCountries)
print('Iceland es un pais Nordico? ', 'Iceland' in nordicCountries)
#REVISADO
print("Revisado")