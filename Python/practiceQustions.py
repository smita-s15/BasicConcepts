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



# string = "kobas"
# string2="boka"
# # count=[]

# def isAnagram():
#     return sorted(string)==sorted(string2)
# print(isAnagram())

# for char in string:
#     if string.count(char) == 1:
#         count.append(char)
# print(count)

# if string == string[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

# reversedString= ""

# for ch in string:
#     reversedString = ch+reversedString
    
# print(reversedString,"reversedString")
    



# def anagrams(str1, str2):
#     return sorted(str1)==sorted(str2)


# print(anagrams("listen", "silent"))  # True
# print(anagrams("hello", "world"))    # False


# string ="Hello There..."
# char_counts = {}
# # def getCountOfCharacter(str):
# for char in string:
#     if char in char_counts:
#         char_counts[char] += 1
#     else:
#          char_counts[char] = 1


# print(char_counts)


# string = "Hello There..."
# char_counts = {}

# for char in string:
#     if char in char_counts:
#         char_counts[char] += 1
#     else:
#         char_counts[char] = 1

# print(char_counts)

# import time

# def task(name):
#     print(f"Starting {name}")
#     time.sleep(2)  # blocking
#     print(f"Finished {name}")

# task("A")
# task("B")


# class Counter:
#     def __init__(self, limit):
#         self.limit = limit
#         self.current = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current < self.limit:
#             self.current += 1
#             return self.current
#         else:
#             raise StopIteration

# for num in Counter(5):
#     print(num)  # 1 2 3 4 5



# # def count_up_to(n):
# #     i = 1
# #     while i <= n:
# #         yield i
# #         i += 1

# # for num in count_up_to(5):
# #     print(num)  # Prints 1 2 3 4 5


# # def repeat_word(word, times):
# #     return word * times

# # print(repeat_word("HI", 3))  # "HiHiHi"
