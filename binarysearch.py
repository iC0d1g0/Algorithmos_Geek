
def binarysearch(array, target): 
    start = 0
    end = len(array)-1
    intentos=0
    while start <= end: 
        middle =(start+ end) //2
        #print(middle)
        intentos+=1
        if array[middle]==target:
            
            print("INtenteos", intentos)
            return True
        elif array[middle]<target: 
            start=middle+1
        else: 
            end=middle-1
    
    print("El numero elegido esta fuera de rango, INtenteos: ", intentos)
    return False

array = [int(i) for i in range(10000001)]
target = int(input("INgresa el target: >"))
print(f"Veamos si encuentras el {target}: ",binarysearch(array,target ))
print("Evaluando el len: ",len(array)-1)
