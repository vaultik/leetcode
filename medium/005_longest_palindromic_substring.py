# 5. Longest Palindromic Substring
# Difficulty: Medium
# https://leetcode.com/problems/longest-palindromic-substring/
# Time: O(n²) | Space: O(1)


# My solution – expand around center (odd + even)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        result = ''

        for i in range(len(s) - 1):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            result = s[left + 1:right] if len(s[left + 1:right]) > len(result) else result

            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            result = s[left + 1:right] if len(s[left + 1:right]) > len(result) else result

        return result


# Optimized version – Manacher's algorithm, O(n) time
# Time: O(n) | Space: O(n)
class SolutionManacher:
    def longestPalindrome(self, s: str) -> str:
        T = '^#' + '#'.join(s) + '#$'
        n = len(T)
        P = [0] * n

        center = 0
        right = 0

        for i in range(1, n - 1):
            i_mirror = 2 * center - i

            if right > i:
                P[i] = min(right - i, P[i_mirror])

            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > right:
                center = i
                right = i + P[i]

        max_len = max(P)
        center_index = P.index(max_len)
        start = (center_index - max_len) // 2

        return s[start: start + max_len]
