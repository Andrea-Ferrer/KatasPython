#Ejercicio1


# Crear variables para almacenar las dos distancias
# ¡Asegúrate de quitar las comas!

first_planet = 149597870
second_planet = 778547200



# Calcular la distancia entre planetas

distance_km = second_planet - first_planet
print(distance_km)

distance_mi = distance_km * 0.621
print(distance_mi)


#Ejercicio 2

# Almacenar las entradas del usuario
first_planet = input('Introduzca la distancia del sol para el primer planeta en KM')
second_planet = input('Introduzca la distancia desde el sol para el segundo planeta en KM')

# Convierte las cadenas de ambos planetas a números enteros
first_planet = int(first_planet)
second_planet = int(second_planet)

# Realizar el cálculo y determinar el valor absoluto
distance_km = second_planet - first_planet
print(distance_km)

# Convertir de KM a Millas
distance_mi = distance_km * 0.621
print(abs(distance_mi))