from math import ceil
from random import random
import time


# function to sort array using bubble sort algorithm
def bubble_sort(arr):
  arr_length = len(arr)

  for i in range(arr_length):
    for j in range(0, arr_length - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Generating array with random numbers and random length

arr = []
arr_length = int(input("Input array length\n"))

print("Generating array")

for i in range(arr_length):
  # Generating random number from range [-50; 50]
  number = -50 + ceil(random() * 101)
  arr.append(number)

# print("array before sort -> ", arr)

print("starting sorting array")

start_time = time.time()
bubble_sort(arr)
end_time = time.time()

# print("array after sort -> ", arr)

print("--- %s seconds --- " % (end_time - start_time))