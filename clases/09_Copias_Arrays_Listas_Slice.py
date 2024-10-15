# Ejemplo de una lista

champions_list = ["Jinx", "Zed", "Ahri", "Dr. Mundo", "Lucian"]
print(champions_list)

# Mirar la referencia en memoria de la lista

print(id(champions_list))

# Copia de una lista con una asignación a una nueva variable

new_champions_list = champions_list
print(new_champions_list)

# Mirar refencia en memoria de la nueva lista

print(id(new_champions_list))

# Modificación la segunda lista, afectan a ambas listas

del new_champions_list[0]

print(new_champions_list)
print(champions_list)

# Creacion de una lista independiente

add_others_champions_list = champions_list[:]
print(add_others_champions_list)

# Mirar la referencia en memoria de todas las lista

print(id(champions_list))
print(id(new_champions_list))
print(id(add_others_champions_list))

# Modificación de la lista independiente 

new_season_champions = ["Aatros", "Ahri", "Akshan"]
add_others_champions_list.extend(new_season_champions)

# Mirar todas las litas

print(champions_list)
print(new_champions_list)
print(add_others_champions_list)

# Mirar la referencia en memoria

print(id(champions_list))
print(id(new_champions_list))
print(id(add_others_champions_list))