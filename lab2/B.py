number = int(input())
myList_with_integers = [int(number) for number in input().split(' ')]
myList_with_integers.sort()
print( int( myList_with_integers[ number - 2 ] ) * int( myList_with_integers[ number - 1]) )
#sdfs