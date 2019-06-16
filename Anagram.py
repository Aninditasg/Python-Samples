import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    dict_chars = dict()
    str1 =a.strip()
    str2=b.strip()
    
    for char in str1:
        if char in dict_chars:
            dict_chars[char] += 1
        else:
            dict_chars[char] = 1
    for char in str2:
        if char in dict_chars:
            dict_chars[char] -= 1
        else:
            dict_chars[char] = -1
    
    sum_diff = 0
    
    for char in dict_chars.keys():
        sum_diff += abs(dict_chars[char])
        
    return sum_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
