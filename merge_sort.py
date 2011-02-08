#!/usr/bin/python
##coding:utf8

from random import randint

#A1 = [randint(1,200) for a in range(10)]
#A2 = [randint(1,200) for a in range(10)]


import sys
def merge(lista, p, q, r):
    L = lista[p:q] + [sys.maxint]
    R = lista[q:r] + [sys.maxint]
    i = 0
    j = 0
    for k in range(p,r):
        if L[i] < R[j]:
            lista[k] = L[i]
            i += 1
        else:
            lista[k] = R[j]
            j += 1







def merge_sort(lista, p, r):
    if p < r:
        q = (p+r)/2
        merge_sort(lista,p,q)
        merge_sort(lista,q+1,r)
        merge(lista,p,q+1,r+1)

def mergesort(lista):
    merge_sort(lista,0,len(lista)-1)

#prefix = [] 

#lista = prefix + A1+A2
#print lista
#merge_sort(lista,len(prefix),len(lista)-1)
#print lista
#print prefix + sorted(A1+A2)
