"""Assume you have access to a function toss_biased()
which returns 0 or 1 with a probability that's not 50-50
 (but also not 0-100 or 100-0). You do not know the bias
 of the coin.

Write a function to simulate an unbiased coin toss.
"""
import random

unknown_ratio_heads = random.randint(1,100)
unknown_ratio_tails = 100-unknown_ratio_heads


def coin_toss(tosses):
    heads_count = 0
    tails_count = 0
    weighted_probabilities = unknown_ratio_heads * ['Heads'] + unknown_ratio_tails * ['Tails']
    for x in range(tosses):
        toss = random.choice(weighted_probabilities)
        if toss == 'Heads':
            heads_count += 1
        else:
            tails_count += 1
    ratio_tails = (tails_count / tosses) * 100
    ratio_heads = (heads_count / tosses) * 100
    print(str(heads_count) + " of the " + str(tosses) + " tosses were heads. That is " + str(ratio_heads) + " percent.")
    print(str(tails_count) + " of the " + str(tosses) + " tosses were tails. That is " + str(ratio_tails) + " percent.")
    print("The unknown probability of getting heads was " + str(unknown_ratio_heads) +". How close were you?")


coin_toss(10000)
#heads = 1, tails = 2
