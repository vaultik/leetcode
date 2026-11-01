# 197. Rising Temperature
# Difficulty: Easy
# https://leetcode.com/problems/rising-temperature/
# Time: O(n log n) | Space: O(n)
import pandas as pd


# My solution – SQL self JOIN on date + 1
# SELECT w2.id
# FROM Weather AS w1
# JOIN Weather AS w2 ON w2.recordDate = w1.recordDate + INTERVAL '1 day'
# WHERE w2.temperature > w1.temperature

# Alternative SQL – window function LAG
# SELECT id
# FROM (
#     SELECT id, temperature, recordDate,
#            LAG(temperature) OVER(ORDER BY recordDate) as prev_temp,
#            LAG(recordDate) OVER(ORDER BY recordDate) as prev_date
#     FROM Weather
# ) subquery
# WHERE temperature > prev_temp
#   AND recordDate = prev_date + INTERVAL '1 day'


# Pandas version – shift + mask
def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values(by='recordDate')
    weather['prev_temp'] = weather['temperature'].shift(1)
    weather['prev_date'] = weather['recordDate'].shift(1)

    mask = (
        (weather['temperature'] > weather['prev_temp']) &
        ((weather['recordDate'] - weather['prev_date']) == pd.Timedelta(days=1))
    )
    return weather[mask][['id']]
