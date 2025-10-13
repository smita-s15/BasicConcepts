# 🐍 Python Practice Problems

## 1. Lists & Arrays

### Flatten a nested list

Time Complexity: O(n) — where n = total number of elements in all nested lists.

Space Complexity: O(n + d) — where n = number of elements, d = maximum depth of nesting.

```python
from collections.abc import Iterable

def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

print(flatten([[1, 2], [3, [4, 5]]]))  # [1, 2, 3, 4, 5]
```

### Reverse a list

```python
lst = [1, 2, 3, 4]
print(lst[::-1])  # [4, 3, 2, 1]
```

### Find max & min without max()/min()

```python
lst = [3, 1, 4, 2]
max_val = lst[0]
min_val = lst[0]
for num in lst:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
print(max_val, min_val)  # 4 1
```

### Remove duplicates

```python
lst = [1, 2, 2, 3, 4, 4]
print(list(set(lst)))  # [1, 2, 3, 4]
```

### Rotate array

```python
lst = [1, 2, 3, 4, 5]
k = 2
rotated = lst[-k:] + lst[:-k]
print(rotated)  # [4, 5, 1, 2, 3]
```

## 2. Strings

### Reverse a string

```python
s = "hello"
print(s[::-1])  # olleh
```

### Check palindrome

```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # True
print(is_palindrome("apple"))  # False
```

### Count vowels & consonants

```python
s = "hello"
vowels = consonants = 0
for char in s.lower():
    if char in 'aeiou':
        vowels += 1 
    elif char.isalpha():
        consonants += 1
print(vowels, consonants)  # 2 3
```

### First non-repeated character

```python
s = "swiss"
for char in s:
    if s.count(char) == 1:
        print(char)  # w
        break
```

### Check anagram

```python
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  # True
```

## 3. Numbers

### Check prime

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # True
```

### Fibonacci sequence

```python
def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

print(fibonacci(5))  # [0, 1, 1, 2, 3]
```

### Factorial

```python
def factorial_iter(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def factorial_rec(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n-1)

print(factorial_iter(5))  # 120
print(factorial_rec(5))   # 120
```

### GCD & LCM

```python
import math

a, b = 12, 18
print(math.gcd(a, b))  # 6
print(a*b // math.gcd(a, b))  # 36
```

### Armstrong number

```python
num = 153
sum_cubes = sum(int(d)**3 for d in str(num))
print(sum_cubes == num)  # True
```

## 4. Dictionaries & Sets

### Count frequency

```python
s = "banana"
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
print(freq)  # {'b':1, 'a':3, 'n':2}
```

### Merge dictionaries

```python
d1 = {'a':1}
d2 = {'b':2}
d1.update(d2)
print(d1)  # {'a':1, 'b':2}
```

### Common elements

```python
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print(list(set(list1) & set(list2)))  # [2, 3]
```

### Check subset

```python
print({1,2}.issubset({1,2,3,4}))  # True
```

### Sort dictionary by values

```python
d = {'a':3,'b':1,'c':2}
sorted_d = dict(sorted(d.items(), key=lambda x:x[1]))
print(sorted_d)  # {'b':1,'c':2,'a':3}
```

## 5. Algorithms & Logic

### Binary search

```python
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1,2,3,4,5],3))  # 2
```

### Bubble sort

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([4,2,1,3]))  # [1,2,3,4]
```

### Second largest number

```python
lst = [3,5,1,4]
lst = list(set(lst))
lst.remove(max(lst))
print(max(lst))  # 4
```

### Move zeros to end

```python
lst = [0,1,0,3,12]
nz = [x for x in lst if x != 0]
zeros = [0]*lst.count(0)
print(nz + zeros)  # [1,3,12,0,0]
```

### Two sum

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target-num], i]
        seen[num] = i

print(two_sum([2,7,11,15], 9))  # [0,1]
```

## 6. Advanced

### Flatten dictionary

```python
def flatten_dict(d, parent_key='', sep='.'):
    items = {}
    for k,v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v,new_key,sep))
        else:
            items[new_key] = v
    return items

print(flatten_dict({'a':{'b':1}}))  # {'a.b':1}
```

### Matrix transpose

```python
matrix = [[1,2,3],[4,5,6]]
transpose = [list(row) for row in zip(*matrix)]
print(transpose)  # [[1,4],[2,5],[3,6]]
```

### Spiral traversal

```python
def spiral(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result

print(spiral([[1,2,3],[4,5,6],[7,8,9]]))  # [1,2,3,6,9,8,7,4,5]
```

### Balanced parentheses

```python
def is_balanced(s):
    stack = []
    mapping = {')':'(', ']':'[', '}':'{'}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack

print(is_balanced("({[]})"))  # True
```

### Generate all subsets

```python
from itertools import combinations
lst = [1,2,3]
subsets = [list(combinations(lst,i)) for i in range(len(lst)+1)]
subsets = [item for sublist in subsets for item in sublist]
print(subsets)  # [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)]
```
