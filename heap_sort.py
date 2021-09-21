def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapify(arr, n, i, order):
    left = 2*i + 1
    right = 2*i + 2
    largest = i

    if order == "asc":    
        if left < n and arr[i] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right
        
        if largest != i:
            swap(arr, i, largest)        
            heapify(arr, n, largest, order)
    else:
        if left < n and arr[i] > arr[left]:
            largest = left

        if right < n and arr[largest] > arr[right]:
            largest = right
        
        if largest != i:
            swap(arr, i, largest)        
            heapify(arr, n, largest, order)

def heap_sort(arr, order):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, order)
  
    for i in range(n-1, 0, -1):
        swap(arr, 0, i)   
        heapify(arr, i, 0, order)

