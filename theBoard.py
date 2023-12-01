import tkinter as tk
from tkinter import messagebox, CENTER

root = tk.Tk()

tableColor = '#0c6122'
placeColor = '#070c52'
root.title("Welcome to True Odds Craps")
root.geometry("600x600")
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
rollOne = tk.IntVar()

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
    import random

    def generate_random_number():
        return random.randint(1, 6)


rollOne = tk.IntVar()
rOne=rollDice()


def showRoll(rOne):
    rollOne = rOne
    lblRoll.place(relx=0.28, rely=0.8, anchor=CENTER)
# Create a "File" menu

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add items to the "File" menu
file_menu.add_command(label="New Game", command=new_game)
file_menu.add_command(label="Quit Game", command=quit_game)
file_menu.add_command(label="Exit", command=exit_program)

# Load and display an image
image_path = "Images/Dice-icon.png"
img_path = "Images/Chip-5.png"
img25_path = "Images/Chip-25.png"
img50_path = "Images/Chip-50.png"
img100_path = "Images/Chip-100.png"
try:
    # Open and read the image file
    image = tk.PhotoImage(file=image_path)
    img = tk.PhotoImage(file=img_path)
    img25 = tk.PhotoImage(file=img25_path)
    img50 = tk.PhotoImage(file=img50_path)
    img100 = tk.PhotoImage(file=img100_path)

    # Create a label and set the image
    image_label = tk.Label(root, image=image, borderwidth=4, relief="raised")
    image_label.place(relx=0.12, rely=0.11, anchor=CENTER)  # Adjust padding as needed
    imgLabel = tk.Label(root, image=img, borderwidth=4, relief="raised")
    imgLabel.place(relx=0.38, rely=0.8, anchor=CENTER)
    img25Label = tk.Label(root, image=img25, borderwidth=4, relief="raised")
    img25Label.place(relx=0.48, rely=0.8, anchor=CENTER)
    img50Label = tk.Label(root, image=img50, borderwidth=4, relief="raised")
    img50Label.place(relx=0.58, rely=0.8, anchor=CENTER)
    img100Label = tk.Label(root, image=img100, borderwidth=4, relief="raised")
    img100Label.place(relx=0.68, rely=0.8, anchor=CENTER)

    lblBank = tk.Label(root, text="Bank", font=("Arial", 18, ""), bg=tableColor, fg="white")
    lblBank.place(relx=0.62, rely=0.11, anchor=CENTER)
    lblBalance = tk.Label(root, text="Balance", font=("Arial", 12,), bg=tableColor, fg="white")
    lblBalance.place(relx=0.75, rely=0.11, anchor=CENTER)

except tk.TclError:
    # Handle if the image file is not found or not supported
    messagebox.showerror("Error", f"Unable to load image: {image_path}")

lblOne = tk.Label(root, text="4      5      6       8       9       10", font=("Arial", 21, "bold"), bg=tableColor,
                  fg="white", )
lblOne.place(relx=0.49, rely=0.23, anchor=CENTER)

entryFour = tk.Entry(root, font=("Arial", 12, "bold"), width=5, bg=tableColor, fg="white")
entryFour.place(relx=0.19, rely=0.28, anchor=CENTER)
entryFive = tk.Entry(root, font=("Arial", 12, "bold"), width=5, bg=tableColor, fg="white")
entryFive.place(relx=0.30, rely=0.28, anchor=CENTER)
entrySix = tk.Entry(root, font=("Arial", 12, "bold"), width=5, bg=tableColor, fg="white")
entrySix.place(relx=0.36, rely=0.26, )
entryEight = tk.Entry(root, font=("Arial", 12, "bold"), width=5, bg=tableColor, fg="white")
entryEight.place(relx=0.52, rely=0.28, anchor=CENTER)
entryNine = tk.Entry(root, font=("Arial", 12, "bold"), width=5, bg=tableColor, fg="white")
entryNine.place(relx=0.65, rely=0.28, anchor=CENTER)
entryTen = tk.Entry(root, font=("Arial", 12, "bold"), width=5, bg=tableColor, fg="white")
entryTen.place(relx=0.78, rely=0.28, anchor=CENTER)

# Place the Dice
dieOne_path = "Images/dice-6.png"
dieOne = tk.PhotoImage(file=dieOne_path)
lblDieOne = tk.Label(root, image=dieOne, borderwidth=4, )
lblDieOne.place(relx=0.40, rely=0.42, anchor=CENTER)
dieTwo_path = "Images/dice-5.png"
dieTwo = tk.PhotoImage(file=dieTwo_path)
lblDieTwo = tk.Label(root, image=dieTwo, borderwidth=4, )
lblDieTwo.place(relx=0.55, rely=0.42, anchor=CENTER)

lblRoll = tk.Label(root, text=rollOne.get(), font=("Arial", 12), bg="yellow", fg="red", width=5, relief="raised")
lblRoll.place(relx=0.28, rely=0.8, anchor=CENTER)

lblBet = tk.Label(root, text="Bet", font=("Arial", 12, "bold"), bg="yellow", fg="red", width=5, relief="raised")
lblBet.place(relx=0.28, rely=0.8, anchor="e")
btnSubmit = tk.Button(root, text="Roll", command=rollDice, font=("Arial", 12, "bold"), bg=tableColor, fg="yellow")
btnSubmit.place(relx=0.5, rely=0.9, anchor=CENTER)

lblPass = tk.Label(root, text="PASS", font=("Arial", 12, "bold"), bg="yellow", fg="red", height=1, width=50)
lblPass.place(relx=.5, rely=0.72, anchor="s")

frmCome = tk.Frame(root, bg="teal", height=65, width=450, borderwidth=4, relief="raised")
frmCome.place(relx=0.50, rely=0.6, anchor=CENTER)
lblCome = tk.Label(frmCome, text="Come", font=("Arial", 18, "bold"), bg="teal", fg="white")
lblCome.place(relx=0.15, rely=0.50, anchor="w")

bet5 = tk.IntVar()
bet25 = tk.IntVar()
bet50 = tk.IntVar()
bet100 = tk.IntVar()

# Run the Tkinter event loop
root.mainloop()
