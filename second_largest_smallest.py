

l1 = [9,2,3,4,5,56,56,565,77,75,77]


def ss_largest(arr):
    largest = arr[0]
    slargest = -1

    for i in arr:
        if i > largest :
            ss_largest= largest
            largest = i
        elif i < largest and i > slargest:
            slargest = i
    return largest,slargest


def ss_smallest(arr):
    smallest = arr[0]
    s_smallest = 0
    for i in arr:
        if i <smallest:
            s_smallest =smallest
            smallest =i
        elif i != smallest and i <s_smallest :   
            s_smallest =i
    return smallest,s_smallest


print("largest {} and ss largest {}",ss_largest(l1))

print("smallest {} and ss smallest {}",ss_smallest(l1))