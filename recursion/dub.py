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
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print "sum(%s)=%s" % (partial, target)
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])

subset_sum([1,2,3,4],6)