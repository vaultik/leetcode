# 181. Employees Earning More Than Their Managers
# Difficulty: Easy
# https://leetcode.com/problems/employees-earning-more-than-their-managers/
# Time: O(n) | Space: O(n)
import pandas as pd


# My solution – SQL self JOIN
# SELECT employer.name AS Employee
# FROM Employee AS employer
# JOIN Employee AS manager ON employer.managerId = manager.id
# WHERE employer.salary > manager.salary


# Pandas version
def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    inner_joined_df = employee.merge(
        employee,
        left_on='managerId',
        right_on='id',
        suffixes=('_employer', '_manager')
    )
    filtered_df = inner_joined_df[
        inner_joined_df['salary_employer'] > inner_joined_df['salary_manager']
    ]
    return filtered_df[['name_employer']].rename(columns={'name_employer': 'Employee'})
