# -- Data types --
number = 0
word = "word"
flag = False
floatas = 0.2

# -- Data structures --
phone_list = ["iphone 12", "samsung 20", "nokia 3310"]
tv_list = ["lg21222", "kgb2020", "silelis22"]
phone_list1 = ["stringas", "stringas", 1, 1, 2, 3, 4, 5, False, False]
number_list = [1, 2, 3, 4, 5, 6, 7]
no_duplicate_phone_list = set(phone_list1)

# can change created items
mutable = ["iphone12", "samsung 20"]
mutable[0] = "iphone13"

# can't change already created items
immutable = ("iphone12", "samsung 20")

# in other languages called hash map
dictionary = {"mobile_phones": phone_list, "tv": tv_list}

# -- Printing --
print(phone_list)
print(immutable)
print(dictionary.values())

# -- if logic gates --
if word == number:
    print("zodis lygus skaiciui")
else:
    print("padaryta kazka kito")

if len(phone_list) == len(immutable):
    print("Sitie listai yra lygus")
elif phone_list == immutable:
    print("lygus listai")
else:
    print("neivyko funcionalumas")

# bad logic statement example (most of the time is the wrong approach)
# if len(phone_list) == len(immutable):
#    print("Sitie listai yra lygus")
# elif phone_list == immutable:
#    print("lygus listai")
# else:
#    print("neivyko funcionalumas")

# -- loops --

for i in phone_list:
    print(i)

count = 0
while (flag == False):
    count += 1
    if count > 5:
        flag = True
        print("flag was changed")


# -- Functions/Methods --
def funcija(sarasas, sarasas1):
    print(phone_list)
    print(tv_list)


class User:
    def method(self, sarasas, sarasas1):
        print(sarasas)
        print(sarasas1)


# -- Function call/Method call --
# -- Function call --
funcija(phone_list, tv_list)

# -- Method call --
# Creates instance
user = User()
user.method(phone_list, tv_list)

# -- Access data structures --
# -- List index access --
pirmas_indeksas = phone_list[1]
print(pirmas_indeksas)

# -- Dictionary access --
print(dictionary["mobile_phones"])
print(dictionary.values())


# -- Bubble sort --
# [7,3,2,8,2,1,5,3,2,1,7,3,2] -> Bubble sort -> [1,1,2,2,2,2,3,3,3,5,7,7,8]
# 1: while loop
# 2: 7,3 -> is 7 higher number than 3 if yes switch places

def bubble_sort():
    bubble_sort_list = [1, 2, 3, 4, 5, 6, 7, 9, 8]
    is_sorting_finished = False
    iteration_counter = 0
    while is_sorting_finished == False:
        did_sort_happen = False
        for i in range(len(bubble_sort_list) - 1):
            if bubble_sort_list[i] > bubble_sort_list[i + 1]:
                temp = bubble_sort_list[i]
                bubble_sort_list[i] = bubble_sort_list[i + 1]
                bubble_sort_list[i + 1] = temp
                did_sort_happen = True
            iteration_counter += 1
        iteration_counter += 1

        if did_sort_happen == False:
            is_sorting_finished = True

    print(bubble_sort_list)
    print(iteration_counter)


# 9*9 = 81
bubble_sort()


# -- Fibonacci --
# def fibonacci(fibonacci_index):
#     n1 = 0
#     n2 = 1
#     fibonacci_sequence = [n1, n2]
#
#     for i in range(fibonacci_index - 2):
#         n1 = fibonacci_sequence[-2]
#         n2 = fibonacci_sequence[-1]
#         new_number = n1 + n2
#         fibonacci(fibonacci_index)
#         fibonacci_sequence.append(new_number)
#     print(fibonacci_sequence)

    # nterms = int(input("How many"))
    #
    # n1, n2 = 0, 1
    # count = 0
    # if nterms <= 0:
    #     print("invalid")
    # elif nterms == 1:
    #     print(n1)
    # else:
    #     while count < nterms:
    #         print(n1)
    #         nth = n1 + n2
    #
    #         n1 = n2
    #         n2 = nth
    #         count += 1


# fibonacci(100)


# -- Recursive fibonacci
# i = 8

# def fibonacci_recursive(a, b, index):
#     n1 = a
#     n2 = b
#     # calculations ty
#     i += 1
#     if index != i:
#     fibonacci_recursive(n1, n2, i, index)
#
# fibonacci_recursive(0,1, i, 500)

def user_login(user):
    if user.first_name == "asd":
        print("Acess granted")
    else:
        print("Access denied")
