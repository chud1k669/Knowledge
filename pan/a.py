import numpy as np

def solution(arr1, arr2):
    arr = [arr1[0] + arr2[-2],arr1[1] + arr2[-1]]
    return arr
print(solution([1,2],[10,11]))