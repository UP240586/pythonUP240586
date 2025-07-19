print('Ejercicio 1')

dogdct = {}  
print(dogdct)

print('Ejercicio 2')

dogdct ['Name'] = 'Jake'
dogdct ['Color'] = 'Yellow'
dogdct ['Breed'] = 'Bulldog England'
dogdct ['Legs'] = '4'
dogdct ['Age'] = '34'
print(dogdct)

print('Ejercicio 3')

studentdct = {
    'First name': 'Leonardo',
    'Last name': 'Zamora',
    'Gender': 'male',
    'Age': '19',
    'Material Status': 'Single',
    'Skills': ['Beginer in cybersecutity', 'Beginer in python', 
    'Support and maintenance technician', 'B1 basic in english'],
    'Address': {'State':'Aguascalientes', 
                'City': 'Ags', 
                'Neighborhood': 'Mision de Santa Fe',
                'Street':'Estrella 456'}
}
print(studentdct)

print('Ejercicio 4')

print(len(studentdct))

print('Ejercicio 5')

print(studentdct.get('Skills'))

print('Ejercicio 6')

studentdct['Skills'].extend(['Autodidact', 'Smart'])
print(studentdct)

print('Ejercicio 7')

studntkeys = studentdct.keys()
print(studntkeys)

print('Ejercicio 8')

studentvalues = studentdct.values()
print(studentvalues)

print('Ejercicio 9')

studentlist = studentdct.items()
print(studentlist)

print('Ejercicio 10')

del studentdct['Skills']
print(studentdct)

print('Ejercicio 11')

del dogdct
print(dogdct)

print("revisado")