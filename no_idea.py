toss = raw_input() # Toss the integer count

arry = map(int, raw_input().split()) # Input the array the test
A = map(int, raw_input().split())
B = map(int, raw_input().split())

A = set(A)
B = set(B)

happiness = 0
for i in arry:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1

print happiness