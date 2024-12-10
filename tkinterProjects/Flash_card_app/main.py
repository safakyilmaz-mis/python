import random
import tkinter as tk
from tkinter import *
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"

root = Tk()
root.title("Flash card app")
root.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

try:
    words = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words = pd.read_csv("data/spanish_words.csv")
    toLearn = words.to_dict(orient="records")
else:
    toLearn = words.to_dict(orient="records")

card_word = {}
timer = None


def saveToCsv():
    global timer
    # savedWords = pd.DataFrame.from_records(toLearn)
    savedWords = pd.DataFrame(toLearn)
    savedWords.to_csv("data/words_to_learn.csv", index=False)


def flipEnglishWord():
    global card_word, timer
    if timer:
        root.after_cancel(timer)
    canvas.itemconfig(wordCard, image=myimage2)
    translatedWord = card_word["English"]
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=translatedWord, fill="white")
    timer = None


def nextCard():
    global card_word, timer
    if timer:
        root.after_cancel(timer)
    try:
        card_word = random.choice(toLearn)
    except IndexError:
        canvas.itemconfig(word, text="¡Felicidades! ¡Conoces todas las palabras!", font=("Arial", 15, "bold"))
    else:
        canvas.itemconfig(wordCard, image=myimage)
        Word = card_word["Spanish"]
        canvas.itemconfig(language, text="Spanish", fill="black")
        canvas.itemconfig(word, text=Word, fill="black")
        timer = root.after(3000, flipEnglishWord)


def deleteWord():  # user know this word already
    global card_word, timer
    if timer:
        root.after_cancel(timer)
    try:
        card_word = random.choice(toLearn)
    except IndexError:
        canvas.itemconfig(word, text="¡Felicidades! ¡Conoces todas las palabras!", font=("Arial", 15, "bold"))
    else:
        toLearn.remove(card_word)
        canvas.itemconfig(wordCard, image=myimage)
        Word = card_word["Spanish"]
        canvas.itemconfig(language, text="Spanish", fill="black")
        canvas.itemconfig(word, text=Word, fill="black")
        saveToCsv()
        timer = root.after(3000, flipEnglishWord)


myimage = PhotoImage(file="images/card_front.png")
myimage2 = PhotoImage(file="images/card_back.png")
true = PhotoImage(file="images/right.png")
false = PhotoImage(file="images/wrong.png")

canvas = Canvas(root, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=1, columnspan=2, padx=50, pady=50)

wordCard = canvas.create_image(400, 263, image=myimage)

language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

button_t = Button(image=true, highlightthickness=0, command=deleteWord)
button_t.grid(row=2, column=2)

button_f = Button(image=false, highlightthickness=0, command=nextCard)
button_f.grid(row=2, column=1)

nextCard()

tk.mainloop()
