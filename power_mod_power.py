a = int(raw_input())
b = int(raw_input())
m = int(raw_input())

assert a >= 1 and a <= 10
assert b >= 1 and b <= 10
assert m >= 2 and m <= 1000

print pow(a,b)
print pow(a,b,m)