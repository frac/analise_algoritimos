#!/usr/bin/python
#coding:utf8

from operator import itemgetter

def qui(num, soma, lista):
    if num == 0:
        if soma == lista[0][1]:
            #if the element is equal to the sum I should print it
            print lista[0][0], lista[0][1]
            return True
        return False

    if lista[num][1] == soma:
        #same here
        #if the element is equal to the sum I should print it
        print lista[num][0], lista[num][1]
        return True

    if qui(num-1, soma-lista[num][1],  lista):
        #if the element is in the sum I should print it
        print lista[num][0], lista[num][1]
        return True

    if qui(num-1, soma,  lista):
        #I do not need to print out this case because it falls down on one of the other cases
        return True
            

def main():
    lines = input()
    atividades = {}
    alimentos = {}
    for i in range(lines):
        foo = raw_input()
        key, kcal = foo.split()
        kcal = int(kcal)
        if kcal > 0:
            alimentos[key] = kcal
        else:
            atividades[key] = kcal

    negativos = atividades.values()
    positivos = alimentos.values()


    alimentos = alimentos.items()
    alimentos.sort(key=itemgetter(1))

    

    atividades = atividades.items()
    atividades.sort(key=itemgetter(1),reverse=True)


#trivial answers
    if not atividades:
        print "no solution"
        return

    if not alimentos:
        print "no solution"
        return

    # se voce tem um elemento zero na lista. desencana.
    
    lista = atividades + alimentos
    if not qui(len(lista)-1, 0, lista):
        print "no solution"
        return
   
    """ 
    s = 0
    S = [0]
    for xi in indexes:
        T = []
        for y in S:
            T += [xi + y]
        U = T + S
        U.sort()
        y = U[0]
        S = [y]
        for z in U:
            if y + 10 < z < s:
                y = z
                S.append(z)
    print S
    """


        
        



if __name__ == '__main__':
    main()
