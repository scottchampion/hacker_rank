from collections import Counter

L = Counter(raw_input())
C = L.most_common(3)

print L
print C
for letter, counts in sorted(C, key = lambda x:(-x[1],x[0])):
    print letter, counts