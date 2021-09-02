from math import ceil
from random import random
import time


# function to sort array using insertion sort algorithm
def insertion_sort(arr):
  arr_length = len(arr)

  for i in range(1, arr_length):
    elem = arr[i]
    j = i
    while j > 0 and elem < arr[j - 1]:
      arr[j] = arr[j - 1]
      j -= 1
    arr[j] = elem

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
insertion_sort(arr)
end_time = time.time()

# print("array after sort -> ", arr)

print("--- %s seconds --- " % (end_time - start_time))