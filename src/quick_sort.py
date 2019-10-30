import random


def quick_sort(A):
    return split(A, 0, len(A) - 1)


def split(A, start, end):
    if start >= end:
        return A
    else:
        index = partition(A, start, end)
        A = split(A, start, index - 1)
        A = split(A, index + 1, end)
        # import pdb; pdb.set_trace()
        return A


def partition(A, start, end):
    pivot = A[random.choice(range(start, end + 1))]
    p_index = start
    for i in range(start, end):
        if A[i] <= pivot:
            temp = A[i]
            A[i] = A[p_index]
            A[p_index] = temp
            p_index += 1
    temp = A[p_index]
    A[p_index] = A[end]
    A[end] = temp
    return p_index
