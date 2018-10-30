from basic_operations import left
from basic_operations import right


def max_heapify(A, i):
    max_index = i
    l = left(i)
    r = right(i)
    if l < A.heap_size:
        if A.arr[i] < A.arr[l]:
            max_index = l

    if r < A.heap_size:
        if A.arr[max_index] < A.arr[r]:
            max_index = r

    if max_index != i:
        temp = A.arr[i]
        A.arr[i] = A.arr[max_index]
        A.arr[max_index] = temp
        i = max_index
        max_heapify(A, i)
    else:
        print A.arr
        return

