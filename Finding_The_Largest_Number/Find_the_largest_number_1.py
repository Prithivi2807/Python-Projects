largest_so_far = -1
print('before iteration', largest_so_far)
for random in [3, 22, 11, 55, 33, 66, 55, 63, 73]:
    if random > largest_so_far:
        largest_so_far = random
    print(largest_so_far, random)
print('after iteration', largest_so_far)
