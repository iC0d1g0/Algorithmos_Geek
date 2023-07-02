def ordBurbuja2 (a,n):
        #/* i es el índice del último elemento de la sublista */
    i = n-1  #/* el proceso continúa hasta que no haya intercambios */
    eficiencia =0
    while i > 0:
        eficiencia+=1
        indiceIntercambio = 0
            #/* explorar la sublista a[0] a a[i] */
            #/* intercambiar pareja y actualizar IndiceIntercambio */
        for j in range(i):
            if a[j+1] < a[j]:
                aux = a[j]
                a[j] = a[j+1]
                a[j+1] = aux
                indiceIntercambio = j
            #/* i se pone al valor del índice del último intercambio */
        i = indiceIntercambio
    print("eficiencia", eficiencia)
    return a
#arr=[ 45, 60, 60,70, 80, 85, 89, 90, 90, 70,0, 1, 2, 4, 6, 6, 9, 23, 40 ]

array = [70,90,0,85,80,60, 89, 40, 70, 60, 90, 23,45, 6, 1, 2, 6, 9]
listaordenada=[0, 1, 2, 6, 6, 9, 23, 40, 45, 60, 60, 70, 70, 80, 85, 89, 90, 90]


print("Lista desordenada",ordBurbuja2(array, len(array)))
print("Lista Ordenada", ordBurbuja2(listaordenada, len(listaordenada)))