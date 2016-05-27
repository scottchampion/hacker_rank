def p_decorate(number):
    """Receives a 10 char number and exports it in the following format
       +91 XXXXX XXXXX"""
    assert len(number) == 10
    return "+91 %s %s" % (number[0:5], number[-5:])

def n_standard(num_string):
    """Returns the right 10 digits of the string passed"""
    return num_string[-10:]

X = []

for i in range(int(raw_input())):
    X.append(n_standard(raw_input()))

X.sort()

for i in X:
    print p_decorate(i)