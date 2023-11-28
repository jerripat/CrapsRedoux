import tkinter as tk
from tkinter import messagebox, CENTER
from typing import List

root = tk.Tk()

tableColor = '#0c6122'
placeColor = '#070c52'
root.title("Welcome to True Odds Craps")
root.geometry("500x500")
root.configure(background=tableColor)

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

onFour = tk.IntVar()
onFive = tk.IntVar()
onSix = tk.IntVar()
onEight = tk.IntVar()
onNine = tk.IntVar()
onTen = tk.IntVar()


def new_game():
    # Add your code for starting a new game here
    messagebox.showinfo("New Game", "Starting a new game!")


def quit_game():
    # Add your code for quitting the game here
    messagebox.showinfo("Quit Game", "Quitting the game!")


def exit_program():
    # Add your code for exiting the program here
    root.destroy()


def getPlace() -> list:
    place_values: list[int] = [onFour.get(), onFive.get()]
    for i in place_values:
        print(i)
    return place_values


def rollDice():
    pass


# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add items to the "File" menu
file_menu.add_command(label="New Game", command=new_game)
file_menu.add_command(label="Quit Game", command=quit_game)
file_menu.add_command(label="Exit", command=exit_program)

# Load and display an image
image_path = "Images/Dice-icon.png"
try:
    # Open and read the image file
    image = tk.PhotoImage(file=image_path)

    # Create a label and set the image
    image_label = tk.Label(root, image=image, borderwidth=4, relief="raised")
    image_label.place(relx=0.2, rely=0.2, anchor=CENTER)  # Adjust padding as needed

except tk.TclError:
    # Handle if the image file is not found or not supported
    messagebox.showerror("Error", f"Unable to load image: {image_path}")

lblOne = tk.Label(root, text="4      5      6      8      9      10", font=("Arial", 20, "bold"), bg=tableColor,
                  fg="white", )
lblOne.place(relx=0.45, rely=0.4, anchor=CENTER)

lblBet = tk.Label(root, text="Bet", font=("Arial", 12, "bold"), bg="yellow", fg="red", relief="raised")
lblBet.place(relx=0.2, rely=0.8, anchor="e")
btnSubmit = tk.Button(root, text="Roll", command=getPlace, font=("Arial", 12, "bold"), bg=tableColor, fg="yellow")
btnSubmit.place(relx=0.5, rely=0.9, anchor=CENTER)

lblPass = tk.Label(root, text="PASS", font=("Arial", 12, "bold"), bg="yellow", fg="red", height=1 , width=46)
lblPass.place(relx=.5, rely=0.75, anchor="s")
chkFour = tk.Checkbutton(root, text="", variable=onFour, onvalue=4, offvalue=0,bg=placeColor, relief="raised")
chkFour.place(relx=0.13, rely=0.48, anchor=CENTER)
chkFive = tk.Checkbutton(root, text="", variable=onFive, onvalue=5, offvalue=0,bg=placeColor, relief="raised")
chkFive.place(relx=0.26, rely=0.48, anchor=CENTER)
chkSix = tk.Checkbutton(root, text="", variable=onSix, onvalue=6, offvalue=0.,bg=placeColor, relief="raised")
chkSix.place(relx=0.38, rely=0.48, anchor=CENTER)
chkEight = tk.Checkbutton(root, text="", variable=onEight, onvalue=8, offvalue=0,bg=placeColor, relief="raised")
chkEight.place(relx=0.5, rely=0.48, anchor=CENTER)
chkNine = tk.Checkbutton(root, text="", variable=onNine, onvalue=9, offvalue=0,bg=placeColor, relief="raised")
chkNine.place(relx=0.63, rely=0.48, anchor=CENTER)
chkTen = tk.Checkbutton(root, text="", variable=onTen, onvalue=10, offvalue=0,bg=placeColor, relief="raised")
chkTen.place(relx=0.76, rely=0.48, anchor=CENTER)
frmCome = tk.Frame(root, bg="teal", height=53, width=500, borderwidth=4, relief="raised")
frmCome.place(relx=0.50,rely=0.6, anchor=CENTER)
lblCome = tk.Label(frmCome, text="Come", font=("Arial", 18, "bold"), bg="teal", fg="white")
lblCome.place(relx= 0.15,rely=0.50, anchor="w")

bet5 = tk.IntVar()
bet10 = tk.IntVar()
bet25 = tk.IntVar()
bet50 = tk.IntVar()
bet100 = tk.IntVar()

radioOne = tk.Radiobutton(root, text="5", variable=bet5, value=5)
radioOne.place(relx=0.3, rely=0.8, anchor=CENTER)

radioTwo = tk.Radiobutton(root, text="10", variable=bet10, value=10)
radioTwo.place(relx=0.41, rely=0.8, anchor=CENTER)

radioThree = tk.Radiobutton(root, text="25", variable=bet25, value=25)
radioThree.place(relx=0.53, rely=0.8, anchor=CENTER)

radioFour = tk.Radiobutton(root, text="50", variable=bet50, value=50)
radioFour.place(relx=0.65, rely=0.8, anchor=CENTER)

radioFive = tk.Radiobutton(root, text="100", variable=bet100, value=100)
radioFive.place(relx=0.78, rely=0.8, anchor=CENTER)


# Run the Tkinter event loop
root.mainloop()
