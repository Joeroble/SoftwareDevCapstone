# Tuples

city_state = [('Seattle', 'WA'), ('Portland', 'OR'), ('San Francisco', 'CA')]
print(len(city_state))

first_city_state = city_state[0]
print(first_city_state)

print(first_city_state[0])
print(first_city_state[1])

city, state = first_city_state
print(city)

animals = ('lion', 'puma', 'tiger')
print(animals)

lion, puma, tiger = animals
print(tiger)

def get_distance():
    miles = 1000
    km = miles *1.6
    return miles, km

distances = get_distance()    
print(distances[0])

miles, km = get_distance()
print(km)


