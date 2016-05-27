from operator import itemgetter

def format_name(first, last, gender):
    def gender_prefix():
        return ('Mr. ' if gender == 'M' else 'Ms. ')
    return gender_prefix() + first + ' ' + last

L =[]

for i in range(int(raw_input())):
    L.append(raw_input().split())

L.sort(key=itemgetter(2))

for i in L:
    print format_name(i[0], i[1], i[3])

