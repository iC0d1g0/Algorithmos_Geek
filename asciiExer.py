"""
Ejercicios: Write a function which gerates a six digit/character random_user_id


"""
#importo los modulos randint de random y string para acceder todos los ascii
from random import randint
import string
import random

"""
Creo un alista con todos los caracteres del codigo ascii
"""
alfabeto=list(string.ascii_letters + string.digits +string.punctuation)
def random_user_id(n=0): 

    try:
        n=int(n)
    except : 
        return 'invalid input'
    if n: 
        id=''
    
        for i in range(n): 
            aleatorio =alfabeto[randint(0,len(alfabeto)-1)]
            id=id+aleatorio
        return id
    return 'no input'
    
    """
    No recibe parametros,
    usa id='' basia como base, 5
    un for en el rango de 6.
    usabos aleatorio dentro del for para calcular o selecionar un caracter de la 
    lista random y agregarcelo a id. 
    """
    

#print("pOR MI, ",random_user_id(10))
alfabeto = string.ascii_letters + string.digits + string.punctuation
def random_user_id2(n=0):
    try:
        n = int(n)
    except ValueError:
        return 'invalid input'

    if n > 0:
        return ''.join(random.choices(alfabeto, k=n))

    return 'no input'






def random_user_id4(n=0):
    try:
        n = int(n)
    except ValueError:
        return 'invalid input'

    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=n)) if n else 'no input'



def random_user_id8(n=0):
    try:
        return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=int(n))) if n else 'no input'

    except ValueError:
        return 'invalid input'
    



#EL MAS SIMPLE 
expresion = lambda n : ''.join(random.choices(string.printable, k=int(n))) if n else 'no input'
"""
try: print("Usando lambda: ", expresion('a'))
except: print("Que error ")
"""

""" 
COn todo y exeptciones

"""
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
    
#user_id_gen_by_user()

rgb = lambda: random.randint(0, 255)
rgb_color_gen=lambda: f"rgb({rgb()},{rgb()},{rgb()})"

"""
def rgb_color_gen(): 
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
"""


#print(rgb_color_gen())

#print(hex(10))
"""
1.
Write a function list_of_hexa_colors which returns any
number of hexadecimal colors in an array (six hexadecimal
numbers written after #. Hexadecimal numeral system is made out of 16 symbols,
0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
"""

list_of_hexa_colors=lambda :'#'+''.join(random.choices(string.hexdigits, k=6))

#print(list_of_hexa_colors())
"""
Write a function list_of_rgb_colors
 which returns
 any number of RGB colors in an array.
 """
def list_of_hexa_colors2(x): 
    colors=[]
    if x:
        for i in range(x): colors.append(list_of_hexa_colors())  
    else:
            return 'Invalid Input'
    return colors
def list_of_rgb_colors3(x): 
    colors=[]
    if x:
        for i in range(x): colors.append(rgb_color_gen())  
    else:
            return 'Invalid Input'
    return colors

#print(list_of_rgb_colors3(7))
"""Write a function generate_colors which 
can generate any number of hexa or rgb colors.
"""
def generate_colors(a,b): 
    if a == 'rgb'.lower(): 
        return list_of_rgb_colors3(b)
    elif a=='hex'.lower(): 
        return list_of_hexa_colors2(b)
    else: 
        return 'Invalid entry, try : hex or rgb'

print(generate_colors('hex', 3)) # ['#a3e12f','#03ed55','#eb3d2b'] 
print(generate_colors('hex', 1)) # ['#b334ef']
print(generate_colors('rgb', 3))  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
print(generate_colors('rgb', 1))

    