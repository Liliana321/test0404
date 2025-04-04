# Crea un sistema ripetibile che si occupi di dividere su tre possibili liste i tipi
# basilari di dato che riceve in entrata. 
# Deve poter stampare una lista singola o tutte.  
# Si deve ripetere X volte 
# definite all'inizio dall'utente

n=int(input("quante volte vuoi ripete l'analisi? "))

lista_stringa=[]
lista_numero=[]
lista_boolean=[]
lista_completa=[True,False]

contatore=0
while contatore <n:
    stringa=input("inserisci valore:")
    numero=int(input("inserisci numero"))


    lista_completa.append(stringa)
    lista_completa.append(numero)
    print(lista_completa)

    for i in lista_completa:
        if i is bool:
            lista_boolean.append(i)
        elif i is str:
            lista_stringa.append(i)
        else:
            lista_numero.append(i)
    
    contatore+=1
    
scelta=int(input(" vuoi stampare lista dei numeri (1), delle stringhe (2), dei booleani (3), tutte (4)"))

match scelta:
    case 1:
        print(lista_numero)
    case 2:
        print(lista_stringa)
    case 3:
        print(lista_boolean)
    case 4:
        print(lista_numero)
        print(lista_stringa)
        print(lista_boolean)
    case _:
        print("scelta non valida")