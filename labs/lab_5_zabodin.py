# Завдання 1
print("Завдання 1")
hat_list = [1, 2, 3, 4, 5]

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
inputNumber = int(input('Write a number to replace the middle number'))
hat_list[int(len(hat_list) // 2)] = inputNumber
print(hat_list)
# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]
print(hat_list)

# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))


"""
Поряд з можливістю реалізувати будь-який алгоритм сортування,
 у python існують вбудовані методи для сортування списків.
[0, 1, 7, 23, 34]
[34, 23, 7, 1, 0]
"""
array_1 = [1, 7, 0, 23, 34]
array_1.sort()
print("Sorted array_1", array_1)
array_1.reverse()
print("Reverse sorted array_1", array_1)

# Завдання 2
print("Завдання 2")
"""
Написати програму сортування списку у порядку зростання методом бульбашки.
"""
array_2 = [6, 8, 10, 2, 4]

was_swapped = True

while (was_swapped):
    swapped = False
    for x in range(len(array_2) - 1):
        if array_2[x] > array_2[x + 1]:
            swapped = True
            array_2[x], array_2[x+1] = array_2[x + 1], array_2[x]
            print(array_2)

print("Результат сортування списку у порядку зростання методом бульбашки", array_2)

# Завдання 3
print("# Завдання 3")

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
uniq = []

for i in my_list:
    if i not in uniq:
        uniq.append(i)

print("The list with unique elements only:")
print(uniq)

# Завдання 4
print("# Завдання 4")
board = [["_" for h in range(8)] for d in range(8)]

board[0][0] = "Тура 1"
board[0][7] = "Тура 2"
board[7][0] = "Тура 3"
board[7][7] = "Тура 4"
print(board)
