
"""Exercises: Level 1
"""
"""
1.
Declare a function add_two_numbers. It takes two parameters and it returns a sum.
"""
add_two_numbers=lambda a,b: a+b
#print(add_two_numbers(6,4))

"""
2.
Area of a circle is calculated as follows: 
area = π x r x r. 
Write a function that calculates area_of_circle"""

from math import pi

Area=lambda r: pi * (r *r)
#print("Ingresa el radio \n",Area(10))
"""
3.
    Write a function called add_all_nums which takes arbitrary
    number of arguments and sums all the arguments. 
    Check if all the list items are number types. 
    If not do give a reasonable feedback."""

def add_all_nums(*args): 
    total=0
    for num in args: 
        if isinstance(num, (int, float)): 
            total+=num
        else: 
            return 'no all args are numbers'
    return total

print(add_all_nums(4,3,4,3,2,3,4,4))
print(add_all_nums('pepe', 'pepita',23,4,2))

"""
4.
    Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
    Write a function which converts °C to °F, 
    convert_celsius_to-fahrenheit."""
    #°F = (°C x 9/5) + 32

F=lambda c: (c*9/5)+32
print("Convertidor de Celcius a Fahrenheit: ", F(33))

"""
5.
    Write a function called check-season,
    it takes a month parameter and returns the season: 
    Autumn, Winter, Spring or Summer.
"""
def check_season(month): 
    month=month.lower()
    Autoum=['september', 'october', 'november']
    Winter=['december', 'january', 'february']
    Spring=['march', 'april','may']
    if month in Autoum: 
        print('Autoum')
    elif month in Winter: 
        print("Winter")
    elif month in Spring: 
        print("Spring")
    else: 
        return 'Error'


check_season('october')