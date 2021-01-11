# import json

name = input("Enter Name: ")

surname = input("Enter Surname: ")

age = int(input("Enter age:"))

string = str(age)

restrict = int('18')

name_surname = name + surname + string

if age < restrict:
    print("You Are Too Young!")
elif age >= restrict:
    print("You may enter", name, surname)
