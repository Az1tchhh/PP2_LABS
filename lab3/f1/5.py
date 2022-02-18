from itertools import permutations
def permutation(str):
    a = str.split()
    perm = permutations(a)
    for i in perm:
        print(i)
str = input()
permutation(str)