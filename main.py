from heap_sort import heap_sort

if __name__ == '__main__':

    print("Welcome to Heap sort")
    print("Input elements using ',' ")
    arr = list(map(int, input().split(",")))
    print("Input asc or desc")
    order = input()

    heap_sort(arr, order)
    
    for i in range(len(arr)):
        print (arr[i], end = ' ')