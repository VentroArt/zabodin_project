import sys
# Завдання 1
PI = 3.14
MU = 1
sigma = 2
x = 5
epsilon = sys.float_info.epsilon

gaus = (1 / sigma * ((2 * PI) ** 0.5)) * epsilon ** - \
    (((x - MU) ** 2) / (2 * (sigma ** 2)))

print(gaus)

# Завдання 2

john, mary, adam = 3, 5, 6
totalApple = john + mary + adam
print("Total Apple: ",  totalApple)

# Завдання 3
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# Завдання 4
x = int(input("Введіть значення 'x' "))
y = 3 * (x ** 3) - 2 * (x ** 2) + 3 * x - 1
print("Ми порахували для вас значення 'y': ", y)

# Завдання 5

# this program computes the number of seconds in a given number of hours
hours = 2
seconds = 60 * 60  # number of seconds in 1 hour

print("Hours: ", hours)
print("Seconds in Hours: ", hours * seconds)
print("Goodbye")
# this is the end of the program that computes the number of seconds in 2 hour

# Завдання 6
a = float(input("input a float value for variable a here "))
b = float(input("input a float value for variable b here "))

print("output the result of addition here ", a + b)
print("output the result of subtraction here ", a - b)
print("output the result of multiplication here ", a * b)
print("output the result of division here ", a / b)

print("\nThat's all, folks!")

# Завдання 7
x = float(input("Enter value for x: "))
y = 1 / (x + (1 / (x + (1 / (x + (1 / (x + 1 / x)))))))

print("y =", y)

# Завдання 8
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
duration = int(input("Event duration (minutes): "))

new_time = str(int((hour + ((mins + duration) / 60) % 24) % 24)) + \
    ":" + str((mins + duration) % 60)
print(new_time)
