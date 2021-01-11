from tkinter import *
from tkinter import messagebox
import random
import datetime

# login window

window = Tk()
window.geometry('500x500')
window.title("Login")

x = datetime.datetime.now()

# stored date and time in a Lable

lbl_dt = Label(window, text=x)
lbl_dt.place(x=20, y=450)

# labels for login user interface

lbl_title = Label(window, text="Welcome", font=("Arial Bold", 20))
lbl_slogan = Label(window, text="Ithuba National Lottery of South Africa", font=("Arial Bold", 15))

lbl_first_name = Label(window, text="First Name:")
lbl_last_name = Label(window, text="Last Name:")
lbl_age = Label(window, text="Age:")

# entries for login

ent_first_name = Entry(window)
ent_last_name = Entry(window)
ent_age = Entry(window)

# a function that closes the program


def ext():
    window.destroy()

# A function that clears text boxes print(x)


def clear():

    ent_first_name.delete("0", END)
    ent_last_name.delete("0", END)
    ent_age.delete("0", END)

# The login function
# if the users age is less than 18 a message displays that the user is too young to enter
# if the users age is greater than 18 the user is allowed to enter into the lottery application


def login():
    try:
        if int(ent_age.get()) >= 18:
            messagebox.showinfo("WElCOME", "You may Enter" "\n" + ent_first_name.get() + "\n" + ent_last_name.get())

            window.withdraw()
            logged_in()

        elif int(ent_age.get()) < 18:
            messagebox.showerror("invalid", "You are too young" "\n" + ent_first_name.get() + "\n" + ent_last_name.get()
                                 )
    except ValueError:
        messagebox.showerror("Invalid", "Please your AGE")

# bring up the 2nd gui which allows the user to play


def logged_in():
    my_frame = Tk()
    my_frame.geometry('700x500')
    my_frame.title("Ithuba National Lottery of South Africa")

# lables for the 2nd Gui

    lbl_title_1 = Label(my_frame, text="WELCOME")
    lbl_title_1.place(x=330, y=25)
    lbl_user_name = Label(my_frame, text=ent_first_name.get() + " " + ent_last_name.get())
    lbl_user_name.place(x=280, y=60)
    lbl_user_input = Label(my_frame, text="Enter a number ranging from 0 - 49")
    lbl_user_input.place(x=220, y=100)

    lbl_lotto_numbers = Label(my_frame, text="Lotto Draw is:")
    lbl_lotto_numbers.place(x=50, y=300)

    lbl_match_numbers = Label(my_frame, text="Your Matching Numbers:")
    lbl_match_numbers.place(x=50, y=400)

# new_list is a list that contains the users numbers
# lotto_draw is a list with the random lotto draw

    new_list = []
    lotto_draw = random.sample(range(1, 50), 6)

    print(lotto_draw)

# entries where the user would input numbers

    ent_user_input_1 = Entry(my_frame, width=5)
    ent_user_input_2 = Entry(my_frame, width=5)
    ent_user_input_3 = Entry(my_frame, width=5)
    ent_user_input_4 = Entry(my_frame, width=5)
    ent_user_input_5 = Entry(my_frame, width=5)
    ent_user_input_6 = Entry(my_frame, width=5)

