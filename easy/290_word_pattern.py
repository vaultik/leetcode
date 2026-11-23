# 290. Word Pattern
# Difficulty: Easy
# https://leetcode.com/problems/word-pattern/
# Time: O(n) | Space: O(n)


# My solution – two dicts + used_words set
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False

        used_words = set()
        char_to_word = dict()

        for i, char in enumerate(pattern):
            if char not in char_to_word:
                if words[i] in used_words:
                    return False
                used_words.add(words[i])
                char_to_word[char] = words[i]
            else:
                if char_to_word[char] != words[i]:
                    return False

        return True


# Optimized version – setdefault bidirectional check
class SolutionSetDefault:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word, word_to_char = {}, {}
        for char, word in zip(pattern, words):
            if char_to_word.setdefault(char, word) != word:
                return False
            if word_to_char.setdefault(word, char) != char:
                return False
        return True


# Pythonic version – zip + set lengths
class SolutionZip:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        return (len(pattern) == len(words)
                and len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words))))
