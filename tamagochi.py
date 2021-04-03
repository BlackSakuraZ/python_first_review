from tkinter import *
from tkinter.messagebox import *


flag = False
energy = 101
fun = 101
satiety = 101
health = 101
name = 0
color = ""
toggle = True
sleepy = True


def alll():
    def show():
        stroka = str("""Welcome to the tamagochi! Here you can create your own pet.
        At the beginning you should choose your pets's color and name and click save.
        Congratulations, your pet is created! It has four states: health, fun, satiety and energy.
        To increase first three of them you should click on buttons heal, play and feed respectively.
        To increase energy put your pet to sleep. Please, don't click this button twice.
        Attention! If one of the states will be 0, your pet will die, you will be able to restart game.
        Good luck!""")
        showinfo("Guide", stroka)
    def coma():
        showinfo("Information", "Your pet is dead")
        answer = askquestion("Restart", "Do yo want to try again?")
        if answer == "yes":
            global flag, name, color, satiety, health, fun, energy
            flag = True
            root.destroy()
            flag = False
            name = 0
            color = ""
            satiety = 101
            health = 101
            fun = 101
            energy = 101
            alll()
        else:
            root.destroy()

    def ok():
        showinfo("Information", "saved successfully")
        global name
        name = entry.get()
        global color
        if col.get() == 1:
            color = "tomato"
        if col.get() == 2:
            color = "gold"
        if col.get() == 3:
            color = "sky blue"
        if col.get() == 4:
            color = "SeaGreen1"
        if col.get() == 5:
            color = "magenta"
        win.destroy()

    def toggle_eyes():
        global flag
        if flag:
            return
        global toggle
        if toggle:
            current_color = can.itemcget(eye_left, 'fill')
            if current_color == 'white':
                new_color = can.body_color
                can.itemconfigure(pupil_left, fill=new_color, outline=new_color)
                can.itemconfigure(pupil_right, fill=new_color, outline=new_color)
            else:
                new_color = 'white'
                can.itemconfigure(pupil_left, fill="black", outline="black")
                can.itemconfigure(pupil_right, fill="black", outline="black")
            can.itemconfigure(eye_left, fill=new_color)
            can.itemconfigure(eye_right, fill=new_color)
            root.after(800, toggle_eyes)
        else:
            global sleepy
            sleepy = True

    def show_happy(event):
        global flag
        if flag:
            return
        if (20 <= event.x <= 350) and (20 <= event.y <= 100):
            global fun
            fun = min(100, fun + 5)
            st = str(fun)
            f.delete(1.0, END)
            f.insert(1.0, st)
            can.itemconfigure(cheek_left, state=NORMAL)
            can.itemconfigure(cheek_right, state=NORMAL)
            can.itemconfigure(mouth_normal, state=HIDDEN)
            can.itemconfigure(mouth_happy, state=NORMAL)
        else:
            can.itemconfigure(cheek_left, state=HIDDEN)
            can.itemconfigure(cheek_right, state=HIDDEN)
            can.itemconfigure(mouth_normal, state=NORMAL)
            can.itemconfigure(mouth_happy, state=HIDDEN)

    def decline_in_satiety():
        global flag
        if flag:
            return
        global satiety
        if satiety == 0:
            coma()
        satiety -= 1
        st = str(satiety)
        sat.delete(1.0, END)
        sat.insert(1.0, st)
        root.after(10000, decline_in_satiety)

    def decline_in_fun():
        global flag
        if flag:
            return
        global fun
        if fun == 0:
            coma()
        fun -= 1
        st = str(fun)
        f.delete(1.0, END)
        f.insert(1.0, st)
        root.after(6000, decline_in_fun)

    def decline_in_health():
        global flag
        if flag:
            return
        global health
        if health == 0:
            coma()
        health -= 1
        st = str(health)
        h.delete(1.0, END)
        h.insert(1.0, st)
        root.after(14000, decline_in_health)

    def decline_in_energy():
        global flag
        if flag:
            return
        global energy
        if energy == 0:
            coma()
        energy -= 1
        st = str(energy)
        en.delete(1.0, END)
        en.insert(1.0, st)
        root.after(3000, decline_in_energy)

    def increase_health():
        global health
        health = min(100, health + 5)
        st = str(health)
        h.delete(1.0, END)
        h.insert(1.0, st)

    def increase_fun():
        global fun
        fun = min(100, fun + 5)
        st = str(fun)
        f.delete(1.0, END)
        f.insert(1.0, st)

    def increase_satiety():
        global satiety
        satiety = min(100, satiety + 5)
        st = str(satiety)
        sat.delete(1.0, END)
        sat.insert(1.0, st)

    def sleep():
        global sleepy
        if sleepy:
            global toggle
            toggle = False
            root.after(70)
            global color
            can.itemconfigure(pupil_left, fill=color, outline=color)
            can.itemconfigure(pupil_right, fill=color, outline=color)
            can.itemconfigure(eye_left, fill=color)
            can.itemconfigure(eye_right, fill=color)
            global energy
            energy = min(101, energy + 6)
            increase_health()
            root.after(10000, sleep)
        else:
            sleepy = True


    def wake_up():
        global toggle
        if not toggle:
            toggle = True
            global sleepy
            sleepy = False
            toggle_eyes()

    rt = Tk()
    show()
    rt.destroy()

    win = Tk()
    win.title("settings")
    col = IntVar()
    lab = Label(text="Choose your pet's color")
    r1 = Radiobutton(text="red", variable=col, value=1)
    r1.grid(row=1, column=0, sticky=W)
    r1.select()
    r2 = Radiobutton(text="yellow", variable=col, value=2)
    r2.grid(row=2, column=0, sticky=W)
    r3 = Radiobutton(text="light blue", variable=col, value=3)
    r3.grid(row=3, column=0, sticky=W)
    r4 = Radiobutton(text="green", variable=col, value=4)
    r4.grid(row=4, column=0, sticky=W)
    r5 = Radiobutton(text="purple", variable=col, value=5)
    r5.grid(row=5, column=0, sticky=W)
    # labl = Label(textvariable=col, state=NORMAL).grid(row=0, column=0)

    label = Label(text="Enter your pet's name")
    label.grid(row=6, column=0)
    entry = Entry()
    entry.grid(row=6, column=1)
    check = Button(text="save", font=("Ubuntu", 10), command=ok)
    check.grid(row=7, columnspan=2)
    win.mainloop()

    root = Tk()
    global name
    root.title(name)
    can = Canvas(root, width=400, height=400)

    # creating pet
    global color
    can.body_color = color
    body = can.create_oval(35, 20, 365, 350, fill=can.body_color)
    ear_left = can.create_polygon(75, 80, 75, 10, 165, 70, fill=can.body_color)
    ear_right = can.create_polygon(255, 45, 325, 10, 325, 77, fill=can.body_color)
    mouth_normal = can.create_line(170, 250, 200, 272, 230, 250, width=2, smooth=1)
    foot_left = can.create_oval(65, 320, 145, 360, fill=can.body_color)
    foot_right = can.create_oval(250, 320, 330, 360, fill=can.body_color)
    eye_left = can.create_oval(130, 110, 160, 170, fill="white")
    eye_right = can.create_oval(230, 110, 260, 170, fill="white")
    pupil_left = can.create_oval(140, 130, 150, 155, fill="black")
    pupil_right = can.create_oval(240, 130, 250, 155, fill="black")
    cheek_left = can.create_oval(70, 180, 120, 230, fill='pink', state=HIDDEN)
    cheek_right = can.create_oval(280, 180, 330, 230, fill='pink', state=HIDDEN)
    mouth_happy = can.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)

    can.grid(rowspan=17, columnspan=4)

    toggle_eyes()

    can.bind('<Motion>', show_happy)

    feed = Button(text="FEED", width=10, height=2, command=increase_satiety)
    feed.grid(row=9, column=5, sticky=W)

    play = Button(text="PLAY", width=10, height=2, command=increase_fun)
    play.grid(row=11, column=5, sticky=W)

    heal = Button(text="HEAL", width=10, height=2, command=increase_health)
    heal.grid(row=13, column=5, sticky=W)

    put = Button(text="PUT TO SLEEP", width=10, height=2, command=sleep)
    put.grid(row=15, column=5, sticky=W)

    wake = Button(text="WAKE UP", width=10, height=2, command=wake_up)
    wake.grid(row=17, column=5, sticky=W)

    s = "SATIETY"
    SATIETY = Text(width=8, height=1)
    SATIETY.insert(1.0, s)
    SATIETY.grid(row=0, column=5)

    s = "FUN"
    FUN = Text(width=8, height=1)
    FUN.insert(1.0, s)
    FUN.grid(row=2, column=5)

    s = "HEALTH"
    HEALTH = Text(width=8, height=1)
    HEALTH.insert(1.0, s)
    HEALTH.grid(row=4, column=5)

    s = "ENERGY"
    ENERGY = Text(width=8, height=1)
    ENERGY.insert(1.0, s)
    ENERGY.grid(row=6, column=5)

    global satiety
    s = str(satiety)
    sat = Text(width=3, height=1)
    sat.insert(1.0, s)
    sat.grid(row=0, column=6)

    global fun
    s = str(fun)
    f = Text(width=3, height=1)
    f.insert(1.0, s)
    f.grid(row=2, column=6)

    global health
    s = str(health)
    h = Text(width=3, height=1)
    h.insert(1.0, s)
    h.grid(row=4, column=6)

    global energy
    s = str(energy)
    en = Text(width=3, height=1)
    en.insert(1.0, s)
    en.grid(row=6, column=6)

    decline_in_satiety()
    decline_in_fun()
    decline_in_health()
    decline_in_energy()

    root.mainloop()


alll()
