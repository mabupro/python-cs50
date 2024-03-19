# with open("students.csv") as file:
#     for line in file:
#         # row = line.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]}")
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
        # students.append(f"{name} is in {house}")

        # student = {}
        # student["name"] = name
        # student["house"] = house

        # student = {"name":name, "house":house}
        # students.append(student)

# for student in sorted(students):
#     print(student)
        
# for student in students:
#     print(f"{student['name']} is in {student['house']}")
        
# def get_name(student):
#     return student["name"]

# def get_house(student):
#     return student["house"]

# for student in sorted(students, key=get_house, reverse=True):
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")

# import csv

# students = []

# with open("students2.csv") as file:
#     # reader = csv.reader(file)
#     reader = csv.DictReader(file)
#     # for name, home in reader:
#     for row in reader:
#         # students.append({"name": name, "home": home})
#         students.append({"name": row["name"], "home": row["home"]})
    

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")

# import csv

# students = []

# with open("students2.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         name = row.get("name", "").strip()
#         home = row.get("home", "").strip()
#         students.append({"name": name, "home": home})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students3.csv", "a") as file:
        # writer = csv.writer(file)
        writer = csv.DictWriter(file, fieldnames=["name","home"])
        # writer.writerow([name,home])
        writer.writerow({"name": name, "home": home})



