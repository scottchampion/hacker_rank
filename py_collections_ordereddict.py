from collections import OrderedDict

day_sales = OrderedDict()

for i in range(int(raw_input())):
	item_name, net_price = raw_input().rsplit(' ', 1)
	try: day_sales[item_name] += int(net_price)
	except: day_sales[item_name] = int(net_price)

#for item_name, total_sales in day_sales.iteritems():
#	print item_name, total_sales
for item_name in day_sales:
	print item_name, day_sales[item_name]