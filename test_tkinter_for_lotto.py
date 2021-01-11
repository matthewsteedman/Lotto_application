from tkinter import *
from tkinter import messagebox


my_frame = Tk()
my_frame.geometry('700x500')
my_frame.title("Ithuba National Lottery of South Africa")

lbl_title = Label(my_frame, text="Welcome")
lbl_title.place(x=300, y=25)
lbl_user_input = Label(my_frame, text="Enter a number ranging from 0 - 49")
lbl_user_input.place(x=200, y=100)

lbl_lotto_numbers = Label(my_frame, text="Lotto Draw is:")
lbl_lotto_numbers.place(x=50, y=270)

lbl_match_numbers = Label(my_frame, text="Your Matching Numbers:")
lbl_match_numbers.place(x=50, y=300)

new_list = []
lotto_draw = random.sample(range(1, 50), 6)
print(lotto_draw)

ent_user_input_1 = Entry(my_frame, width=5)
ent_user_input_2 = Entry(my_frame, width=5)
ent_user_input_3 = Entry(my_frame, width=5)
ent_user_input_4 = Entry(my_frame, width=5)
ent_user_input_5 = Entry(my_frame, width=5)
ent_user_input_6 = Entry(my_frame, width=5)


def lotto_funct():

    user_list = [int(ent_user_input_1.get()), int(ent_user_input_2.get()), int(ent_user_input_3.get()),
                 int(ent_user_input_4.get()),
                 int(ent_user_input_5.get()), int(ent_user_input_6.get())]

    for i in range(6):
        if 0 <= int(user_list[i]) <= 49:
            new_list.append(user_list[i])

        elif 49 < int(user_list[i]):
            messagebox.showerror("INVALID", "Enter a number ranging from 0 - 49")
        lbl_draw = Label(my_frame, text=lotto_draw)
        lbl_draw.place(x=170, y=270)

    matching_numbers = set(new_list) & set(lotto_draw)

    if new_list == new_list:
        lbl_matched = Label(my_frame, text=matching_numbers)
        lbl_matched.place(x=260, y=300)
        print(sorted(matching_numbers))
    else:
        if new_list == 0:
            messagebox.showerror("Sorry!", "no matching numbers :( ")

    if len(matching_numbers) == 0:
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
        messagebox.showinfo("Congratulations!", "All numbers Are Correct!" + str(matching_numbers)
                            + "\n" "You won R10000000.00 :)")


btn = Button(my_frame, command=lotto_funct)
btn.grid()


ent_user_input_1.place(x=60, y=170)
ent_user_input_2.place(x=170, y=170)
ent_user_input_3.place(x=280, y=170)
ent_user_input_4.place(x=390, y=170)
ent_user_input_5.place(x=500, y=170)
ent_user_input_6.place(x=600, y=170)

my_frame.mainloop()
