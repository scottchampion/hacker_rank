from collections import deque

d = deque()
# Prompt user for the number of commands to expect
for i in range(int (raw_input())):

    # Store the command as a list (regardless of input parameters)
    command = raw_input().split()
    
    # Run the command
    if command[0] == 'append':
        d.append(command[1])
    elif command[0] == 'appendleft':
        d.appendleft(command[1])
    elif command[0].strip() == 'pop':
        d.pop()
    elif command[0] == 'popleft':
        d.popleft()
    else:
        print command[0], 'not recognized'

# Format the deque for output
print ' '.join(d)