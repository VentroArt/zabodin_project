# Завдання 1
print("Завдання 1")

list = [i for i in range(1, 101)]
n = int(input("Enter N: "))
uniq_list = []
for i in list:
    if i < n:
        uniq_list.append(i)

print(uniq_list)

# Завдання 2
print("Завдання 2")

list = ("R", "I", "P")

# option 1
result = ""
for index, i in enumerate(list):
    if index == len(list) - 1:
        result += i
    else:
        result += i + ','
print(result)
# option 2
print(",".join(list))
# option 3
print(f"{list[0]},{list[1]},{list[2]}")

# Завдання 3
print('Задання 3')
library = {}
while True:
    book_name = input("Введіть назву книги або Х щоб вийти із программи: ")
    if book_name == "X":
        break
    library[book_name] = ""
    book_author = input("Введіть автора книги: ")
    book_release_year = input("Введіть рік видання книги: ")
    book_pages = input("Введіть кількість сторінок: ")
    library[book_name] = f"Автор \"{book_author}\" надрукована у {book_release_year} році, {book_pages} сторінок"
    print("Наразі ваша бібліотека книг має: ")
    for book in library:
        # print(book)
        print(f"{book} - {library[book]}")

# Завдання 4
print("Завдання 4")
students = {
    "Ivanov": (20, "male", "informatics"),
    "Petrov": (22, "male", "mathematics"),
    "Sidorov": (19, "female", "bilogy"),
}

search = input("Введіть прізвище студента: ")
if students[search]: 
    result = ""
    for i in students[search]:
        result += str(i) + " "
    print(result)
else:
    print("Такого студента в нас немає")
