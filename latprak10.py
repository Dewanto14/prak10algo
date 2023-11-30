# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:52:52 2023

@author: Huawei
"""
def definisi(arr, i, j):
    dew = arr[i]
    arr[i] = arr[j]
    arr[j] = dew
    
    
def bubble_sort(arr, n=None):
    if n is None:
        n = len(arr)
        
    if n <= 1:
        return arr
    for i in range(n -1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return bubble_sort(arr, n - 1)

data_list = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
print("List Sebelum Disorting: \n", data_list)
sorted_list = bubble_sort(data_list, len(data_list))
print("List Yang Sudah Disorting: \n", sorted_list)