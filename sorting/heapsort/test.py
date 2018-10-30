from modules.heap_sort import max_heapify
from classes.a import A

x = A()
arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
x.arr = arr
x.heap_size = len(arr)
i = 1
max_heapify(x, i)