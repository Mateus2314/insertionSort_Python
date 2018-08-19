def insertionSort(A):
    
    for i in range(1,len(A)):
        chave = A[i]
        j = i-1
        while j >= 0 and chave < A[j]:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = chave

filename= raw_input('Path do arquivo:')
file = open(filename, 'r')

insertion = [int(i) for i in file]

insertionSort(insertion)

arquivo = open('resultado.txt', 'w')
arquivo.close()

for i in range(len(insertion)):
    resultado = open('resultado.txt', 'a')
    resultado.write(str(insertion[i])+ '\n') 
    resultado.close()
