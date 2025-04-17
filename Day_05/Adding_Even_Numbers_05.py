# Even number total count 
# even = 0
# odd = 0 
# for i in range (0, 100):
#     if i % 2 == 0:
#         even += 1
#         # print(even)
# #     else:
# #         odd += 1
# print(f"Even number total count {even}")

total = 0 
for number in range(2, 101, 2):
    total += number
print(total)

total2 = 0 
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)