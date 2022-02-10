def min_heap(A, n, k):
    l = 2 * k + 1
    r = 2 * k + 2
    if l < n and A[l] < A[k]:
        smallest = l
    else:
        smallest = k
    if r < n and A[r] < A[smallest]:
        smallest = r
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        min_heap(A, n, smallest)


def build_min_heap(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for k in range((size//2)-1, -1, -1):
            min_heap(array, size, k)


def delete(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break

    array[i], array[size-1] = array[size-1], array[i]

    array.remove(num)

    for i in range((len(array)//2)-1, -1, -1):
        min_heap(array, len(array), i)


A = []
build_min_heap(A, 3)
build_min_heap(A, 9)
build_min_heap(A, 2)
build_min_heap(A, 1)
build_min_heap(A, 4)
build_min_heap(A, 5)
build_min_heap(A, 10)

print("Min-Heap is: " + str(A))

delete(A, 4)
print("After deleting an element: " + str(A))

# build min heap time complexity o(1)
# insertion in min heap time complexity o(n)
# deletion in  min heap time complexity o(n)
