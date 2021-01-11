#Lotto test
import random

#Empty list
LottoNumbers = []

for i in range(6):
    number = random.randint(1, 49)
#Checking if the number has already been picked
    while number in LottoNumbers:
        number = random.randint(1, 49)

#append lotto numbers
    LottoNumbers.append(number)

#sort in ascending order


#getting user input
#creating empty list
userNUmbers = []
for i in range(6):
    number = int(input("Please enter number between 1 and 49:"))
    while (number in userNUmbers or number<1 or number>49) :
        print("invalid number, please try again. ")

    userNUmbers.append(number)


#creating a count
count = 0
for number in userNUmbers:
    if number in LottoNumbers:
        count += 1

    def total_winnings():
        if count == 0:
            message = "Win R0"
            return message
        elif count == 1:
            message = "Win R0"
            return message
        elif count == 2:
            message = "Win R20"
            return message
        elif count == 3:
            message = "Win R100.50"
            return message
        elif count == 4:
            message = "Win 2,384.00"
            return message
        elif count == 5:
            message = "Win R8,584.00"
            return message
        elif count == 6:
            message = "Win R10, 000 000.00"
            return message


print("you guessed " + str(count) + " " + "number(s) correctly")
print("Lotto numbers are: ")
print(userNUmbers)
print(LottoNumbers)
print(total_winnings())
