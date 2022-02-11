#Import required library.
from tkinter import*
import random
#create object
root=Tk()
#Geometry
root.geometry("1500x1500")
# title
root.title("Rock, Paper and Scissors Game")
#Computer choice
computer_choice={"0":"Rock","1":"Paper","2":"Scissors"}
#Reset game
def reset_game():
    b1["state"]="active"
    b2["state"]="active"
    b3["state"]="active"
    l1.config(text="Player")
    l3.config(text="Computer")
    l4.config(text=" ")
#Disable the Buttons
def button_disable():
    b1["state"]="disable"
    b2["state"]="disable"
    b3["state"]="disable"
        
#If the player selected rock
def rock():
    c=computer_choice[str(random.randint(0,2))]
    if c=="Rock":
       result="Match Draw,try again!"
    elif c=="Scissors":
       result="You Win,Congratulations!"
    else:
       result="Computer Wins,better luck next time!"
    l4.config(text=result)
    l1.config(text="Rock")
    l3.config(text=c)
    button_disable()
#If the player selected paper
def paper():
    c=computer_choice[str(random.randint(0,2))]
    if c=="Paper":
       result="Match Draw,try again!"
    elif c=="Scissors":
       result="Computer Wins,better luck next time!"
    else:
       result="You Win,Congratulations!"
    l4.config(text=result)
    l1.config(text="Paper")
    l3.config(text=c)
    button_disable()
#If the player selected scissors
def scissors():
    c=computer_choice[str(random.randint(0,2))]
    if c=="Rock":
       result="Computer Wins,better luck next time!"
    elif c=="Scissors":
       result="Match Draw,try again!"
    else:
        result="You win,Congratulations!"
    l4.config(text=result)
    l1.config(text="Scissors")
    l3.config(text=c)
    button_disable()

#Add Labels,Frames and Button
Label(root,
      text="Rock,Paper and Scissors Game",
      font="normal 20 bold",fg="purple").pack(pady=20)
frame=Frame(root)
frame.pack()
l1=Label(frame,
         text="Player",
         font=10)

l2=Label(frame,
         text="VS",
         font="normal 20 bold")
l3=Label(frame,text="Computer",font=10)
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack( )
l4=Label(root,
         text=" ",
         font="normal 20 bold",
         bg="yellow",
         width= 30,
         borderwidth= 5,
         relief="solid")
l4.pack(pady=20)
frame1=Frame(root)
frame1.pack()

b1=Button(frame1, text="Rock",
          font=10,width=7,
          command=rock)

b2=Button(frame1,text="Paper",
          font=10,width=7,
          command=paper)
b3=Button(frame1,text="Scissors",
          font=10,width=7,
          command=scissors)

b1.pack(side=LEFT,padx=10)
b2.pack(side=LEFT,padx=10)
b3.pack(side=LEFT,padx=10)

b4=Button(root,text="Play Again",
       font=10,fg="black",
       bg="green",command=reset_game)
b4.pack()

#Executing the game
root.mainloop()
            

        

    
