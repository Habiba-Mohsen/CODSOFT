from tkinter import *
from PIL import Image,ImageTk
from random import randint 
##main window##
screen =Tk()
screen.title("Rock Paper Scissors Game")
screen.configure(background="#B3F3FF")
## images ##
rock_user=ImageTk.PhotoImage(Image.open("r-user.png"))
paper_user=ImageTk.PhotoImage(Image.open("p-user.png"))
scissor_user=ImageTk.PhotoImage(Image.open("s-user.png"))
rock_comp=ImageTk.PhotoImage(Image.open("r-comp.png"))
paper_comp=ImageTk.PhotoImage(Image.open("p-comp.png"))
scissor_comp=ImageTk.PhotoImage(Image.open("s-comp.png"))
## styling ##
user_label=Label(screen,image=paper_user,bg="#B3F3FF")
comp_label=Label(screen,image=rock_comp,bg="#B3F3FF")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)
user_score=Label(screen,text='0',bg="#B3F3FF",font=100,fg="black")
comp_score=Label(screen,text='0',bg="#B3F3FF",font=100,fg="black")
user_score.grid(row=1,column=3)
comp_score.grid(row=1,column=1)
rock = Button(screen, width=20, height=2, text="ROCK", fg="black", bg="#A2CAF5",  font=("Verdana", 12, "bold"),bd=0,command=lambda:UpdateChoice("rock")).grid(row=2, column=0)
scissor = Button(screen, width=20, height=2, text="SCISSOR", fg="black", bg="#A2CAF5",  font=("Verdana", 12, "bold"),bd=0,command=lambda:UpdateChoice("scissor")).grid(row=2,column=2)
paper = Button(screen, width=20, height=2, text="PAPER", fg="black", bg="#A2CAF5",  font=("Verdana", 12, "bold"),bd=0,command=lambda:UpdateChoice("paper")).grid(row=2, column=4)
user_indicator=Label(screen,font=50,text="You",bg="#B3F3FF").grid(row=0,column=4)
comp_indicator=Label(screen,font=50,text="Computer",bg="#B3F3FF").grid(row=0,column=0)
msg=Label(screen,font=50,bg="#B3F3FF")
msg.grid(row=5,column=2)
## functionality
options=["rock","paper","scissor"]
def checkWin(player,computer):
    if player==computer:
        UpdateMessage("DRAW!")
    elif player=="rock":
        if computer=="paper":
            UpdateMessage("you LOSE")
            UpdateCompScore()
        else: 
            UpdateMessage("you WIN")
            UpdateUserScore()
    elif player=="scissor":
        if computer=="rock":
            UpdateMessage("you LOSE")
            UpdateCompScore()
        else:
            UpdateMessage("you WIN")
            UpdateUserScore()
    elif player=="paper":
        if computer=="scissor":
            UpdateMessage("you LOSE")
            UpdateCompScore()
        else:
            UpdateMessage("you WIN")
            UpdateUserScore()  
def UpdateMessage(y):
    msg.config(text=y)   
def UpdateUserScore():
    score= int(user_score["text"])
    score= score+1
    user_score["text"]=str(score)
def UpdateCompScore():
    score=int(comp_score["text"])
    score+=1
    comp_score.config(text=str(score))
def UpdateChoice(x):
    ##comp choice
    compChoice=options[randint(0,2)]
    if compChoice=="rock":
        comp_label.configure(image=rock_comp)
    elif compChoice=="paper":
        comp_label.configure(image=paper_comp)
    elif compChoice=="scissor":
        comp_label.configure(image=scissor_comp)
    ##user choice
    if x=="rock":
        user_label.configure(image=rock_user)
    elif x=="paper":
        user_label.configure(image=paper_user)
    elif x=="scissor":
        user_label.configure(image=scissor_user)
    checkWin(x,compChoice) 
screen.mainloop()