# function for lotto random generator and comparing the users input to the random list
# using the try and exception , if the user enters no number it kicks out an error

    def lotto_funct():

        try:
            user_list = [int(ent_user_input_1.get()), int(ent_user_input_2.get()), int(ent_user_input_3.get()),
                         int(ent_user_input_4.get()),
                         int(ent_user_input_5.get()), int(ent_user_input_6.get())]

            # takes the users input and runs it through the for loop below by indexes
            # if the number is between 0 or = to 49 it should append to a new list
            # if the number is greater than 49 it should show an error message

            for i in range(6):
                if 0 <= int(user_list[i]) <= 49:
                    new_list.append(user_list[i])

                elif 49 < int(user_list[i]):
                    messagebox.showerror("INVALID", "Enter a number ranging from 0 - 49")
                lbl_draw = Label(my_frame, text=lotto_draw)
                lbl_draw.place(x=170, y=300)

            # stored the two lists in a variable using set to determine the matching numbers
            # takes the user input and compares it to the lotto draw

            matching_numbers = set(new_list) & set(lotto_draw)

            # a simple if statement that shows if the numbers are match it should display the matching numbers
            # in a lable sorted.
            # if there are no matching numbers a error box should display
            # if the are matching numbers a message box will display with the matching numbers

            if new_list == new_list:
                lbl_matched = Label(my_frame, text=matching_numbers)
                lbl_matched.place(x=260, y=400)
                print(sorted(matching_numbers))
            else:
                if new_list == 0:
                    messagebox.showerror("Sorry!", "no matching numbers :( ")

            if len(matching_numbers) == 0:
                lbl_matched = Label(my_frame, text="0", bg='white', width='10'
                                                                          '')
                lbl_matched.place(x=260, y=400)
                messagebox.showerror("Sorry!", "Please Try Again :( ")

            elif len(matching_numbers) == 1:
                messagebox.showinfo("Sorry", "Please Try Again :( only one number matched: " "\n" +
                                    str(matching_numbers))

            elif len(matching_numbers) == 2:
                messagebox.showinfo("Congratulations!", "Two Numbers Matched:" + str(matching_numbers) +
                                    "\n" "You won R20 :)")

            elif len(matching_numbers) == 3:
                messagebox.showinfo("Congratulations!", "Three Numbers matched:" + str(matching_numbers) +
                                    "\n" "You won R100.50 :)")

            elif len(matching_numbers) == 4:
                messagebox.showinfo("Congratulations!", "Four Numbers Matched:" + str(matching_numbers) +
                                    "\n" "You won R2384.00 :)")

            elif len(matching_numbers) == 5:
                messagebox.showinfo("Congratulations!", "Five Numbers Matched:" + str(matching_numbers) +
                                    "\n" "You won R8584.00 :)")

            elif len(matching_numbers) == 6:
                messagebox.showinfo("Congratulations!\n", "All numbers Are Correct!" + str(matching_numbers)
                                    + "\n" "You won R10000000.00 :)")

    # writes the users name, surname, age, the inputs , winning numbers, the total amount of matching numbers
    # if theres any , the date and time to a text file

            file_object = open('login_details+scores.txt', 'a+')
            file_object.write("First name: " + ent_first_name.get() + "\n")
            file_object.write("Last name: " + ent_last_name.get() + "\n")
            file_object.write("Age: " + ent_age.get() + "\n")
            file_object.write("Guesses: " + str(user_list) + "\n")
            file_object.write("Lotto Draw: " + str(lotto_draw) + "\n")
            file_object.write("Numbers That Matched: " + str(matching_numbers) + "\n")
            file_object.write("Date and time: " + str(x) + "\n" + "\n")
            file_object.close()
            my_frame.destroy()

        except ValueError:
            messagebox.showerror("Error", "NO numbers in entry box")
# a button that when clicked runs the function above

    btn = Button(my_frame,  text="Enter", command=lotto_funct)
    btn.place(x=335, y=220)

# using place i aligned the entry boxes

    ent_user_input_1.place(x=60, y=170)
    ent_user_input_2.place(x=170, y=170)
    ent_user_input_3.place(x=280, y=170)
    ent_user_input_4.place(x=390, y=170)
    ent_user_input_5.place(x=500, y=170)
    ent_user_input_6.place(x=600, y=170)

    my_frame.mainloop()

# a simple button which when clicked should run the login function


btn_login = Button(window, text="Login", command=login)

# a simple button which when clicked should run the clear function and should delete everything in the textbox's

btn_clear = Button(window, text="Clear", command=clear)

# a simple button when clicked will run the ext function which will destroy the program

btn_exit = Button(window, text="Exit", command=ext)

btn_login.place(x=150, y=270)
btn_clear.place(x=230, y=270)
btn_exit.place(x=308, y=270)

ent_first_name.place(x=150, y=125)
ent_last_name.place(x=150, y=170)
ent_age.place(x=150, y=220)

lbl_first_name.place(x=25, y=125)
lbl_last_name.place(x=25, y=170)
lbl_age.place(x=25, y=220)
lbl_title.place(x=170, y=5)
lbl_slogan.place(x=10, y=50)

window.mainloop()
