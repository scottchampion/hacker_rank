from itertools import product

A = map(int, raw_input().split())
B = map(int, raw_input().split())

print str(list(product(A, B))).strip('[]').replace('),', ')')