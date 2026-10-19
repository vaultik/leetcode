# 182. Duplicate Emails
# Difficulty: Easy
# https://leetcode.com/problems/duplicate-emails/
# Time: O(n) | Space: O(n)
import pandas as pd


# My solution – SQL self JOIN
# SELECT DISTINCT per1.email AS Email
# FROM Person AS per1
# JOIN Person AS per2 ON per1.email = per2.email
# WHERE per1.id < per2.id

# Alternative SQL – GROUP BY + HAVING
# SELECT Person.email AS Email
# FROM Person
# GROUP BY email
# HAVING COUNT(email) > 1


# Pandas – duplicated()
def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    dup_rows = person[person.duplicated(subset=['email'])]
    return dup_rows[['email']].drop_duplicates().rename(columns={'email': 'Email'})


# Pandas – groupby
def duplicate_emails_groupby(person: pd.DataFrame) -> pd.DataFrame:
    grouped = person.groupby('email').size().reset_index(name='count')
    return grouped[grouped['count'] > 1][['email']].rename(columns={'email': 'Email'})
