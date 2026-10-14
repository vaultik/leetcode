# 12. Integer to Roman
# Difficulty: Medium
# https://leetcode.com/problems/integer-to-roman/
# Time: O(1) | Space: O(1)


# My solution – digit-by-digit with key lookup
class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {
            1: 'I', 5: 'V', 10: 'X', 50: 'L',
            100: 'C', 500: 'D', 1000: 'M',
        }
        keys_list = list(romans.keys())
        num_list = list(str(num))
        idx = len(num_list) * 2 - 2
        result = []

        for num in num_list:
            num = int(num)

            if not 4 <= num <= 9:
                result.append(romans[keys_list[idx]] * num)
            elif num == 4 or num == 9:
                diff = 1 if num == 4 else 2
                result.append(romans[keys_list[idx]])
                result.append(romans[keys_list[idx + diff]])
            else:
                result.append(romans[keys_list[idx + 1]])
                result.append(romans[keys_list[idx]] * (num - 5))

            idx -= 2

        return ''.join(result)


# Optimized version – greedy subtraction with full symbol map
class SolutionGreedy:
    def intToRoman(self, num: int) -> str:
        roman_map = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }
        result = []

        for value, symbol in roman_map.items():
            while num >= value:
                result.append(symbol)
                num -= value

        return ''.join(result)
