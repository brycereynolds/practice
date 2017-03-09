#!/bin/python3

import sys



n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

## Recursion solution
# def sumArr(arr, n):
#   return arr[n] if n > 0 else sumArr(arr, n - 1)

## Iterative solution
def sumArr(arr):
  num = 0
  for val in arr:
    num += val
  return num

print(sumArr(arr))

## Easy solution
# print(sum(arr))