from basic_operations import left
from basic_operations import right


def max_heapify(a, i):
    max_index = i
    l = left(i)
    r = right(i)
    if l < a.heap_size:
        if a.arr[i] < a.arr[l]:
            max_index = l

    if r < a.heap_size:
        if a.arr[max_index] < a.arr[r]:
            max_index = r

    if max_index != i:
        temp = a.arr[i]
        a.arr[i] = a.arr[max_index]
        a.arr[max_index] = temp
        i = max_index
        max_heapify(a, i)
    else:
        return


def build_max_heap(a):
    for i in reversed(range(0, a.heap_size / 2)):
        max_heapify(a, i)


def sort(a):
    arr = a.arr
    build_max_heap(a)
    for i in range(0, len(arr) - 1):
        heap_size = a.heap_size
        temp = arr[heap_size-1]
        arr[heap_size-1] = arr[0]
        arr[0] = temp
        a.heap_size = heap_size - 1
        max_heapify(a, 0)

    print a.arr
