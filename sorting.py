import random
import time

#This is the Binary Search functtion
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Quick Sort function will help to sort the array in every iteration
def quick_sort(arr, low, high):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    if low < high:
        pi = partition(low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

# This part of the code will generate random sensor data and help to test the sorting and searching algorithms
random.seed(42)
sensor_data = [random.uniform(0, 100) for _ in range(500)]
target = sensor_data[250]

# Testing the algorithms
data_copy = sensor_data.copy()
start_time = time.time()
quick_sort(data_copy, 0, len(data_copy) - 1)
print(f"Quick Sort: {(time.time() - start_time):.6f}s")

# I a testin the binary search algorithm
sorted_data = data_copy
start_time = time.time()
index = binary_search(sorted_data, target)
print(f"Binary Search: Index {index}, Time: {(time.time() - start_time):.6f}s")