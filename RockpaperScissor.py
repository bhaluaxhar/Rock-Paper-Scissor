from tkinter import *
from random import choice

root = Tk()
root.geometry("800x600")
root.title("Rock Paper game By Trio")
score = 0
cScore = 0
Round = 19
root.resizable(False, False)


def active():
    global score
    global cScore
    global Round
    # global won
    # global lose
    # global draw
    rock_btn["stat"] = "normal"
    paper_btn["stat"] = "normal"
    scissor_btn["stat"] = "normal"
    if score > cScore:
        won.destroy()
    elif score <cScore:
        lose.destroy()
    elif score == 0 and cScore ==0:
        pass
    elif score == cScore:
        draw.destroy()
    else:
        pass
    score = 0
    cScore = 0
    Round = 22
    msg["text"] = ""
    compChoice["text"] = ""
    userChoice["text"] = ""
    compScore["text"] = ""
    userScore["text"] = ""
    Rounds["text"] = ""
    winner["text"] = ""

def rock():
    global score
    global cScore
    userChoice['text'] = "You choosed : Rock"
    comp_list = ["Rock","Paper","Scissor"]
    comp_list_choice = choice(comp_list)
    compChoice["text"] = f"Bot choosed : {comp_list_choice}"
    rounds()
    if comp_list_choice == "Rock":
        msg['text'] = "It is Draw"
    if comp_list_choice == "Paper":
        msg['text'] = "Bot wins"
        cScore +=1
        compScore["text"] = f"Bot Score: {cScore}"
    if comp_list_choice == "Scissor":
        msg['text'] = "You Win"
        score +=1
        userScore["text"] = f"Player Score: {score}"
    root.update()
def paper():
    global score
    global cScore
    userChoice['text'] = "You choosed : Paper"
    comp_list = ["Rock", "Paper", "Scissor"]
    comp_list_choice = choice(comp_list)
    compChoice["text"] = f"Bot choosed : {comp_list_choice}"
    rounds()
    if comp_list_choice == "Rock":
        msg['text'] = "You win"
        score += 1
        userScore["text"] = f"Player Score: {score}"
    if comp_list_choice == "Paper":
        msg['text'] = "It is Draw"
    if comp_list_choice == "Scissor":
        msg['text'] = "Bot Win"
        cScore += 1
        compScore["text"] = f"Bot Score: {cScore}"
    root.update()
def scissor():
    global score
    global cScore
    userChoice['text'] = "You choosed : Scissor"
    comp_list = ["Rock", "Paper", "Scissor"]
    comp_list_choice = choice(comp_list)
    compChoice["text"] = f"Bot choosed : {comp_list_choice}"
    rounds()
    if comp_list_choice == "Rock":
        msg['text'] = "Bot win"
        cScore += 1
        compScore["text"] = f"Bot Score: {cScore}"
    if comp_list_choice == "Paper":
        msg['text'] = "Player wins"
        score += 1
        userScore["text"] = f"Player Score: {score}"
    if comp_list_choice == "Scissor":
        msg['text'] = "It is Draw"
    root.update()

def rounds():
    global Round
    for i in range(Round):
        Round = Round - 1
        if Round == 1:
            Rounds["text"] = f"Round Left {0}"
            # rock_btn["stat"] = "disabled"
            # scissor_btn["stat"] = "disabled"
            # paper_btn["stat"] = "disabled"
            # Winner()
            break
        elif Round ==2:
            rock_btn["stat"] = "disabled"
            scissor_btn["stat"] = "disabled"
            paper_btn["stat"] = "disabled"
            Winner()
        else:
            Rounds["text"] = f"Round Left {Round-1}"
            break
    print(Round)

