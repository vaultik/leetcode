# 190. Reverse Bits
# Difficulty: Easy
# https://leetcode.com/problems/reverse-bits/
# Time: O(1) | Space: O(1)
from functools import cache


# My solution – bit-by-bit loop (solved with AI hints)
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            result <<= 1
            result += n & 1
            n >>= 1

        return result


# Optimized version – byte-by-byte with cache
class SolutionCached:
    @cache
    def reverseByte(self, byte: int) -> int:
        res = 0
        for _ in range(8):
            res = (res << 1) | (byte & 1)
            byte >>= 1
        return res

    def reverseBits(self, n: int) -> int:
        byte1 = self.reverseByte(n & 0xff)
        byte2 = self.reverseByte((n >> 8) & 0xff)
        byte3 = self.reverseByte((n >> 16) & 0xff)
        byte4 = self.reverseByte((n >> 24) & 0xff)
        return (byte1 << 24) | (byte2 << 16) | (byte3 << 8) | byte4


# Bit manipulation – divide and conquer swap
class SolutionBitSwap:
    def reverseBits(self, n: int) -> int:
        n = ((n >> 16) & 0x0000FFFF) | ((n << 16) & 0xFFFF0000)
        n = ((n >> 8) & 0x00FF00FF) | ((n << 8) & 0xFF00FF00)
        n = ((n >> 4) & 0x0F0F0F0F) | ((n << 4) & 0xF0F0F0F0)
        n = ((n >> 2) & 0x33333333) | ((n << 2) & 0xCCCCCCCC)
        n = ((n >> 1) & 0x55555555) | ((n << 1) & 0xAAAAAAAA)
        return n
