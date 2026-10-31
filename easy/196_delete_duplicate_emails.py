# 196. Delete Duplicate Emails
# Difficulty: Easy
# https://leetcode.com/problems/delete-duplicate-emails/
# Time: O(n log n) | Space: O(1)
import pandas as pd


# My solution – SQL DELETE with self JOIN
# DELETE
# FROM Person AS p1
# USING Person AS p2
# WHERE p1.email = p2.email AND p1.id > p2.id


# Pandas version – sort + drop_duplicates in-place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', ascending=True, inplace=True)
    person.drop_duplicates(subset='email', keep='first', inplace=True)
