# Merge sort Blog


## pseudocode
```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length
           
    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1
            
        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

```

Merge sort function takes in a list

It starts by assigning a variable to the length of the list divided by 2, this finds the midpoint of the list.

Now we assign a left and a right list variable to split the list into 2 separate lists.

   - left is assigned to look at index 0 through the midpoint
    - right is assigned to look at the midpoint index through the end of the list

Now we call merge_sort() on both left and right to break them down into their own separate lists

