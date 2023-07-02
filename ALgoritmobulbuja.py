
def BubleSort(array): 
    lenth = len(array)-1
    for i in range(0,lenth) : 

        for j in range(0,lenth):
            if array[j] >array[j+1]: 
                demo =array[j]
                array[j]=array[j+1]
                array[j+1]=demo
    print("Bucle i", i)
    print("Bucle J", j)
    return array
array = [70,90,0,85,80,60, 89, 40, 70, 60, 90, 23,45, 6, 1, 2, 6, 9]
listaordenada=[0, 1, 2, 6, 6, 9, 23, 40, 45, 60, 60, 70, 70, 80, 85, 89, 90, 90]
print(BubleSort(array))
print("Lista ordenada",BubleSort(listaordenada) )



