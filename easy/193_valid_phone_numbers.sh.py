# 193. Valid Phone Numbers
# Difficulty: Easy
# https://leetcode.com/problems/valid-phone-numbers/
# Time: O(n) | Space: O(1)

# My solution – grep with Perl regex
grep -P '^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$|^[0-9]{3}-[0-9]{3}-[0-9]{4}$' file.txt

# Alternative – awk
awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/' file.txt

# Alternative – sed
sed -nE '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/p' file.txt
