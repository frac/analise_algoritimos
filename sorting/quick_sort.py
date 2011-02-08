#!/usr/bin/python
#coding:utf8

from random import randint, randrange




def quicksort(lista):
    if len(lista) < 1:
        return lista

    pos = randrange(len(lista))
    pivot = lista[pos]
    less = []
    more = []
    for i, key in enumerate(lista):
        if i == pos:
            continue
        if key < pivot:
            less.append(key)
        else:
            more.append(key)
    return quicksort(less) + [pivot] + quicksort(more)



if __name__ == '__main__':
    SIZE = 50000000
    lista = [ randint(0,999) for i in range(SIZE)]
    print lista
    print quicksort(lista)
