from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import pickle
##main window
root = Tk()
root.title("To Do List")
root.configure(background="#F4C0F0")
background_photo = ImageTk.PhotoImage(Image.open("Background.png"))
my_menu=Menu(root, bg="#FF7EE3", activebackground="#FF7EE3",activeforeground="#FF7EE3")
root.config(menu=my_menu)
file_menu=Menu(my_menu,tearoff=False,bg="#FF7EE3")
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Save List",command=lambda:save_list())
file_menu.add_separator()
file_menu.add_command(label="Open List",command=lambda:open_list())
file_menu.add_separator()
file_menu.add_command(label="Delete List",command=lambda:delete_list())
##Adding Widgets
tdl = Label(root, image=background_photo, bg="#F4C0F0")
tdl.grid(row=2, column=5, columnspan=25, rowspan=9)  
text_box = Entry(root,width=30)
text_box.grid(row=10, column=9,columnspan=2) 
##Buttons
add_button = Button(root, text="Add Item", width=15, height=1, bg="#FF7EE3",command=lambda:add_item())
add_button.grid(row=10, column=11)
delete_button = Button(root, text="Delete Item", width=15, height=1, bg="#FF7EE3",command=lambda:delete_item())
delete_button.grid(row=10, column=12)
cross_button = Button(root, text="Cross-off Item", width=15, height=1, bg="#FF7EE3",command=lambda:cross_off())
cross_button.grid(row=11, column=11)
uncross_button = Button(root, text="Uncross Item", width=15, height=1, bg="#FF7EE3", command=lambda:uncross())
uncross_button.grid(row=11, column=12)
## list and scrollbar
#tasks=["do homework","go to school","wash dishes","do laundry","solve problems","bake"]
my_scrollbar=Scrollbar(root,bd=0,background="#FF7EE3")
my_list=Listbox(root,bd=0,highlightthickness=0,activestyle="none",selectbackground="#FF7EE3", font=("Arial", 13))
my_list.grid(row=7,column=11)
my_scrollbar.grid(row=7, column=12, sticky="NS")
## Configure the scrollbar to control the Listbox
my_scrollbar.config(command=my_list.yview)
my_list.config(yscrollcommand=my_scrollbar.set)
## Functionality
def delete_item():
    my_list.delete(ANCHOR)
def add_item():
    my_list.insert(END,text_box.get())
    text_box.delete(0,END)
def cross_off():
    my_list.itemconfig(my_list.curselection(),fg="#FF7EE3")
    my_list.selection_clear(0,END)
def uncross():
     my_list.itemconfig(my_list.curselection(),fg="black")
     my_list.selection_clear(0,END)

def delete_list():
    my_list.delete(0,END)
def save_list():
    file_name=filedialog.asksaveasfilename(initialdir="C:/desktop",title="Save File",filetypes=(("Dat files","*.dat"),("All files","*.*")))
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name=f'{file_name}.dat'
    count=0
    while count< my_list.size():
        if my_list.itemcget(count,"fg")=="#FF7EE3":
            my_list.delete(my_list.index(count))
        else: 
            count+=1
    stuff=my_list.get(0,END)
    output=open(file_name,'wb')
    pickle.dump(stuff,output)
def open_list():
    file_name=filedialog.askopenfilename(
    initialdir="C:/desktop",title="Save File",filetypes=(("Dat files","*.dat"),("All files","*.*")))
    if file_name:
        my_list.delete(0,END)
        input_file=open(file_name, 'rb')
        stuff=pickle.load(input_file)
        for item in stuff:
            my_list.insert(END,item)
root.eval("tk::PlaceWindow . center")
root.geometry("500x600")
root.resizable(False,False)
root.mainloop()
