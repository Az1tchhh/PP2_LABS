def solve(numheads, numlegs):
    print (numlegs//2 - numheads)
    print (2*numheads - numlegs//2)
a,b = map(int, input().split())
solve(a,b)