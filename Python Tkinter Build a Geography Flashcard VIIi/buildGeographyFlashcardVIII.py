# Python Tkinter Build a Geography Flashcard VIII
# Python Tkinter Construye una tarjeta de geografía

from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random

root = Tk()
root.title('Python Tkinter Build a Geography Flashcard VIII')
root.iconbitmap('Python Tkinter Build a Geography Flashcard VIII/avatar.ico')
root.geometry("500x600")

# Create flashcard randomization
def math_random():

    # Generate a random number
    global num_1
    global num_2
    num_1 = randint(0, 9)
    num_2 = randint(0, 9)
    #math_sign = Label(pic_frame)

    global add_image1
    global add_image2

    card1 = "Python Tkinter Build a Geography Flashcard VIII/flashcards/" + str(num_1) + ".jpg"
    card2 = "Python Tkinter Build a Geography Flashcard VIII/flashcards/" + str(num_2) + ".jpg"

    add_image1 = ImageTk.PhotoImage(Image.open(card1))
    add_image2 = ImageTk.PhotoImage(Image.open(card2))

    # put flashcard images on the screen
    add_1.config(image=add_image1)
    add_2.config(image=add_image2)


# Create addition answer function
def answer_add():
    answer = num_1 + num_2
    if int(add_answer.get()) == answer:
        response = "Correct " + str(num_1) + " + " + str(num_2) + " = " + str(answer)
    else:
        response = "Wrong " + str(num_1) + " + " + str(num_2) + " = " + str(answer) + " Not " + add_answer.get()

    answer_message.config(text=response)
    add_answer.delete(0, "end")
    math_random() #funtion math_ramdom

# Create Addition math flashcards
def add():
    hide_all_frames()
    add_frame.pack(fill="both", expand=1)

    add_label = Label(add_frame, text="Addition Flashcards", font=("Helvetica", 18)).pack(pady=5)
    pic_frame = Frame(add_frame, width = 400, height=300)
    pic_frame.pack()

    # Generate a random number
    global num_1
    global num_2
    num_1 = randint(0, 9)
    num_2 = randint(0, 9)
    #math_sign = Label(pic_frame)

    # Create 3 labes inside our pic frame, frame
    global add_1
    global add_2
    add_1 = Label(pic_frame)
    add_2 = Label(pic_frame)
    math_sign = Label(pic_frame, text="+", font=("Helvetica", 28))
    
    # Grid our label
    add_1.grid(row=0, column=0)
    math_sign.grid(row=0, column=1)
    add_2.grid(row=0, column=2)

    global add_image1
    global add_image2

    card1 = "Python Tkinter Build a Geography Flashcard VIII/flashcards/" + str(num_1) + ".jpg"
    card2 = "Python Tkinter Build a Geography Flashcard VIII/flashcards/" + str(num_2) + ".jpg"

    add_image1 = ImageTk.PhotoImage(Image.open(card1))
    add_image2 = ImageTk.PhotoImage(Image.open(card2))

    # put flashcard images on the screen
    add_1.config(image=add_image1)
    add_2.config(image=add_image2)

    # Create anwer box and button
    global add_answer 
    add_answer = Entry (add_frame, font=("Helvetica", 18))
    add_answer.pack(pady=50)

    add_answer_button = Button(add_frame, text="Answer", command=answer_add)
    add_answer_button.pack()

    global answer_message
    answer_message = Label(add_frame, text="", font=("Helvetica", 18))
    answer_message.pack(pady=20)

# Create Radomizing state function
def random_state():

    # Create list of state names
    global our_states
    our_states = ['california', 'florida', 'illinois', 'kentucky','nebraska', 'nevada', 'newyork', 'oregon', 'texas']

    # Generate a random number
    global rando
    rando = randint(0, len(our_states)-1)
    state = "Python Tkinter Build a Geography Flashcard VIII/states/" + our_states[rando] + ".png"

    # Create our State Images
    global state_image
    state_image = ImageTk.PhotoImage(Image.open(state))
    show_state.config(image=state_image)
    
# create state capital answer
def state_capital_answer():
    if capital_radio.get() == our_state_capitals[answer]:
        response = "Correct " + our_state_capitals[answer] + "is the capital of " + answer.title()
    else:
        response = "Incorrect " + our_state_capitals[answer] + "is the capital of " + answer.title()

    answer_label_capitals.config(text= response)

# Create answer function
def state_answer():

    answer = answer_input.get()
    answer = answer.replace(" ", "") # Remplaza, quitando el espacio

    # Determine if our answer if right or wring!
    if answer.lower() == our_states[rando]:
        response = "Correct " + our_states[rando].title()
    else:
        response="Incorrect " + our_states[rando].title()

    answer_label.config(text=response)
    
    # clear the entrey box
    answer_input.delete(0, 'end')

    random_state()

