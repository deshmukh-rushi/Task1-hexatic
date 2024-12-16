# Task 4: Set - Unique Words in a Text
# Write a Python program that uses a set to store u
# nique words from a text input. The program should ignore cases 
# and count the number of unique words.


class Set():
    def __init__(self):
        self.unique = set()
    def words(self):
        inpt = input("Enter words or line : ")
        inpt.lower().strip()
        words = inpt.split()
        self.unique.update(words)
        print(f"unique words are {self.unique}")
        print(f"length is {len(self.unique)}")
a = Set()
a.words()