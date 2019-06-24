"""Given an integer n and a list of integers l,
write a function that randomly generates a number
from 0 to n-1 that isn't in l (uniform). """

import random

my_list = [1, 2, 3, 5]

def gen_rand_num(n, l):
    generated_num = random.choice(range(0, n-1))
    while generated_num in l:
        generated_num = random.choice(range(0,n-1))
    return generated_num


print(gen_rand_num(10, my_list))
