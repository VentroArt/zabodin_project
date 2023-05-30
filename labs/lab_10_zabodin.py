# print("Example 1")


# def ispalindrom(text):
#     text = text.replace(" ", "").lower()
#     if text == text[::-1]:
#         print("It's a palindrom")
#     else:
#         print("It's not a palindrom")


# text = input("Введіть текст:")
# ispalindrom(text)

# text = input("Введіть текст:")
# ispalindrom(text)

# print("Example 2")
# text1 = input("Введіть перше слово:")
# text2 = input("Введіть друге слово:")

# text1 = list(text1.replace(" ", "").lower())
# text2 = list(text2.replace(" ", "").lower())

# if sorted(text1) == sorted(text2):
#     print("Анаграми")
# else:
#     print("Не анаграми")

# print("Example 3")
# while True:
#     sum = 0
#     for simbol in date:
#         sum += int(simbol)

#     date = str(sum)

#     if len(date) == 1:
#         break

# print(sum)
# import string
# import random
# print("Task 1")

# word = "dog"


# def get_random_string(length):
#     letters = string.ascii_lowercase
#     result_str = ''.join(random.choice(letters) for i in range(length))
#     return result_str

# customString = get_random_string(16)


# def check_string_by_string(string_one, string_two):
#     result = True
#     list_of_letters = list(string_one)
#     for letter in list_of_letters:
#         if string_two.find(letter) == -1:
#             result = False
#     return result

# def get_the_answer():
#     if check_string_by_string(word, customString):
#         print("Yes")
#     else:
#         print("No")

# get_the_answer()

print("Example 4")
while True:
    try:
        number = int(input(" Введіть ціле число: "))
        print(number/2)
        break
    except:
        print("Введене значення не є допустимим числом. Повторіть спробу...")
