x = list(range(1, 10000))
user_input = int(input("Please insert number: "))

divide_list = []

for b in x:
    if user_input % b == 0:
        divide_list.append(b)
print(divide_list)
