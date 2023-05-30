# Приклад 1
print("Приклад 1")


def copy_split(line):
    line = line.strip()
    list = []
    if line.isspace() or line == "":
        return list
    word = ""
    for letter in line:
        if letter == " ":
            list.append(word)
            word = ""
        else:
            word += letter
    list.append(word)
    return list


print(copy_split("Test Test1"))
