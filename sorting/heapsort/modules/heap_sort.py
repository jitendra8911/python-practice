from basic_operations import left
from basic_operations import right


def max_heapify(A, i):
    max_index = i
    l = left(i)
    r = right(i)
    if l < len(A):
        if A[i] < A[l]:
            max_index = l

    if r < len(A):
        if A[max_index] < A[r]:
            max_index = r

    if max_index != i:
        temp = A[i]
        A[i] = A[max_index]
        A[max_index] = temp
        i = max_index
        max_heapify(A, i)
    else:
        print A
        return

