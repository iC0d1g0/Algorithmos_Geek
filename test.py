
import random
import string
alfabeto = string.ascii_letters + string.digits + string.punctuation
#print("".join(random.choices(alfabeto,k=3)))
even_numbers = [i-1 for i in range(2,22) if i%2] 
print(even_numbers) 

