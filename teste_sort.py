#!/usr/bin/python
#coding:utf8
from random import randint
from time import time



from insert_sort import insertsort 
from merge_sort import mergesort
from quick_sort import quicksort

for i in range(10):
    SIZE = 10 ** i
    print "tamanho", SIZE
    agora = time()
    quicksort([ randint(0,99) for i in range(SIZE)])
    pronto = time()
    print "qs", pronto - agora

    agora = time()
    insertsort([ randint(0,99) for i in range(SIZE)])
    pronto = time()
    print "insert", pronto - agora

    agora = time()
    mergesort([ randint(0,99) for i in range(SIZE)])
    pronto = time()
    print "merge", pronto - agora




