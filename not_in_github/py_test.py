s = "010230849100001000000100000000012800000100240000000000000000000000000000"
numbers = [int(s[i:i+2]) for i in range(0, len(s), 2)]
print(numbers)
print(len(s))
# [1, 2, 30, 84, 91, 0, 0, 10, 0, 0, 1, 0, 0, 0, 0, 1, 28, 0, 0, 1, 0, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]