from collections import Counter

# Get count of shoes
X = int(raw_input())

# Get inventory of shoes and store as Counter Inventory
Inventory = Counter(map(int, raw_input().split()))

# Get count of customers
N = int(raw_input())

Sales = int(0)
for n in range(N):
	# Get customer order
	Size, Price = map(int, raw_input().split())

	# See if order can be filled
	if Inventory[Size] > 0:
		Sales = Price + Sales
		Inventory[Size] -= 1

print Sales

