from tkinter import *
from tkinter import messagebox
import lotteri

# Create root window
root = Tk()
root.title("Lotteri")
root.geometry("400x400")

# Create listbox object
listbox = Listbox(root, height=4, width=30, bg="white", activestyle="dotbox", font="Helvetica", fg="black")
lotteri_obj = lotteri.Lotteri()  # Rename the object to avoid conflicts

# Vinst = lotteri.get_vinst()
# print(f'vinst= {vinst}')

label_antal = Label(root, text="Antal lotter, max 3 st: ")
label_antal.grid(row=0, column=0, sticky=E, padx=5, pady=5)
textbox_antal = Entry(root, width=2)
textbox_antal.grid(row=0, column=1, sticky=W, padx=5, pady=5)
textbox_antal.focus_set()

# Functions()--------------
def update_listbox(antal_lotter):
    listbox.delete(0, END)
    
    try:
        int_antal_lotter = int(antal_lotter)
        
        if int_antal_lotter < 4:
            for i in range(int_antal_lotter):
                vinst = lotteri_obj.get_vinst()  # Use the renamed object
                listbox.insert(END, vinst)  # Use END to add to the end of the listbox
        else:
            messagebox.showinfo("Felmeddelande", "Du har valt för många lotter!")

    except ValueError:
        messagebox.showinfo("Felmeddelande", "Endast siffror tillåtet")

def click_slumpa_button():
    antal_lott = textbox_antal.get()
    textbox_antal.delete(0, END)
    textbox_antal.focus_set()
    update_listbox(antal_lott)

# Slut på funktioner()

button_slumpa = Button(text="Slumpa", command=click_slumpa_button)
button_slumpa.grid(row=1, column=0, columnspan=2, padx=15, pady=15)

listbox.grid(row=2, column=0, columnspan=2, padx=15, pady=15)

root.mainloop()