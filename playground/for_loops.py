cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for city in cities: # "city" is the loops itteration variable. 
   print(city.title()) # this itterates through the cities list and prints w/cap 
                        # letter on the first. 

capatalize_cities = []

for city in cities: 
    capatalize_cities.append(city.title())  

print(capatalize_cities)                         
print("Done!")


# Write a for loop to print out each word in the sentence list, one word per line

sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

for i in sentence: 
    print(i)

# Write a for loop using range() to print out multiples of 5 up to 30 inclusive

for i in range(5, 35, 5):
    print(i)