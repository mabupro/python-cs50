name = input("What's your name? ")

# if name == "Harry":
# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Hermione":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Gryffindor")
# elif name == "Doraco":
#     print("Slyrherin")
# else:
#     print("Who?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    # case "Hermione":
    #     print("Gryffindor")
    # case "Ron":
    #     print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")