it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print('Las cantidad de compañias en it_commpanies es de: ', len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Intel', 'Nvidia', 'Amd', 'Radeon'])
print(it_companies)

it_companies.remove('Apple')
print(it_companies)

it_companies.remove('Amd')
it_companies.add('Qualcomm')
it_companies.remove('Qualcomm')
it_companies.discard('Samsung')
print(it_companies)

'''
this should give us an error and thats because we don´t have Qualcomm in the list
And here we don´t have any problem because discar is like an if
if we have samsung in the list discard discard it but in another
way it don´t give us an error
'''

A.update(B)
print(A)

print(B.intersection(A))

print('un set puede ser un set o subset o superset')

print(A.issubset(B))

print(A.isdisjoint(B))

A.update(B)
B.update(A)

print('La diferencia entre A y B es: ', A.difference(B))
print('La diferencia entre B y A es: ', B.difference(A))
print('La cantidad de edades es de: ', len(age))
print('La edad maxima es de: ', max(age))
print('La edad minima es de: ', min(age))

'''
Una string o cadena solo puede contener una palabra y que esta no se puede cambiar 
Una lista ya puede contener mas cadenas por asi decirlo y a su vez a esta se le puede quitar y agregar
contenido
Y En tuple no podemos modificarla y esta como las 2
y los set pueden estar ordenados como desordenados y se pueden acoplar a otros sin necesidad de que se
repitan strings
'''

phrace = 'Use', 'the', 'split', 'methods', 'and', 'set', 'to', 'get', 'the', 'unique', 'words'

uniquewords = set(phrace)

print('Las palabras unicas son: ', len(uniquewords))

print("revisado")