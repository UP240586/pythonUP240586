it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Longitud del set it_companies
print("Longitud de it_companies:", len(it_companies))

# 2. Añadir 'Twitter' a it_companies
it_companies.add('Twitter')
print("Después de añadir Twitter:", it_companies)

# 3. Insertar múltiples compañías a la vez
new_companies = {'LinkedIn', 'Netflix', 'Tesla'}
it_companies.update(new_companies)
print("Después de añadir múltiples compañías:", it_companies)

# 4. Eliminar una compañía
it_companies.remove('IBM')
print("Después de eliminar IBM:", it_companies)

# 5. Diferencia entre remove y discard
try:
    it_companies.remove('IBM')  # Esto lanzará un error ya que IBM ya no está
except KeyError:
    print("remove() lanza un error si el elemento no existe")

it_companies.discard('IBM')  # Esto no lanza error aunque IBM no exista
print("discard() no lanza error si el elemento no existe")