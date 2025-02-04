"""
Write a function that receives two words (String) and returns
true or false (Bool) depending on whether they are anagrams or not.
An Anagram consists of forming a word by rearranging ALL
the letters of another original word.
It is NOT necessary to check whether both words exist.
Two identical words are not considered anagrams.
"""

def are_anagrams(word1, word2):
    # Ensure both words are lowercase and not the same
    if word1.lower() == word2.lower():
        return False
    # Check if sorted letters of both words are the same
    return sorted(word1.lower()) == sorted(word2.lower())


print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
print(are_anagrams("abc", "cab"))        # True
print(are_anagrams("test", "test"))     # False