"""
1.
Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
"""
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positivo=[i for i in numbers if i<=0]
print(positivo)
"""Flatten the following 
list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

output
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]


onedimencional=[row3 for row in list_of_lists for number in row for row3  in number ]
print(onedimencional)
"""
curiosiando
print(len(onedimencional))
mi_=str(onedimencional)
print(len(mi_))
print(''.join(mi_))

"""
"""
Using list comprehension create the following list of tuples:

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

"""

liscomprehen=[(i,1,i**2, i**3, i**4, i**5, i**6) for i in range(11)]
#print(liscomprehen)
"""
Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
"""
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [[country.upper(), country[:3].upper(), city.upper()] for country in countries for (country, city) in country]

print(output)

"""
Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]

"""
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output=[{'country':country, 'city':city} for country in countries for(country, city) in country]
print(output)

"""
Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
"""
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output=[f'{name} {lastname}' for name in names for (name, lastname) in name]
print(output)

" y=mx+b"

linear_function = lambda m, b: {'slope': m, 'y_intercept': b}

# Ejemplo de uso
slope_intercept = linear_function(2, 3)
print(slope_intercept['slope'])         # 2
print(slope_intercept['y_intercept'])   # 3
