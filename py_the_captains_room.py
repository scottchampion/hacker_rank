# Gather user input.
K = int(raw_input())
room_assignments = map(int, raw_input().split())

# Make set of occupied rooms
occupied_rooms_set = set(room_assignments)

for i in occupied_rooms_set:
	try:
		# able to remove i from room_assignments twice, not captain's room
		room_assignments.remove(i)
		room_assignments.remove(i)
		continue
	except:
		# unable to remove i from room_assignments twice. found captain's room
		print i
		break