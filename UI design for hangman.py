from tkinter import *
from tkinter import ttk
import random
from words import words
import string
from PIL import ImageTk, Image
from tkinter import messagebox


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


# root creation
root = Tk()
root.title("hangman game")
root.geometry('500x400')


# entry
e1 = Entry(root, width=35, borderwidth=5)
e1.grid(column=2, row=0, columnspan=20, padx=10, pady=10)


var = IntVar()
var.set(0)

strvar = StringVar()
strvar.set("LETPLAY")

letter_guessed = StringVar()
letter_guessed.set(" ")

label_1 = Label(root, text="Type the letter you guess ").grid(
    column=1, row=0, sticky="w")
label_2 = Label(root, text="Lives you still have left").grid(
    column=1, row=1, sticky="w")
label_3 = Label(root, textvariable=var).grid(column=2, row=1, sticky="e")

label_4 = Label(root, width=24, textvariable=strvar, font=35, borderwidth=5,
                background="#FFFFFF")

label_4.grid(column=2, row=3, columnspan=18, padx=10, pady=10, sticky="W")

label_5 = Label(root, text="The word you need to guess ").grid(
    column=1, row=3, sticky="w")

label_7 = Label(root, text="The letter you guessed ")
label_7.grid(column=1, row=4, sticky="w")
label_8 = Label(root, width=24, textvariable=letter_guessed, font=35, borderwidth=5,
                background="#FFFFFF")
label_8.grid(column=2, row=3, columnspan=18, padx=10, pady=10, sticky="W")


# images
my_image0 = ImageTk.PhotoImage(Image.open(
    "C:/Users/nguyetr/Desktop/Personal stuff/Python/hangman/images/0.png"))
my_image1 = ImageTk.PhotoImage(Image.open(
    "C:/Users/nguyetr/Desktop/Personal stuff/Python/hangman/images/1.png"))
my_image2 = ImageTk.PhotoImage(Image.open(
    "C:/Users/nguyetr/Desktop/Personal stuff/Python/hangman/images/2.png"))
my_image3 = ImageTk.PhotoImage(Image.open(
    "C:/Users/nguyetr/Desktop/Personal stuff/Python/hangman/images/3.png"))
my_image4 = ImageTk.PhotoImage(Image.open(
    "C:/Users/nguyetr/Desktop/Personal stuff/Python/hangman/images/4.png"))
my_image5 = ImageTk.PhotoImage(Image.open(
    "C:/Users/nguyetr/Desktop/Personal stuff/Python/hangman/images/5.png"))
my_image6 = ImageTk.PhotoImage(Image.open(
    "C:/Users/nguyetr/Desktop/Personal stuff/Python/hangman/images/6.png"))

image_list = [my_image0, my_image1, my_image2,
              my_image3, my_image4, my_image5, my_image6]


label_6 = Label(root, image=my_image0)
label_6.grid(row=6, column=6, columnspan=10)


def button_click():
    global submit_button
    list_of_word_letter = []
    word = get_valid_word(words)
    word_letters = set(word)  # get the unique value of letter in that word
    # get the unique value of alphabet letter
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # to keep track of what user has guessed
    correct_guess_letters = set()  # to keep track of what users guess correctly
    global number_of_guesses
    number_of_guesses = 0
    var.set(number_of_guesses)
    global label_6, label_1, label_2, label_3, label_4, label_5
    label_6.grid_forget()

    while len(word_letters) > 0:
        # break the loop if the number of guess go over 7
        if number_of_guesses == 7:
            label_6 = Label(root, Image=my_image6)
            label_6.grid(row=6, column=6, columnspan=10)
            break

        # what the current word is
        for i in range(len(word)):
            if word[i] in correct_guess_letters:
                list_of_word_letter.append(word[i])
            else:
                list_of_word_letter.append("-")

        word_to_get = " ".join([str(item) for item in list_of_word_letter])
        global strvar
        strvar.set(word_to_get)

        user_input = str(e1.get().upper)
        e1.delete(0, END)
        if user_input in alphabet and user_input not in used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
                correct_guess_letters.add(user_input)
            else:
                number_of_guesses += 1
                if number_of_guesses == 0:
                    label_6 = Label(root, Image=my_image0)
                    label_6.grid(row=6, column=6, columnspan=10)
                elif number_of_guesses == 1:
                    label_6 = Label(root, Image=my_image1)
                    label_6.grid(row=6, column=6, columnspan=10)
                elif number_of_guesses == 2:
                    label_6 = Label(root, Image=my_image2)
                    label_6.grid(row=6, column=6, columnspan=10)
                elif number_of_guesses == 3:
                    label_6 = Label(root, Image=my_image3)
                    label_6.grid(row=6, column=6, columnspan=10)
                elif number_of_guesses == 4:
                    label_6 = Label(root, Image=my_image4)
                    label_6.grid(row=6, column=6, columnspan=10)
                elif number_of_guesses == 5:
                    label_6 = Label(root, Image=my_image5)
                    label_6.grid(row=6, column=6, columnspan=10)
                else:
                    label_6 = Label(root, Image=my_image6)
                    label_6.grid(row=6, column=6, columnspan=10)

        elif user_input in used_letters:
            messagebox.showwarning(
                "Error", "You already guessed this letter. Please guess other letter")
            root.update()
        else:
            messagebox.showwarning(
                "Error", "wrong character. Please try again")
            root.update()

        you_guessed = " ".join(used_letters)
        global letter_guessed
        letter_guessed.set(you_guessed)


# Button
# submit button
submit_button = Button(root, text="SUBMIT", padx=40, command=button_click)
submit_button.grid(column=8, row=12, columnspan=4)


root.mainloop()
