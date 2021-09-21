from heap_sort import heap_sort
from timeit import default_timer as time

if __name__ == '__main__':

    print("Welcome to Heap sort")
    print("Input elements using ',' ")
    arr = list(map(int, input().split(",")))
    print("Input asc or desc")
    order = input()

    start_time = time()
    counters = heap_sort(arr, order)
    sort_time = (float(time() - start_time))*1000
    print("Sorting time:", sort_time,"ms" )
    print("Swaps:", counters[0])
    print("Comparisons", counters[1])
    for i in range(len(arr)):
        print (arr[i], end = ' ')