# 全域變數與區域變數

length = 5  # 全域變數


def calculate_square_area1():
    area = length * length  # 區域變數
    print("面積是", area)


calculate_square_area1()


length = 5  # 全域變數


def calculate_square_area2():
    area = length * length  # 區域變數
    print("面積是", area)


length = 10  # 全域變數

calculate_square_area2()

# print("_" * 30)

# length = 5  # 全域變數


# def calculate_square_area3():
# area = length * length  # 區域變數


# length = 10  # 全域變數
# calculate_square_area3()
# print("面積是", area)


print("_" * 30)

length = 5  # 全域變數
area = 3.14 * 10**2  # 全域變數


def calculate_circle_area4():
    area = length * length


calculate_circle_area4()
print("面積是", area)

# print("_" * 30)

# length = 5  # 全域變數
# area = 3.14 * 10**2  # 全域變數


# def calculate_circle_area5():
#     print("面積是", area)
#     area = length * length
#     print("面積是", area)


# calculate_circle_area5()

print("_" * 30)

length = 5  # 全域變數
area = 3.14 * 10**2  # 全域變數


def calculate_circle_area6():
    area = length * length
    return area


area = calculate_circle_area6()
print("面積是", area)

print("_" * 30)

length = 5  # 全域變數
area = 3.14 * 10**2  # 全域變數


def calculate_circle_area7():
    global area
    area = length * length


calculate_circle_area7()
print("面積是", area)
