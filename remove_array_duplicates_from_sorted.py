arr = [1,2,2,3,4,4,5,5,6]

def remove_duplicates(arr):
    i = 0 
    for j in range(1,len(arr)):
        if arr[i]!= arr[j] :
            arr[i+1] = arr[j]
            i=i+1
    return arr[:i+1]

print("check result :",remove_duplicates(arr))

