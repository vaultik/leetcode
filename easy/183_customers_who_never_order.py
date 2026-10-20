# 183. Customers Who Never Order
# Difficulty: Easy
# https://leetcode.com/problems/customers-who-never-order/
# Time: O(n) | Space: O(n)
import pandas as pd


# My solution – SQL LEFT JOIN + IS NULL
# SELECT Customers.name AS Customers
# FROM Customers
# LEFT JOIN Orders ON Customers.id = Orders.customerId
# WHERE Orders.customerId IS NULL

# Alternative SQL – NOT IN subquery
# SELECT name AS Customers
# FROM Customers
# WHERE id NOT IN (
#     SELECT customerID
#     FROM Orders
# )


# Pandas – merge + isna
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = customers.merge(orders, how='left', left_on='id', right_on='customerId')
    result = result[result['customerId'].isna()]
    return result[['name']].rename(columns={'name': 'Customers'})


# Pandas – isin mask, cleaner
def find_customers_mask(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    mask = ~customers['id'].isin(orders['customerId'])
    return customers[mask][['name']].rename(columns={'name': 'Customers'})
