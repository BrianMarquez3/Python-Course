# Python Tkinter Word Jumble Game II, show hint on word jumble Game
# Pyhton Tkinter Obtener altura y ancho

from tkinter import *
from random import choice
from random import shuffle

root = Tk()
root.title('Python Tkinter Word Jumble Game')
root.iconbitmap('Python Tkinter Word Jumble Game/liam.ico')
root.geometry("600x400+-50+50") 

my_label = Label(root, text="", font=("Helvetica", 48))
my_label.pack(pady=20)

def shuffler():
    entry_anwer.delete(0, END)
    answer_Label.config(text='')


    # List os departamets words
    states = ['ancash', 'apurimac', 'arequipa', 'ayacucho', 'cajamarca', 'cerro de pasco', 'cuzco', 'huancavelica', 'huanuco', 'ica', 'junin', 'la libertad', 'lambayeque', 'lima', 'madre de dios', 'moquegua', 'piura', 'puno', 'san martin', 'tacna', 'tumbes', 'ucayali', 'amazonas', 'loreto']

    # Pick random state from list
    global word
    word = choice(states)
    #my_label.config(text=word)

    #Brack apart our chosen word
    break_apart_word = list(word)
    shuffle(break_apart_word)
    #print(break_apart_word)

    # Turn shiffeled List into a word
    global shuffle_word
    shuffle_word = ''
    for letter in break_apart_word:
        shuffle_word += letter
        
    # print shuflle word the screen
    my_label.config(text=shuffle_word)


# Create anwer Funtion
def answer():
    if word == entry_anwer.get():
        answer_Label.config(text="Correct")
    else:
        answer_Label.config(text="Incorrect")

entry_anwer = Entry(root, font=("Helvetica", 24))
entry_anwer.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

my_button = Button(button_frame, text="Pick Another word", command=shuffler)
my_button.grid(row=0, column=0, padx=10)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=1, padx=10)

answer_Label = Label(root, text="", font=("Helvetica", 18))
answer_Label.pack(pady=20)

root.mainloop()