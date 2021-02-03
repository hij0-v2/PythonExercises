def main_exercise3_with1st_extra():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    c = []

    for b in a:
        if b < 5:
            c.append(b)

    print(c)

def extra_one_liner():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print([b for b in a if b < 5])

def extra_user_input():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    user_input = int(input("Enter a number: "))

    for b in a:
        if b < user_input:
            print(b)

extra_user_input()