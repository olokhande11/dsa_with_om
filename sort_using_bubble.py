def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Track if any swaps happened in this pass
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            print(f"Stopped early at pass {i+1}")
            break
    return arr

arr = [5, 3, 8, 4, 2]

print(bubble_sort_optimized(arr))