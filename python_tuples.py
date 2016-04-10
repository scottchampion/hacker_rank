# Enter your code here. Read input from STDIN. Print output to STDOUT

length = int(raw_input())
string = raw_input()

# Split the string by space, convert to integer, store in tuple
T = tuple(int(n) for n in string.split())

# Export the has of the tuple
print hash(T)
