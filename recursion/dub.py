"""
EXAMPLE 1:
==============
total_combinations = calculate_combinations([5, 5, 15, 10], target_sum=15)
ANSWER 1:
====================
should return 3, as there are 3 combinations of numbers from the input
array that add up to 15, namely:
15
5+10
5+10
"""

def combi_nums_sum(number, target, partial=[]):
    if