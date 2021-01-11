import random

print("---Welcome to South African Lotto!!---")
print()
new_list = []
lotto_draw = random.sample(range(1, 50), 6)


for i in range(6):
    user_list = int(input("Enter a number from 0 to 49: "))
    if 0 <= user_list <= 49:
        new_list.append(user_list)
        print("appended")
    elif 49 < user_list:
        print("out of range")

print("Your lotto Guesses:", (sorted(new_list), "Lotto Draw:", sorted(lotto_draw)))

matching_numbers = set(new_list) & set(lotto_draw)

if new_list == new_list:
    print("Your matching Numbers are:", sorted(matching_numbers))
else:
    if new_list == 0:
        print("No matching numbers")

if len(matching_numbers) == 0:
    print("Try again")
if len(matching_numbers) == 1:
    print("Try again")
if len(matching_numbers) == 2:
    print("You won R20")
if len(matching_numbers) == 3:
    print("You won R100.50")
if len(matching_numbers) == 4:
    print("You won R2384.00")
if len(matching_numbers) == 5:
    print("You won R8584.00")
if len(matching_numbers) == 6:
    print("You won R10000000.00")
