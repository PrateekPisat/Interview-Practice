from heapq import heapify, heappush, heappop


def sort(arr, k):
    result = []
    heap = arr[:k + 1]
    remaining_elements = arr[k + 1:]
    heapify(heap)

    while remaining_elements:
        result += [heappop(heap)]
        heappush(heap, remaining_elements.pop(0))

    while heap:
        result += [heappop(heap)]

    return result
