import math

def dot(a, b):
	c = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
	return c

def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return c

A = map(float, raw_input().split())
B = map(float, raw_input().split())
C = map(float, raw_input().split())
D = map(float, raw_input().split())

AB = [B[0] - A[0], B[1] - A[1], B[2] - A[2]]
BC = [C[0] - B[0], C[1] - B[1], C[2] - B[2]]
CD = [D[0] - C[0], D[1] - C[1], D[2] - C[2]]

#print "AB", AB
#print "BC", BC
#print "CD", CD

X = cross(AB, BC)
Y = cross(BC, CD)
absX = math.sqrt(X[0]**2 + X[1]**2 + X[2]**2)
absY = math.sqrt(Y[0]**2 + Y[1]**2 + Y[2]**2)

print round(math.degrees(math.acos(dot(X, Y) / (absX * absY))), 2)