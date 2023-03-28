# Завдання 1
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
