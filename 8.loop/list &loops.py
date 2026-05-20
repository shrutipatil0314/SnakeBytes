countries = ["India", "USA", "UK", "Australia", "Germany",
              "Ireland", "Italy", "Spain", "France", "Russia"]

#count all the countries whic are starting with letter 'I'
#also print the count at the end
count = 0
output = []
for country in countries:
    if country.startswith("I"):
        count=count+1
        output.append(country)
print(output)
print(count)
    
