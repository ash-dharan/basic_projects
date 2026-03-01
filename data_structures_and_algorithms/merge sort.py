# merge sort

def two_pointer_merge(list1,list2):
    i = 0
    j = 0
    result = []

    l1_len = len(list1)
    l2_len = len(list2)

    while i < l1_len and j < l2_len:
        if list1[i] <= list2[j]:
            result.append(list1[i])

            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    result.extend(list1[i:])
    result.extend(list2[j:])

    return result

def merge_sort(array):
    l = len(array)
    if l <= 1:
        return array
    else:
        left = merge_sort(array[:l//2])
        right = merge_sort(array[l//2:])

        return two_pointer_merge(left,right)

data = [3,6,1,3,6,7,9,99,12,46]

print(merge_sort(data))

