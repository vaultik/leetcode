# 564. Find the Closest Palindrome
# Difficulty: Hard
# https://leetcode.com/problems/find-the-closest-palindrome/
# Time: O(n) | Space: O(n)


# Сandidate generation: edge cases + prefix ±1
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        n_length = len(n)
        num = int(n)

        if n_length == 1:
            return str(num - 1) if num > 0 else '0'

        candidates = set()
        candidates.add(10 ** (n_length - 1) - 1)
        candidates.add(10 ** n_length + 1)

        prefix_len = (n_length + 1) // 2
        prefix = int(n[:prefix_len])

        for delta in (-1, 0, 1):
            p = str(prefix + delta)
            if len(p) != prefix_len:
                continue
            candidate = p + p[::-1] if n_length % 2 == 0 else p + p[:-1][::-1]
            candidates.add(int(candidate))

        candidates.discard(num)

        best = None
        for c in candidates:
            if c < 0:
                continue
            if (
                best is None
                or abs(c - num) < abs(best - num)
                or (abs(c - num) == abs(best - num) and c < best)
            ):
                best = c

        return str(best)
