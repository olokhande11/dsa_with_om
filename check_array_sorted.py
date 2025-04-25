arr = [1,3,4,45,5,1]

def check_sorted(arr):

    for i in range(1,len(arr)):
        if arr[i] >= arr[i-1]:
            {

            }
        else :
            return False
    return True

arr_1 = [1,3,4,5,6,7]

print("unsorted array status",check_sorted(arr))
print("sorted array status",check_sorted(arr_1))