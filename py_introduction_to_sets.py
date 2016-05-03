X = raw_input()
nums = raw_input()
nums = map(float, nums.split())

print sum(set(nums)) * 1.0 / len(set(nums))
