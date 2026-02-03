print(len({}))  # 0
print(len({"蘋果"}))  # 1
print(len([1, 2, 3, 4, 5]))  # 5
print(({1, 2, 3,[4,5]}))  # 4

L1 = ["a", "b", "c"]

# 遍歷串例1
for i in range(len(L1)):
    print(L1[i])

# 遍歷串例2
for element in L1:
    print(element)

print("__" * 30)
a = {1, 2, 3,}
a.add(10)
print(a) # { 2, 3, 10}
 
print("__" * 30)
a = [1, 2, 3]
b = a
b[0] = 10
print(a) # [10, 2, 3]
print(b) # [10, 2, 3]

print("__" * 30)
L2 = [1, 2, 3]
L2.append(4)
print(L2)  # [1, 2, 3, 4]

L3 = [1, 2, 3, 4]
L3.remove(1)
print(L3)  # [2, 3, 1]
L3.remove(1)
print(L3)  # [2, 3, ]

L4 = [1, 2, 3, ]
L4.pop()
print(L4)  # [1, 2]
L4.pop(0)
print(L4)  # [2]

L5 = [3, 1, 4, 2, 5]                 
L5.sort()
print(L5)  # [1, 2, 3, 4, 5]
