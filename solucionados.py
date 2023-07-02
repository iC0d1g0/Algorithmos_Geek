from random import randint
import string
import random
#Exercises: Level 1

"""
1.
Ejercicios: Write a function which gerates
a six digit/character random_user_id
"""

#EL MAS SIMPLE 
expresion = lambda n=6 : ''.join(random.choices(string.printable, k=int(n))) if n else 'no input'
#print(expresion())

"""
Ejercicio numero 2
Modify the previous task. Declare a function named user_id_gen_by_user. 
It doesn't take any parameters but it takes two inputs using input().
 One of the inputs is the number of characters and the second input is
the number of IDs which are supposed to be generated.
"""
def user_id_gen_by_user(): 
    characters = int(input("characters: "))
    number_IDs=int(input("number of IDs: "))
    for i in range(number_IDs): print(f"{i+1}:  {expresion(characters)}")
#print(user_id_gen_by_user())


"""
# 3. Write a function named rgb_color_gen.
It will generate rgb colors (3 values ranging from 0 to 255 each).
"""
rgb = lambda: random.randint(0, 255)
rgb_color_gen=lambda: f"rgb({rgb()},{rgb()},{rgb()})"
#print(rgb_color_gen())

#Exercises: Level 2

"""
1.
Write a function list_of_hexa_colors which returns any
number of hexadecimal colors in an array (six hexadecimal
numbers written after #. Hexadecimal numeral system is made out of 16 symbols,
0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

"""
def list_of_hexa_colors(x): 
    colors=[]
    if x:
        for i in range(x): colors.append('#'+''.join(random.choices(string.hexdigits, k=6)))  
    else:
        return 'Invalid Input'
    return colors

"""
2.
Write a function list_of_rgb_colors
which returns
any number of RGB colors in an array.
"""
def list_of_rgb_colors(x): 
    colors=[]
    if x:
        for i in range(x): colors.append(rgb_color_gen())  
    else:
            return 'Invalid Input'
    return colors

"""
3.
Write a function generate_colors 
which can generate any number of hexa or rgb colors.
"""
def generate_colors(a,b): 
    match a.lower(): 
        case 'hexa':
            return list_of_hexa_colors(b)
        case 'rgb':
            return list_of_rgb_colors(b)
        case _: 
            return 'Invalid entry, try : hexa or rgb'
        
print(generate_colors('HEXA', 3)) # ['#a3e12f','#03ed55','#eb3d2b'] 
print(generate_colors('heXa', 1) )# ['#b334ef']
print(generate_colors('rgB', 3))  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
print(generate_colors('rGb', 1))  # ['rgb(33,79, 176)']
