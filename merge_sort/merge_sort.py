def merge_sort(lists):
    n = len(lists)

    if n < 2:
        return "2 or more numbers needed to sort"

    if n > 1:
        mid = round(n / 2) 
        left = lists[:mid]
        right = lists[mid:]
        #  ^^^[START :STOP :STEP]
        
        merge_sort(left)

        merge_sort(right)

        merge(left, right, lists)
    return lists

def merge(left, right, lists):
    i = 0   # LEFT
    j = 0   # RIGHT
    k = 0   # LISTs

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lists[k] = left[i]
            i += 1
        else:
            lists[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        lists[k] = left[i]
        i += 1
        k +=1

    while j < len(right):
        lists[k] = right[j]
        j += 1
        k +=1

    # print("returned lists", lists)  
    return lists

print(merge_sort([8,4,-23,42,-16,15]))