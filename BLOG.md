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


MergeSort([8,4,23,42,16,15])
```

Merge sort function takes in an unordered list

We start by assigning the list length to the variable `"n"`

We then assign a variable to the length of the list divided by 2, this finds the midpoint of the list.

> Think about how to `round()` the numbers that return as a float value for the midpoint

Now we assign a left and a right list variable to split the list into 2 separate lists.

- **left** is assigned to look at index 0 through the midpoint
- **right** is assigned to look at the midpoint index through the end of the list

Now we call merge_sort() on both left and right to break them down into their own separate lists, creating a total of 4 lists

When dealing with odd length lists the new list will be imbalance, in this example we have a list of 3 values being split into 2 lists. 

| PASS | BEFORE | LEFT | RIGHT | 
| --- | --- | --- | --- |
| 1 | [8,4,23,42,16,15] | [4,8,23] | [42,16,15] | 
| 2 | [4,8,23] & [42,16,15] | [4,8] [23] | [42,16] [15] | 
| 3 | [4,8] & [42,16] | [4] & [8] | [42] & [16] | 
| Final Lists | [8], [4], [23], [42], [16], [15]