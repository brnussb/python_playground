cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for city in cities: # "city" is the loops itteration variable. 
   print(city.title()) # this itterates through the cities list and prints w/cap 
                        # letter on the first. 

capatalize_cities = []

for city in cities: 
    capatalize_cities.append(city.title())  

print(capatalize_cities)                         
print("Done!")