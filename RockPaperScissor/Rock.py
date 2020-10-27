import tkinter as tk

import random

root = tk.Tk()
root.title("Rock, Paper, Scissor Game")
width = 570
height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#99ff99")


#================================IMAGES========================================
blank_img=tk.PhotoImage(file="images/blank.png")
player_rock=tk.PhotoImage(file="images/player_rock.png")
sm_player_rock=player_rock.subsample(3, 3)
player_paper=tk.PhotoImage(file="images/player_paper.png")
sm_player_paper=player_paper.subsample(3, 3)
player_scissor=tk.PhotoImage(file="images/player_scissor.png")
sm_player_scissor= player_scissor.subsample(3, 3)
com_rock=tk.PhotoImage(file="images/com_rock.png")
com_paper=tk.PhotoImage(file="images/com_paper.png")
com_scissor=tk.PhotoImage(file="images/com_scissor.png")


#===============================METHODS========================================
def Rock():
    global player_choice
    player_choice = 1
    player_img.configure(image=player_rock)
    MatchProcess()
 
def Paper():
    global player_choice
    player_choice = 2
    player_img.configure(image=player_paper)
    MatchProcess()
    
def Scissor():
    global player_choice
    player_choice = 3
    player_img.configure(image=player_scissor)
    MatchProcess()

def MatchProcess():
    com_choice = random.randint(1,3)
    if com_choice == 1:
        comp_img.configure(image=com_rock)
        ComputerRock()
    elif com_choice == 2:
        comp_img.configure(image=com_paper)
        ComputerPaper()
        
    elif com_choice == 3:
        comp_img.configure(image=com_scissor)
        CompututerScissor()

def ComputerRock():
    if player_choice == 1:
        lbl_status.config(text="Game Tie")
    elif player_choice == 2:
        lbl_status.config(text="Player Win")
    elif player_choice == 3:
        lbl_status.config(text="Computer Win")
           
def ComputerPaper():
    if player_choice == 1:
        lbl_status.config(text="Computer Win")
    elif player_choice == 2:
        lbl_status.config(text="Game Tie")
    elif player_choice == 3:
        lbl_status.config(text="Player Win")
    
def CompututerScissor():
    if player_choice == 1:
        lbl_status.config(text="Player Win")
    elif player_choice == 2:
        lbl_status.config(text="Computer Win")
    elif player_choice == 3:
        lbl_status.config(text="Game Tie")

def ExitApp():
    root.destroy()
    exit()

#===============================LABEL WIDGET=========================================
player_img = tk.Label(root,image=blank_img)
comp_img = tk.Label(root,image=blank_img)
lbl_player = tk.Label(root,text="PLAYER")
lbl_player.grid(row=1, column=1)
lbl_player.config(bg="#99ff99")
lbl_computer = tk.Label(root,text="COMPUTER")
lbl_computer.grid(row=1, column=3)
lbl_computer.config(bg="#99ff99")
lbl_status= tk.Label(root, text="", font=('arial', 8))
lbl_status.config(bg="#99ff99")
player_img.grid(row=2,column=1, padx=30, pady=20)
comp_img.grid(row=2,column=3, pady=20)
lbl_status.grid(row=3, column=2)


#===============================BUTTON WIDGET===================================
rock = tk.Button(root, image=sm_player_rock, command=Rock)
paper = tk.Button(root, image=sm_player_paper, command=Paper)
scissor = tk.Button(root, image=sm_player_scissor, command=Scissor)
btn_quit = tk.Button(root, text="Quit", command=ExitApp)
rock.grid(row=4,column=1, pady=30)
paper.grid(row=4,column=2, pady=30)
scissor.grid(row=4,column=3, pady=30)
btn_quit.grid(row=5, column=2)

#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
