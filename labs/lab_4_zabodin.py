import time
# Завданная 1
print("Завдання 1")
n = float(input("Input N: "))
print(bool(n >= 100))

# Завдання 2
print("Завдання 2")
num_1 = float(input('Input number 1: '))
num_2 = float(input('Input number 2: '))
if num_1 > num_2:
    print(num_1)
else:
    print(num_2)

# Завдання 3
print("Завдання 3")
line = input("Type anything: ")
if line == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!”")
elif line == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {line}!")

# Завдання 4
print("Завдання 4")
income = float(input("Tell us your income: "))
free_income = 85528
tax = 0
if income <= free_income:
    tax = round(income / 100 * 18 - 556.2, 0)
else:
    tax = round((income - free_income) / 100 * 32 + 14839.2)
print("The tax is:", tax, "thalers")

# Завдання 5
print("Завдання 5")
year = int(input('Type year: '))

if year < 1582:
    print("Not within the Gregorian calendar period.")
elif year % 4 != 0:
    print("Common year")
elif year % 100 != 0:
    print("Leap year")
elif year % 400 == 0:
    print("Leap year")
else:
    print("Common year")

# Завдання 6
print("Завдання 6")

secret_number = 777
did_he_guess = False
print("""
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)

while did_he_guess == False:
    number = int(input())
    if number == secret_number:
        did_he_guess = True
        print("Молодець, магле! Тепер ти вільний")
        break
    print("Ха-ха! Ви застрягли у моїй петлі!")

# Завдання 7
print("Завдання 7")
for i in range(5):
    if i <= 5:
        print(f"{i + 1} Mississippi")
        time.sleep(1)

# Завдання 8
print("Завдання 8")
secret_word = "chupacabra"
word = ""

while word != secret_word:
    word = input("")
    if word == secret_word:
        print("You've successfully left the loop")
        break  # not necessary here cause of condition for while

# Завдання 9
print("Завдання 9")
user_word = input("Type the word please: ").upper()

for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    else:
        print(letter)

# Завдання 10
print("Завдання 10")
user_word = input("Type the word please: ").upper()
new_word = ""
for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    else:
        new_word += letter
print(new_word)

# Завдання 11
print("Завдання 11")
number = int(input("Тож скільки у вас цеглинок?"))
height = 0
in_use = 1

while in_use <= number:
    if number >= in_use + height + 1:
        height += 1
        in_use += height
    else:
        break

print("Що ж, висота пірамідки: ", height)

# Завдання 12

print("Завдання 12")
c0 = int(input('Введіть с0'))
steps = 0

while c0 != 1:
    steps += 1
    if c0 % 2 == 0:
        c0 = c0 / 2
    else:
        c0 = 3 * c0 + 1

print("Кроків зроблено ", steps)
