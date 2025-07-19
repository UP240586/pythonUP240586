A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Unión de A y B
print("Unión A y B:", A.union(B))

# 2. Intersección de A y B
print("Intersección A y B:", A.intersection(B))

# 3. ¿Es A subconjunto de B?
print("¿A es subconjunto de B?", A.issubset(B))

# 4. ¿Son A y B conjuntos disjuntos?
print("¿A y B son disjuntos?", A.isdisjoint(B))

# 5. Unión de A con B y B con A (es lo mismo)
print("A unión B:", A.union(B))
print("B unión A:", B.union(A))

# 6. Diferencia simétrica entre A y B
print("Diferencia simétrica:", A.symmetric_difference(B))

# 7. Eliminar los conjuntos completamente
del A
del B