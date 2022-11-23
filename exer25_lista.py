# Listas

lista1 = ['Catarina','Felipe',1986,2002]
print(lista1)

print(lista1[3])

print(lista1.index('Felipe'))   # index retorna o número do índice de um elemento que está na lista, senão estiver, retorna erro

print(len(lista1))                          # len = exibe a quantidade de elementos da lista

lista1.append('Adolfo')                     # Adicionando elementos em uma lista
lista1.append('Fabio')
lista1.append('Isabela')
print(lista1)

lista1 = ['Catarina','Felipe',1986,2002]
lista1 = 'Adolfo'                           # sobrescreve o valor no indice
print(lista1)

lista1 = ['Catarina','Felipe',1986,2002]
lista1.insert(2,'Substituido')              # substituindo valores na lista
print(lista1)

lista1 = ['Catarina','Felipe',1986,2002]    
lista1.pop(1)                               # pop - remove o elemento pelo número do indice
print(lista1)

lista1 = ['Catarina','Felipe',1986,2002]
lista1.remove(1986)                       # remove - remove o elemento pelo valor
print(lista1)

num = [9,4,7,2,5,1,8,3,6,0]
num.sort()                                # ordem crescente  
print(num)

num = [9,4,7,2,5,1,8,3,6,0]
num.sort(reverse=True)                  # ordem decrescente
print(num)

num = [9,4,7,2,5,1,8,3,6,0]
num.sort(reverse=True)                             # ordem inversa da lista
print(num)

frutas1 = ['Banana','Maçã','Morango']
frutas2 = ['Manga','Laranja']
todasFrutas = frutas1 + frutas2                       # concatenação
print(todasFrutas)

frutas1 = ['Banana','Maçã','Morango']
frutas2 = ['Manga','Laranja']
frutas2.extend(frutas1)                             # adiciona na primeira lista os elementos da segunda lista
frutas2.append('Amora')
print(frutas1)
print(frutas2)







