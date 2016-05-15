# Get the number of students subscribed to English
n = raw_input()

# Get the n space-separated role numbers of English subscriber students
sub_en = set(map(int, raw_input().split()))

# Get the number of students subscribed to French
b = raw_input()

# Get the b space-separated role numbers of French subscriber students
sub_fr = set(map(int, raw_input().split()))

# Print the length of the intersection of sub_en and sub_fr
print len(sub_en | sub_fr)