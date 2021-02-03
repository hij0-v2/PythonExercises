from functionality.main import user_login


class User:
    def __init__(self, username, password, first_name, last_name):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name


user1 = User("asd", "asd", "asd", "asd")
user2 = User("das", "das", "das", "das")

print(user1.first_name)
print(user2.first_name)


# Carry
# 010901060 + 090909050
# 4
# Write an algorithm that solves carry counting

def carry_solver(n1, n2):
    counter = 0
    n3 = 0

    longer_number = max(len(str(n1)), len(str(n2)))

    for i in reversed(range(longer_number)):
        n3 = n1 % 10 + n2 % 10 + n3
        if n3 > 9:
            n3 = 1
        else:
            n3 = 0
        counter += n3
        n1 //= 10
        n2 //= 10
    if counter == 0:
        print("No carry")
    else:
        print("Carry counter: " + str(counter))



carry_solver(78896, 10012)