# Create state flascard Function
def states():
    # Hide previous frames
    hide_all_frames() # borra el frame anterior
    state_frame.pack(fill="both", expand=1)
    #my_label = Label(state_frame, text="States").pack()

    '''
    # Create list of state names
    global our_states
    our_states = ['california', 'florida', 'illinois', 'kentucky','nebraska', 'newyork', 'oregon', 'texas']

    # Generate a random number
    global rando
    rando = randint(0, len(our_states)-1)
    state = "Python Tkinter Build a Geography Flashcard IV/states/" + our_states[rando] + ".png"

    # Create our State Images
    global state_image
    state_image = ImageTk.PhotoImage(Image.open(state))
    '''

    global show_state
    show_state = Label(state_frame)
    show_state.pack(pady=15)
    random_state()

    # Create a aswer input box
    global answer_input
    answer_input = Entry (state_frame, font=("Helvetica", 18), bg="white")
    answer_input.pack(pady=15)

    # Create Button randomize state Images
    randon_button = Button(state_frame, text="Pass", command=states)
    randon_button.pack(pady=10)

    # Create a Button to Answers the question
    answer_button = Button(state_frame, text="Answer", command=state_answer)
    answer_button.pack(pady=5)

    # Create a Label to tell us if we got the answer right or not
    global answer_label
    answer_label = Label(state_frame, text="",  font=("Helvetica", 18), bg="white")
    answer_label.pack(pady=15)

# Create State Capital Flashcard Function
def state_capitals():
    # Hide previous frames
    hide_all_frames() # borra el frame anterior
    state_capitals_frame.pack(fill="both", expand=1)
    #my_label = Label(state_capitals_frame, text="States Capitals").pack()

    global show_state
    show_state = Label(state_capitals_frame)
    show_state.pack(pady=15)

    global our_states
    our_states = ['california', 'florida', 'illinois', 'kentucky','nebraska', 'nevada', 'newyork', 'oregon', 'texas']

    global our_state_capitals
    our_state_capitals = {
    'california':"sacramento",
    'florida':"tallahasse", 
    'illinois':"sorinfield", 
    'kentucky':"frankfort",
    'nebraska': "lincoln", 
    'nevada':"carson city", 
    'newyork': "albany", 
    'oregon': "salem", 
    'texas':"austin"
    }

    # create empty answer list and counter
    answer_list =[]
    count = 1
    global answer
    
    # Generate our theree randon capitals
    while count < 4:
        # if first selection, make it our answer
        rando = randint(0, len(our_states)-1)
        if count == 1: 
            answer = our_states[rando]
            global state_image
            state = "Python Tkinter Build a Geography Flashcard VIII/states/" + our_states[rando] + ".png"
            state_image = ImageTk.PhotoImage(Image.open(state))
            show_state.config(image=state_image)

        # add our first selection to a new list
        answer_list.append(our_states[rando])

        # Remove from old list
        our_states.remove(our_states[rando])

        # Shuffle our original list
        random.shuffle(our_states)

        count += 1

    random.shuffle(answer_list)

    global capital_radio
    capital_radio = StringVar()
    capital_radio.set(our_state_capitals[answer_list[0]])
    
    capital_radio_butto1 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[0]].title(), variable=capital_radio, value=our_state_capitals[answer_list[0]]).pack()
    capital_radio_butto2 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[1]].title(), variable=capital_radio, value=our_state_capitals[answer_list[1]]).pack()
    capital_radio_butto3 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[2]].title(), variable=capital_radio, value=our_state_capitals[answer_list[2]]).pack()

    # Add a Pass Button
    pass_button = Button(state_capitals_frame, text="Pass", command=state_capitals)
    pass_button.pack(pady=15)

    # Create a button to answer
    capital_anwer_button = Button(state_capitals_frame, text="Answer", command=state_capital_answer)
    capital_anwer_button.pack(pady=15)

    # Create an answer label
    global answer_label_capitals
    answer_label_capitals = Label(state_capitals_frame, text="", font=("helvetica", 15))
    answer_label_capitals.pack(pady=15)



# Hide all previous frames
def hide_all_frames():
    # Loop thru and destroy all children in previous frames
    for Widget in state_frame.winfo_children():
        Widget.destroy()

    for Widget in state_capitals_frame.winfo_children():
        Widget.destroy()

    for Widget in add_frame.winfo_children():
        Widget.destroy()

    add_frame.pack_forget()
    state_frame.pack_forget()
    state_capitals_frame.pack_forget()

# Create our menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Geography Menu Items
states_menu = Menu(my_menu)
my_menu.add_cascade(label="Geography", menu=states_menu)
states_menu.add_command(label="States", command=states)
states_menu.add_command(label="State Capitals", command=state_capitals)
states_menu.add_separator()
states_menu.add_command(label="Exit", command=root.quit)


# Math Flashcard Menu
math_menu = Menu(my_menu)
my_menu.add_cascade(label="Math", menu=math_menu)
math_menu.add_command(label="Addition", command=add)

# Create our Frames
state_frame = Frame(root, width=500, height=50, bg="white")
state_capitals_frame = Frame(root, width=500, height=500)

# addition Frame
add_frame = Frame(root, width=500, height=500)

root.mainloop()