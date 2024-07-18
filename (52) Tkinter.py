from tkinter import * # importing everything from tkinter library (GUI)

# WINDOW
window = Tk() # creating a window

window.geometry("500x800") # giving the window a size
window.title("Samson Rizz Code") # giving it a title
icon = PhotoImage(file='sppaark logo.png') # converting our image to a format that tkinter can understand
window.iconphoto(True, icon) # adding an icon to the window
window.config(background='white') # adding bg color

# -----------------------------------------------------------------------

# LABELS
# an area displaying text and images
icon_img = PhotoImage(file='logo.png')
label = Label(window,
              text='Samson Codes',
              font=('Arial', 30, 'italic'),
              bg='black', # bg color
              fg='white', # fg/font color
              relief=RAISED, # a 3d kinda border
              bd=10, # thickness of border
              padx=20, pady=20,
              # image=icon_img,
              compound='top') # placement of image
label.pack()

# -----------------------------------------------------------------------

# BUTTONS
count = 0
def click():
    global count
    count +=1
    print(f"You clicked me {count} times")

button = Button(window,
                text="Click",
                font=("Comic Sans", 20),
                command=click,
                bg='black',
                fg='white',
                # image=icon_img,
                compound='right',
                activeforeground='white', # button won't flash if active fg color is same
                activebackground='black') # button won't flash if active bg color is same
button.pack(padx=10, pady=10)

# -----------------------------------------------------------------------

# ENTRY BOX
def submit():
    name = entry.get()
    print(f'Hey {name}')

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

entry = Entry(window, bg='white', fg='black', font=('Arial', 20, 'italic'))
entry.pack(side=TOP,padx=2, pady=0)

submit = Button(window, text="Submit", command=submit)
submit.pack(padx=10, pady=10)

delete = Button(window, text="Delete", command=delete)
delete.pack(padx=5, pady=5)

backspace = Button(window, text="Backspace", command=backspace)
backspace.pack(padx=5, pady=5)

# -------------------------------------------------------------------------

# CHECKBOX
def display():
    if x.get()==1:
        print("Thanks")
    else:
        print("No thanks!")

x = IntVar()

checkbutton = Checkbutton(window, text="Okay", variable=x, onvalue=1, offvalue=0, command=display)
checkbutton.pack(padx=10, pady=10)

# ---------------------------------------------------------------------------

# RADIOBUTTONS



foods = ['Pizza', 'Hamburger', 'Fries']

x = IntVar()
def order():
    for food in foods:
        if x.get() == foods.index(food):
            print(f"I love {food}")

for i in range(len(foods)):
    radiobutton = Radiobutton(window,
                              text=foods[i],
                              font=('Impact', 20),
                              variable=x,
                              value=i,
                              command=order,
                              padx=20)
    radiobutton.pack(anchor=W)

window.mainloop() # displaying the window
