"""Given an array of numbers, find the length of the longest
increasing subsequence in the array. The subsequence does not
necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6,
 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing
 subsequence has length 6: it is 0, 2, 6, 9, 11, 15.

 """

 # Thoughts : make a function that finds if an array is
 # increasing (i+1 > i) and then keeps a record of the
 # longest subsequence.

my_array = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]



def is_increasing(seq):
    count = 0
    thing = []
    for i in range(len(seq)-1):
        if seq[i] > seq[i+1]:
            count += 1
            thing.append(seq[i])
        else:
            pass
    return thing

print(is_increasing(my_array))


# so this doesn't match the answer I'm supposed to get,
# but I am also not understanding how they got the subsequence
# [0, 2, 6, 9, 11, 15] for their answer. So mine kind of works,
# It just lets you know what values are larger than the
# value directly preceeding them. 
