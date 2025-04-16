def merge_sort(arr):
    # If the list has 1 or no elements, it's already sorted, so just return it
    if len(arr) <= 1:
        return arr
    
    # Split the list into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Sort each half by calling merge_sort again (this is recursion!)
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Now merge the two sorted halves into one sorted list
    return merge(left, right)

def merge(left, right):
    result = []  # This will hold the final merged list
    i = j = 0    # Pointers for left and right lists
    
    # Keep picking the smallest element from left or right until one list runs out
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # If anything's left in the left list, add it to the result
    result.extend(left[i:])
    # If anything's left in the right list, add that too
    result.extend(right[j:])
    
    return result

# Let's try it out!
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(f"Unsorted list: {unsorted_list}")
sorted_list = merge_sort(unsorted_list)
print(f"Sorted list: {sorted_list}")
