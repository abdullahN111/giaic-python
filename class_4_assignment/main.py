# Problem 1: Reverse a String

inp = input("Write something to reverse: ")

def reverse_str(string1):
    return string1[::-1]  

print(reverse_str(inp))



# Problem 2: Count Vowels in a String

word = input("Write a word to count vowels in it: ")
vowels = ["a", "e", "i", "o", "u"]

def count_vowels(vowel):
    count = 0
    for char in word.lower():
        if char in vowels:
            count += 1
            
    print(f"There are {count} vowels in word {vowel}.")
   
count_vowels(word)



# Problem 3: Sum of Digits

digits = int(input("Write numbers: "))

def sum_of_digits(nums):
    total = sum(int(digit) for digit in str(nums))
    return total

print(sum_of_digits(digits))
    
    