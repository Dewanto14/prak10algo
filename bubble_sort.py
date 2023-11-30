# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:05:48 2023

@author: Huawei
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid  
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  

def search_element(arr, target):
    bubble_sort(arr)

    result = binary_search(arr, target)

    if result != -1:
        return f"Elemen {target} ditemukan pada indeks {result}."
    else:
        return f"Elemen {target} tidak ditemukan dalam list setelah sorting."

my_list = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
target_element = int(input("Masukkan Angka: "))

hasil_pencarian = search_element(my_list, target_element)
print(f"Tablenya \n{my_list} \nTargetnya: {target_element}")
print(hasil_pencarian)
