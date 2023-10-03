from tkinter import *
from tkinter import messagebox
import lotteri
# create root window
root = Tk()
root.title("Lotteri")
root.geometry("1280x720")
# creat listbox object
listbox = Listbox(root, height=4, width=30, bg="white", activestyle="dotbox", font="Helvetica", fg="white")
lotteri = lotteri.Lotteri()

#vinst = lotteri.get_vinst()
#print(f'vinst= {vinst}')

label_antal = Label(root, text="antal lotter, max 3 st: ")
label_antal.grid(row=0, column=0, sticky=E, padx=5, pady=5)
textbox_antal = Entry(root, width=2)
textbox_antal.grid(row=0, column=1, sticky=W, padx=5, pady=5)
textbox_antal.focus_set()

#Funktioner()--------------
def update_listBox(antal_lotter):
    #print("update_listBox")
    listbox.delete(0, END)
    listbox.insert(1, "Grattis du vann den här")

    try:
        int_antal_lotter = int(antal_lotter)
        i=0

        if (int_antal_lotter < 4):
         while i<int_antal_lotter:
                vinst= lotteri.get_vinst()
                listbox.insert((i+2), vinst)
                i = i+1
        else:
            messagebox.showinfo("Du har valt för många lotter!")
            
    

    except ValueError:
        messagebox.showinfo("Endast siffror tillåtet")
 

def clickSlumpsaButton():
    #print("clickSlumpabutton()")

    antal_lott = textbox_antal.get()
    #tömmer textboxen efter tryck
    textbox_antal.delete(0, END)
    textbox_antal.focus_set()

    update_listBox(antal_lott)



#slut på funktioner()

button_slumpa = Button(text="tur knapp", command=clickSlumpsaButton)
button_slumpa.grid(row=1, column=0, columnspan=2, padx=15, pady=15)

listbox.grid(row=2, column=0, columnspan=2, padx=15, pady=15)

root.mainloop()