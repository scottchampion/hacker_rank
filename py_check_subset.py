S = ''
for i in range(int(raw_input())): #More than 4 lines will result in 0 score. Blank lines won't be counted.  
    a = int(raw_input()); A = set(raw_input().split()); b = int(raw_input()); B = set(raw_input().split()); B &= A; S += str(A == B) + '\n'
print S.strip()