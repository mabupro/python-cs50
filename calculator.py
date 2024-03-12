# x = 1
# x = int(input("What's x? "))
x = float(input("What's x? "))

# y = 2
# y = int(input("What's y? "))
y = float(input("What's y? "))

# z = x + y
# z = int(x) + int(y)
# z = round(x + y)

z = round(x / y, 2)

# print(z)
# print(x + y)
# print(z)
# print(f"{z:,}")
print(f"{z:.2f}")

