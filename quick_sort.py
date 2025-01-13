import random

def quick_sort(a):
    if len(a) > 1:
        x = a[random.randint(0, len(a) - 1)] # случайное пороговое значение (для разделения на малые и большие)
        low = [u for u in a if u < x]
        eq = [u for u in a if u == x]
        hight = [u for u in a if u > x]
        a = quick_sort(low) + eq + quick_sort(hight)

    return a

a = [9, 5, -3, 4, 7, 8, -8]
a = quick_sort(a)

print(a)

# Версия сотрировки in-place (без использования дополнительной памяти)
"""
from random import randint
def partition(array: list, left: int, right: int) -> int:
    rand = randint(left, right)
    array[rand], array[left] = array[left], array[rand]
    x = array[left]
    j = left
    for i in range(left + 1, right + 1):
        if array[i] <= x:
            j += 1
            array[j], array[i] = array[i], array[j]
    array[left], array[j] = array[j], array[left]
    return j


def quick_sort(array: list, left: int, right: int) -> None:
    if left < right:
        m = partition(array, left, right)
        quick_sort(array, left, m - 1)
        quick_sort(array, m + 1, right)
"""