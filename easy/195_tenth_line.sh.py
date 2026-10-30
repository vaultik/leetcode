# 195. Tenth Line
# Difficulty: Easy
# https://leetcode.com/problems/tenth-line/
# Time: O(n) | Space: O(1)

# My solution – sed
# sed -n 10p file.txt

# Alternative – awk
# awk 'NR == 10 {print}' file.txt

# Alternative – tail + head
# tail -n +10 file.txt | head -n 1
