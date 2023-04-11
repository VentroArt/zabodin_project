# Завдання 1
print("Завдання 1")


def is_year_leap(year):
    if year < 1582:
        print('Too early')
        return
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

# Завдання 2
print("Завдання 2")


def days_in_month(year=1900, month=2):
    if type(year) != int:
        return None
    elif type(month) != int:
        return None
    else:
        february = 28
        if is_year_leap(year):
            february = 29
        days = [
            31, february, 31,
            30, 31, 30,
            31, 31, 30,
            31, 30, 31
        ]
        return days[month - 1]


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

# Завдання 3
print("Завдання 3")

def day_of_year(year, month, day):
    if type(year) != int or type(month) != int or type(day) != int:
        return None
    february = 28
    if is_year_leap(year):
        february = 29
    days = [
        31, february, 31,
        30, 31, 30,
        31, 31, 30,
        31, 30, 31
    ]
    sum = 0
    for idx, i in enumerate(days, start=0):
        if idx < month - 1:
            sum += days[idx]
    sum += day
    return sum


print(day_of_year(2000, 12, 31))

# Завдання 4
print("Завдання 4")


def is_prime(number):
    prime = False
    for num in range(0, number + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    prime = False
                    break
                else:
                    prime = True
    return prime


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")

# Завдання 5
print("Завдання 5")
# 1 американська міля = 1609.344 метрів;
# 1 американський галон = 3.785411784 літрів.

def liters_100km_to_miles_gallon(liters):
    galons = liters / 3.785411784
    miles = 100 / 1.609344
    return miles / galons


def miles_gallon_to_liters_100km(miles):
    liters = 3.785411784
    kilometers = miles * 1.609344
    return liters / kilometers * 100


print(liters_100km_to_miles_gallon(3.9))  # 60.31143162393162
print(liters_100km_to_miles_gallon(7.5))  # 31.36194444444444
print(liters_100km_to_miles_gallon(10.))  # 23.52145833333333
print(miles_gallon_to_liters_100km(60.3))  # 3.9007393587617467
print(miles_gallon_to_liters_100km(31.4))  # 7.490910297239916
print(miles_gallon_to_liters_100km(23.5))  # 10.009131205673757

# Завдання 6
print("Завдання 6")

def is_a_triangle(a, b, c):
    if a + b < c or b + c < a or c + a < b:
        return False
    return True


a = float(input("Введіть А: "))
b = float(input("Введіть Б: "))
c = float(input("Введіть В: "))

if is_a_triangle(a, b, c):
    print("Так, це може бути трикутник")
else:
    print("Ні, це не може бути трикутник")
# Завдання 7
print("Завдання 7")

def is_a_right_triangle(a, b, c):
    if is_a_triangle(a, b, c) == False:
        return False
    if a ** 2 + b ** 2 == round(c ** 2, 4):
        return True
    else:
        return False


if is_a_right_triangle(a, b, c):
    print("Це ще й прямокутний трикутник")
else:
    print("Але нажаль цей трикутник не прямокутний")
