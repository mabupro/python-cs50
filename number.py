# x = int(input("What's x? "))
# print(f"x is {x}")

# What's x? cat
# ValueError: invalid literal for int() with base 10: 'cat'


# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")

# What's x? cat
# x is not an integer


# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")

# print(f"x is {x}")

# What's x? cat
# x is not an integer
# NameError: name 'x' is not defined


# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

# What's x? cat
# x is not an integer


# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break

# print(f"x is {x}")

# What's x? cat
# x is not an integer
# What's x? 2
# x is 2


def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            # x = int(input("What's x? "))
            return int(input(prompt))
        except ValueError:
            # print("x is not an integer")
            pass
        # else:
        #     break
    # return x

main()