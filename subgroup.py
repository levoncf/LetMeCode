#!/usr/bin/python3
Z = 23
def func(n, k):
    lists =[]
    for i in range(0,k):
        factor = n**i
        lists.append(factor%Z)
    sort_list = sorted(lists, key=int)
    return Remove(sort_list)
# Python code to remove duplicate elements 
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 

if __name__ =='__main__':
    lists = []
    for i in range(0,Z):
        print(func(i,22), 'when i = {}'.format(i))
