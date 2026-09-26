weather = [
    {"Mumbai": [31, 29, 30]},{"Delhi": [34, 33, 32]},{"Ahmedabad": [34, 33, 34]},{"Bengaluru": [32, 30, 29]},
    {"Pune": [30, 29, 30]},{"Chennai": [35, 34, 34]},{"Kolkata": [31, 32, 31]},{"Hyderabad": [29, 30, 28]},
]

print('-----Weather Data-----')
for cities in weather:
    for city, temp in cities.items():
        print(f'{city} : {temp}')

print('-----City With Minimum And Maximum Temperature----')
min_temp = float('inf')
min_city = ""
max_temp = float('-inf')
max_city = ""

for city in weather:
    for city,temp in city.items():

        min_in_city = min(temp)
        max_in_city = max(temp)

        if min_in_city < min_temp:
            min_temp = min_in_city
            min_city = city

        if max_in_city > max_temp:
            max_temp = max_in_city
            max_city = city

print(f'Minimum Temperature City-> {min_city} : {min_temp}')
print(f'Maximum Temperature City-> {max_city} : {max_temp}')

print('-----Cities That Experience Min Temperature More Than 30 degree-----')
cities = [cities for city in weather for cities,temp in city.items() if min(temp) > 30 ]
print(','.join(cities))

print('-----City With Average Temp-----')
cities = {cities:f'{sum(temp)/len(temp):.2f}' for city in weather for cities,temp in city.items() }
for city,temp in cities.items():
    print(f'{city} : {temp}')
