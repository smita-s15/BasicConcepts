string = "Heloow World"

vowels = 0
consonants=0

for char in string.lower():
    if char in "aeiou":
        vowels += 1
    else:
        consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)



string = "kobas"
string2="boka"
count=[]

def isAnagram():
    return sorted(string)==sorted(string2)
print(isAnagram())

for char in string:
    if string.count(char) == 1:
        count.append(char)
print(count)

if string == string[::-1]:
    print("palindrome")
else:
    print("not palindrome")

reversedString= ""

for ch in string:
    reversedString = ch+reversedString
    
print(reversedString,"reversedString")
    

string = "hello world"
vowels = 0
consonants = 0

for char in string.lower():
    if char in "aeiou":
        vowels += 1
    elif 'a' <= char <= 'z':
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)




def anagrams(str1, str2):
    return sorted(str1)==sorted(str2)


print(anagrams("listen", "silent"))  # True
print(anagrams("hello", "world"))    # False


string ="Hello There..."
char_counts = {}
# def getCountOfCharacter(str):
for char in string:
    if char in char_counts:
        char_counts[char] += 1
    else:
         char_counts[char] = 1


print(char_counts)


string = "Hello There..."
char_counts = {}

for char in string:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

print(char_counts)

import time

def task(name):
    print(f"Starting {name}")
    time.sleep(2)  # blocking
    print(f"Finished {name}")

task("A")
task("B")


class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

for num in Counter(5):
    print(num)  # 1 2 3 4 5



def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)  # Prints 1 2 3 4 5


def repeat_word(word, times):
    return word * times

print(repeat_word("HI", 3))  # "HiHiHi"


original_list = [1, 2, 2, 3]
slst=[4, 4, 5, 1]
 
combined_list = original_list+ slst

for pass_number in range(len(combined_list) + 1):
    for current_index in range(0, len(combined_list) - pass_number - 1):
        next_index = current_index + 1
        if combined_list[current_index] > combined_list[next_index]:
            combined_list[current_index], combined_list[next_index] = combined_list[next_index], combined_list[current_index]

print(combined_list)

stringa = "abcabcabcdabcd"

longest = ""
n = len(stringa)

for length in range(1, n//2 + 1):  # possible substring lengths
    for i in range(n - 2*length + 1):
        if stringa[i:i+length] == stringa[i+length:i+2*length]:
            if length > len(longest):
                longest = stringa[i:i+length]

print("Longest sequential repeated substring:", longest)




# original_list = [1, 2, 2, 3]
# slst = [4, 4, 5, 1]

# d = original_list + slst
# print(sorted(d))


# import copy
# a = [[1,2],[3,4]]
# b = copy.copy(a)       # Shallow copy
# print(b)
# c = copy.deepcopy(a) 

# print(a)

# s={1,2,3,4,frozenset({6,9,0})}
# a = frozenset({1, 2})
# b = frozenset({3, 4, a})

# print(b)


# a = [1, 2, 3]
# b = a
# a.append(4)
# print(b)

 
 

# prime_array=[]

# for i in range(1,101):
#     if(i%i==0):
#         print(i)
#         prime_array.append(i)
        
# print(prime_array,"prime_array")

# original_list = [1, 2, 2, 3, 4, 4, 5, 1]

# uniqueList=[]

# for  item in original_list:
#     if item not in uniqueList:
#         uniqueList.append(item)
    
# print(uniqueList,"UniqueList")

# stringss="hey There !"

# reversed_string =""
# for char in stringss:
#     reversed_string = char+reversed_string

# print(reversed_string)
    


# tuples=(1,2,(3,4,5),8,(2,910,10))


# def flattentupple(nested):
#     flat_list=[]
#     for i in nested:
#         if isinstance(i, tuple):
#             for i in i:
#                 flat_list.append(i)
#         else:
#             flat_list.append(i)
#     return tuple(flat_list)

# print(flattentupple(tuples))
# class Employee:
#     salary= 234
#     increment= 50
#     @property
#     def salaryAfterIncrement(self):
#         return self.salary + (self.salary* self.increment)/100
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, salary):
#         self.increment = ((self.salary/self.salary-1))*100


# e = Employee()
# print(e.salary)

# print(e.salaryAfterIncrement)
# print(e.salaryAfterIncrement)
# class Animal:
#     pass

# class Pets(Animal):
#     @staticmethod
#     def bark():
#         print("Bow Bow!")

# class Dog(Pets):
#     pass


# d= Dog()

# d.bark()


# class TwodVector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
#     def show(self):
#         print(f"The vector is {self.i} + {self.i}")

# class ThreedVector(TwodVector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
#     def show(self):
#         print(f"The vector is {self.i} + {self.i} + {self.k}")

# o= TwodVector(1,2)
# o.show()
# b= ThreedVector(1,2,3)
# b.show()