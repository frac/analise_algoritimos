#!/usr/bin/python
#coding:utf8

#import ipdb
def insertsort(lista):
    #ipdb.set_trace()

    for i in range(1,len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > key:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = key 

    #print lista

if __name__ == '__main__':
    foo = [9,2,9,4,5,12,33,66,2,233,1,1]
    foo1 = [9,2,9,4,5,12,33,66,2,233,1,1]
    insertsort(foo)
    print sorted(foo1)
