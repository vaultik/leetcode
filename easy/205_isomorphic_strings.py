# 205. Isomorphic Strings
# Difficulty: Easy
# https://leetcode.com/problems/isomorphic-strings/
# Time: O(n) | Space: O(n)


# My solution – two dicts bidirectional mapping
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = dict()
        t_s = dict()

        for i in range(len(s)):
            if (t[i] in t_s and t[i] != s_t.get(s[i])) or (s[i] in s_t and s[i] != t_s.get(t[i])):
                return False
            else:
                t_s[t[i]] = s[i]
                s_t[s[i]] = t[i]

        return True


# Optimized version – zip + set one-liner
class SolutionClean:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
