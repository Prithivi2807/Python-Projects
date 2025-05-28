import math
# number_of_cans =(wall_height * wall_width) / coverage_per_can

test_h = int(input("Height of wall: "))
test_w = int(input("width of wall: "))
coverage = 5

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = area / cover
    num_of_cans = math.ceil(area / cover)
    print(f"you'll need {num_of_cans} cans of paint")
    # Either
    # number_of_can_paint = (height * width) / cover
    # x = round(number_of_can_paint)
    # print(f"You'll need {x} cans of paint")


paint_calc(height=test_h, width=test_w, cover=coverage)
