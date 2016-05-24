from cmath import phase

# Total hack method to parce the polynomial expression
A = raw_input().replace('-', '+-').lstrip('+').replace('++', '+')
A = map(int, A.strip('j').split('+'))

# Print A
print abs(complex(A[0], A[1]))
print phase(complex(A[0], A[1]))