def Winner():
    global won
    global lose
    global draw
    compScore["text"] = ""
    userScore["text"] = ""
    if score >cScore:
        winner["text"] = "You Won The Match!!!"
        won = Label(root, image=photo, bg="#fbeb04", fg="black", width=800, height=500, relief=RIDGE, borderwidth=0)
        won.place(relx=1, x=-25, y=90, anchor=NE)
    elif score <cScore:
        winner["text"] = "Bot Won The Match!!!"
        lose = Label(root, image=photo2, bg="#fbeb04", fg="black", width=800, height=500, relief=RIDGE, borderwidth=0)
        lose.place(relx=1, x=-25, y=90, anchor=NE)
    elif score == cScore:
        winner["text"] = "Match is Draw"
        draw = Label(root, image=photo3, bg="#fbeb04", fg="black", width=800, height=500, relief=RIDGE, borderwidth=0)
        draw.place(relx=1, x=-25, y=90, anchor=NE)
    else:
        pass


# Background Image


f = PhotoImage(file = "gallery/try.png")
background_label = Label(root, image=f)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# background Image
# background_image = root.PhotoImage(file = "try.png")
# background_label = root.Label(root, image=background_image)
# background_label.place(x=0,y=0, relwidth=1, relheight=1)

# Images of button
rockImg = PhotoImage(file = "gallery/rock.PNG")
paperImg = PhotoImage(file = "gallery/paper.PNG")
scissorImg = PhotoImage(file = "gallery/scissor.PNG")
startImg = PhotoImage(file = "gallery/Play.PNG")
photo =  PhotoImage(file = "gallery/win.png")
photo2 =  PhotoImage(file = "gallery/lose.png")
photo3 =  PhotoImage(file = "gallery/DRAW.png")

rock_btn = Button(root, text="Rock", font="bold", width=76, height=28,relief=RIDGE,borderwidth=0,image = rockImg, command=rock)
rock_btn["stat"] = "disabled"
rock_btn.place(relx = 1, x =-613, y = 492, anchor = NE)
#rock_btn.pack()

paper_btn = Button(root, text="Paper", font="bold", width=78, height=28, relief=RIDGE,borderwidth=0,image = paperImg, command=paper)
paper_btn["stat"] = "disabled"

paper_btn.place(relx = 1, x =-110, y = 492, anchor = NE)
# paper_btn.pack()

scissor_btn = Button(root, text="Scissor", font="bold", width=120, height=28, relief=RIDGE,borderwidth=0,image = scissorImg, command=scissor)
scissor_btn["stat"] = "disabled"

scissor_btn.place(relx = 1, x =-340, y = 491, anchor = NE)
# scissor_btn.pack()

active_btn = Button(root, image=startImg,bg = "#fbeb04",fg="black", font="bold", width=140, height=100, relief=RIDGE,borderwidth=0,command=active)
active_btn.place(relx = 1, x =-310, y = 10, anchor = NE)
active_btn.pack()

userChoice = Label(root, text="",bg = "#fbeb04",fg="black", font="bold", width=20, height=1, relief=RIDGE,borderwidth=0)
userChoice.place(relx = 1, x =-500, y = 25, anchor = NE)
userChoice.pack()

userScore = Label(root, text= "",bg = "#fbeb04",fg="black", font="bold", width=20, height=1, relief=RIDGE,borderwidth=0)
userScore.place(relx = 1, x =-650, y = 25, anchor = NE)

compChoice = Label(root, text="",bg = "#fbeb04",fg="black", font="bold", width=25, height=1, relief=RIDGE,borderwidth=0)
compChoice.pack()

compScore = Label(root, text= "",bg = "#fbeb04",fg="black", font="bold", width=20, height=1, relief=RIDGE,borderwidth=0)
compScore.place(relx = 1, x =-500, y = 25, anchor = NE)

msg = Label(root, text="", bg = "#fbeb04",fg="black", font="bold", width=20, height=1, relief=RIDGE,borderwidth=0)
msg.pack()

Rounds = Label(root, text= "",bg = "#fbeb04",fg="black", font="bold", width=20, height=1, relief=RIDGE,borderwidth=0)
Rounds.place(relx = 1, x =-10, y = 25, anchor = NE)

winner = Label(root, text= "",bg = "#fbeb04",fg="black", font="bold", width=20, height=1, relief=RIDGE,borderwidth=0)
winner.place(relx = 1, x =-310, y = 160, anchor = NE)

root.mainloop()
