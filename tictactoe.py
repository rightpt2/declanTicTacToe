##this is gonna be rad
from importlib.machinery import WindowsRegistryFinder
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic-Tac-Toe')
#root.geometry("1200x710")

# We need a way to move between X and O, X starts
clicked = True # True = X, False = O
count = 0

# reset the game function
def reset():    
    global clicked, count
    # reset the buttons
    for bt in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
        bt.configure(text=" ", bg='grey', highlightbackground='light grey')
        bt.configure(state=NORMAL)
    
    # reset the game parameters
    clicked = True
    count = 0
    

# disable all of the buttons
def desableAllButtons():
    for bt in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
        bt.configure(state=DISABLED)

# check to see if someone won the game
def checkifwon():
    global winnter 
    winner = False

    ## line 1
    if b1['text'] in ['X', 'O'] and b1['text'] == b2['text'] == b3['text']:
        b1.config(bg='green', highlightbackground='light green')
        b2.config(bg='green', highlightbackground='light green')
        b3.config(bg='green', highlightbackground='light green')
        winner = True
        messagebox.showinfo('Tic Tac Toe', '{0} you won!'.format(b1['text']))
        desableAllButtons()

    ## line 2
    elif b4['text'] in ['X', 'O'] and b4['text'] == b5['text'] == b6['text']:
        b4.config(bg='green', highlightbackground='light green')
        b5.config(bg='green', highlightbackground='light green')
        b6.config(bg='green', highlightbackground='light green')
        winner = True
        messagebox.showinfo('Tic Tac Toe', '{0} you won!'.format(b4['text']))
        desableAllButtons()


    ## line 3
    elif b7['text'] in ['X', 'O'] and b7['text'] == b8['text'] == b9['text']:
        b7.config(bg='green', highlightbackground='light green')
        b8.config(bg='green', highlightbackground='light green')
        b9.config(bg='green', highlightbackground='light green')
        winner = True
        messagebox.showinfo('Tic Tac Toe', '{0} you won!'.format(b7['text']))
        desableAllButtons()

    ## col 1
    elif b1['text'] in ['X', 'O'] and b1['text'] == b4['text'] == b7['text']:
        b1.config(bg='green', highlightbackground='light green')
        b4.config(bg='green', highlightbackground='light green')
        b7.config(bg='green', highlightbackground='light green')
        winner = True
        messagebox.showinfo('Tic Tac Toe', '{0} you won!'.format(b1['text']))
        desableAllButtons()

    ## col 2
    elif b2['text'] in ['X', 'O'] and b2['text'] == b5['text'] == b8['text']:
        b2.config(bg='green', highlightbackground='light green')
        b5.config(bg='green', highlightbackground='light green')
        b8.config(bg='green', highlightbackground='light green')
        winner = True
        messagebox.showinfo('Tic Tac Toe', '{0} you won!'.format(b2['text']))
        desableAllButtons()

    ## col 3
    elif b3['text'] in ['X', 'O'] and b3['text'] == b6['text'] == b9['text']:
        b3.config(bg='green', highlightbackground='light green')
        b6.config(bg='green', highlightbackground='light green')
        b9.config(bg='green', highlightbackground='light green')
        winner = True
        messagebox.showinfo('Tic Tac Toe', '{0} you won!'.format(b3['text']))
        desableAllButtons()

    #diag 1
    elif b1['text'] in ['X', 'O'] and b1['text'] == b5['text'] == b9['text']:
        b1.config(bg='green', highlightbackground='light green')
        b5.config(bg='green', highlightbackground='light green')
        b9.config(bg='green', highlightbackground='light green')
        winner = True
        messagebox.showinfo('Tic Tac Toe', '{0} you won!'.format(b1['text']))
        desableAllButtons()

    #diag 2
    elif b3['text'] in ['X', 'O'] and b3['text'] == b5['text'] == b7['text']:
        b3.config(bg='green', highlightbackground='light green')
        b5.config(bg='green', highlightbackground='light green')
        b7.config(bg='green', highlightbackground='light green')
        winner = True
        messagebox.showinfo('Tic Tac Toe', '{0} you won!'.format(b3['text']))
        desableAllButtons()
    
    

    #check if tie
    elif count == 9 and winner == False:
            messagebox.showinfo('Tic Tac Toe', 'Looks like a Tie!\nNo One Wins'.format(b3['text']))
            desableAllButtons()

    else:
        pass

# button clicked function
def b_click(b):
    global clicked, count

    #X plays
    if b['text'] == ' ' and clicked == True:
        b['text'] = 'X'
        clicked = False
        count += 1
        checkifwon()

    #Y Plays
    elif b['text'] == ' ' and clicked == False:
        b['text'] = 'O'
        clicked = True
        count +=1
        checkifwon()

    # what if somebody clicks where there already is a play?
    else:
        messagebox.showerror('Tic Tac Toe', 'Somebody already played there.\nTry again!')

## build our 9 buttons
b1 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg='grey', highlightbackground='light grey', command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg='grey', highlightbackground='light grey', command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg='grey', highlightbackground='light grey', command=lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg='grey', highlightbackground='light grey', command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg='grey', highlightbackground='light grey', command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg='grey', highlightbackground='light grey', command=lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg='grey', highlightbackground='light grey', command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg='grey', highlightbackground='light grey', command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica",20), height=3, width=6, bg='grey', highlightbackground='light grey', command=lambda: b_click(b9))

# make the buttons a grid in the screen
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)


# create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# create an options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Options', menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)


root.mainloop()