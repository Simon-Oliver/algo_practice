print((9.5 * 4.5 - 2.5 * 3) / (45.5 - 3.5))

a = 3
b = 4
c = 5

print(b * b - 4 * a * c)
print(4 * 4 - 4 * 3 * 5)

v0 = 5.6
v1 = 10.5
t = 0.5

print((v1 - v0) / t)
print((10.5 - 5.6) / 0.5)

# Australian Popoulation: 25.69 million (2020)
population = 25.69 * 1000000
seconds_year = 365 * 24 * 60 * 60
born = seconds_year / 7
death = seconds_year / 13
immigrant = seconds_year / 45
years = 5

print(f"Starting Population: {population}")
for y in range(years):
    population = population - death + born + immigrant
    print(f"Year {y+1}: {population}")