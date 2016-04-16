X = raw_input()
# Print True if *any* character is alphanumeric

def any_isalnum(X):
	"""Returns True if *any* values in X are alphanumeric"""
	for each in X:
		if each.isalnum() == True:
			return True
		else:
			continue
	return False

def any_isalpha(X):
	"""Returns True if *any* values in X are alphabetical"""
	for each in X:
		if each.isalpha() == True:
			return True
		else:
			continue
	return False

def any_isdigit(X):
	"""Returns True if *any* values in X are numeric digits"""
	for each in X:
		if each.isdigit() == True:
			return True
		else:
			continue
	return False

def any_islower(X):
	"""Returns True if *any* values in X are lower case"""
	for each in X:
		if each.islower() == True:
			return True
		else:
			continue
	return False

def any_isupper(X):
	"""Returns True if *any* values in X are upper case"""
	for each in X:
		if each.isupper() == True:
			return True
		else:
			continue
	return False

print any_isalnum(X)
print any_isalpha(X)
print any_isdigit(X)
print any_islower(X)
print any_isupper(X)