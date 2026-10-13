# 175. Combine Two Tables
# Difficulty: Easy
# https://leetcode.com/problems/combine-two-tables/
# Time: O(n) | Space: O(n)
import pandas as pd


# My solution – SQL LEFT JOIN
# SELECT
#     Person.firstName,
#     Person.lastName,
#     Address.city,
#     Address.state
# FROM Person
# LEFT JOIN Address
#     ON Person.personId = Address.personId


# Pandas version
def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result = person.merge(address, how='left', on='personId')
    return result[['firstName', 'lastName', 'city', 'state']]
