
city_populations = {}

while True:
    
    city_name = input("Enter the name of a city (or type 'stop' to finish): ")
    
   
    if city_name.lower() == "stop":
        break
    
   
    population = len(city_name.replace(" ", "")) * 1_000_000  # Ignore spaces in the city name
    city_populations[city_name] = population

# Sort cities by their population in descending order
sorted_cities = sorted(city_populations.items(), key=lambda x: x[1], reverse=True)


print("\nCities and their populations :")
for city, population in sorted_cities:
    print(f"{city}: {population:,} citizens")
