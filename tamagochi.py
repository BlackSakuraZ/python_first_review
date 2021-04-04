from tkinter import Button
from tkinter import Canvas
from tkinter import Entry
from tkinter import END
from tkinter import HIDDEN
from tkinter import IntVar
from tkinter import Label
from tkinter import NORMAL
from tkinter import Radiobutton
from tkinter import Text
from tkinter import Tk
from tkinter import W
from tkinter.messagebox import showinfo
from tkinter.messagebox import askquestion


class StatesOfPet:
    name = ""
    color = ""
    fun = 101
    satiety = 101
    health = 101
    energy = 101


def main():

    pet = StatesOfPet()

    def show():
        information = str("""Welcome to the tamagochi! Here you can create your own pet.
        At the beginning you should choose your pets's color and name and click save.
        Congratulations, your pet is created! It has four states: health, fun, satiety and energy.
        To increase first three of them you should click on buttons heal, play and feed respectively.
        To increase energy put your pet to sleep.
        Attention! If one of the states will be 0, your pet will die, you will be able to restart game.
        Good luck!""")
        showinfo("Guide", information)

    def dead_pet():
        showinfo("Information", "Your pet is dead")
        answer = askquestion("Restart", "Do yo want to try again?")
        if answer == "yes":
            root.destroy()
            pet.fun = 101
            pet.satiety = 101
            pet.health = 101
            pet.energy = 101
            main()
        else:
            root.destroy()

    def show_happy(event):
        if (20 <= event.x <= 350) and (20 <= event.y <= 100):
            pet.fun = min(100, pet.fun + 5)
            st = str(pet.fun)
            state_of_fun.delete(1.0, END)
            state_of_fun.insert(1.0, st)
            canvas.itemconfigure(cheek_left, state=NORMAL)
            canvas.itemconfigure(cheek_right, state=NORMAL)
            canvas.itemconfigure(mouth_normal, state=HIDDEN)
            canvas.itemconfigure(mouth_happy, state=NORMAL)
        else:
            canvas.itemconfigure(cheek_left, state=HIDDEN)
            canvas.itemconfigure(cheek_right, state=HIDDEN)
            canvas.itemconfigure(mouth_normal, state=NORMAL)
            canvas.itemconfigure(mouth_happy, state=HIDDEN)

    def decline_in_satiety():
        if pet.satiety <= 0:
            dead_pet()
        pet.satiety -= 1
        new_state_of_satiety = str(pet.satiety)
        state_of_satiety.delete(1.0, END)
        state_of_satiety.insert(1.0, new_state_of_satiety)
        root.after(10000, decline_in_satiety)

    def decline_in_fun():
        if pet.fun <= 0:
            dead_pet()
        pet.fun -= 1
        new_state_of_fun = str(pet.fun)
        state_of_fun.delete(1.0, END)
        state_of_fun.insert(1.0, new_state_of_fun)
        root.after(6000, decline_in_fun)

    def decline_in_health():
        if pet.health <= 0:
            dead_pet()
        pet.health -= 1
        new_state_of_health = str(pet.health)
        state_of_health.delete(1.0, END)
        state_of_health.insert(1.0, new_state_of_health)
        root.after(14000, decline_in_health)

    def decline_in_energy():
        if pet.energy <= 0:
            dead_pet()
        pet.energy -= 1
        new_state_of_energy = str(pet.energy)
        state_of_energy.delete(1.0, END)
        state_of_energy.insert(1.0, new_state_of_energy)
        root.after(3000, decline_in_energy)

    def increase_health():
        pet.health = min(100, pet.health + 5)
        new_state_of_health = str(pet.health)
        state_of_health.delete(1.0, END)
        state_of_health.insert(1.0, new_state_of_health)

    def increase_fun():
        pet.fun = min(100, pet.fun + 5)
        new_state_of_fun = str(pet.fun)
        state_of_fun.delete(1.0, END)
        state_of_fun.insert(1.0, new_state_of_fun)

    def increase_satiety():
        pet.satiety = min(100, pet.satiety + 5)
        new_state_of_satiety = str(pet.satiety)
        state_of_satiety.delete(1.0, END)
        state_of_satiety.insert(1.0, new_state_of_satiety)

    def sleep():
        pet.energy = 101
        new_color = canvas.body_color
        canvas.itemconfigure(pupil_left, fill=new_color, outline=new_color)
        canvas.itemconfigure(pupil_right, fill=new_color, outline=new_color)
        canvas.itemconfigure(eye_left, fill=new_color)
        canvas.itemconfigure(eye_right, fill=new_color)

    def wake_up():
        new_color = 'white'
        canvas.itemconfigure(pupil_left, fill="black", outline="black")
        canvas.itemconfigure(pupil_right, fill="black", outline="black")
        canvas.itemconfigure(eye_left, fill=new_color)
        canvas.itemconfigure(eye_right, fill=new_color)

    def ok():
        showinfo("Information", "saved successfully")
        pet.name = text_from_pet_name.get()
        if value_of_button.get() == 1:
            pet.color = "tomato"
        if value_of_button.get() == 2:
            pet.color = "gold"
        if value_of_button.get() == 3:
            pet.color = "sky blue"
        if value_of_button.get() == 4:
            pet.color = "SeaGreen1"
        if value_of_button.get() == 5:
            pet.color = "magenta"
        settings_window.destroy()

    rt = Tk()
    show()
    rt.destroy()

    # creating window with settings

    settings_window = Tk()
    settings_window.title("settings")
    value_of_button = IntVar()
    choose_of_pet_color = Label(text="Choose your pet's color")
    red_button = Radiobutton(text="red", variable=value_of_button, value=1)
    red_button.grid(row=1, column=0, sticky=W)
    red_button.select()
    yellow_button = Radiobutton(text="yellow", variable=value_of_button, value=2)
    yellow_button.grid(row=2, column=0, sticky=W)
    blue_button = Radiobutton(text="light blue", variable=value_of_button, value=3)
    blue_button.grid(row=3, column=0, sticky=W)
    green_button = Radiobutton(text="green", variable=value_of_button, value=4)
    green_button.grid(row=4, column=0, sticky=W)
    purple_button = Radiobutton(text="purple", variable=value_of_button, value=5)
    purple_button.grid(row=5, column=0, sticky=W)

    pet_name = Label(text="Enter your pet's name")
    pet_name.grid(row=6, column=0)
    text_from_pet_name = Entry()
    text_from_pet_name.grid(row=6, column=1)
    save_button = Button(text="save", font=("Ubuntu", 10), command=ok)
    save_button.grid(row=7, columnspan=2)
    settings_window.mainloop()

    root = Tk()
    root.title(pet.name)
    canvas = Canvas(root, width=400, height=400)

    # creating pet

    canvas.body_color = pet.color
    body = canvas.create_oval(35, 20, 365, 350, fill=canvas.body_color)
    ear_left = canvas.create_polygon(75, 80, 75, 10, 165, 70, fill=canvas.body_color)
    ear_right = canvas.create_polygon(255, 45, 325, 10, 325, 77, fill=canvas.body_color)
    mouth_normal = canvas.create_line(170, 250, 200, 272, 230, 250, width=2, smooth=1)
    foot_left = canvas.create_oval(65, 320, 145, 360, fill=canvas.body_color)
    foot_right = canvas.create_oval(250, 320, 330, 360, fill=canvas.body_color)
    eye_left = canvas.create_oval(130, 110, 160, 170, fill="white")
    eye_right = canvas.create_oval(230, 110, 260, 170, fill="white")
    pupil_left = canvas.create_oval(140, 130, 150, 155, fill="black")
    pupil_right = canvas.create_oval(240, 130, 250, 155, fill="black")
    cheek_left = canvas.create_oval(70, 180, 120, 230, fill='pink', state=HIDDEN)
    cheek_right = canvas.create_oval(280, 180, 330, 230, fill='pink', state=HIDDEN)
    mouth_happy = canvas.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)

    canvas.grid(rowspan=17, columnspan=4)

    canvas.bind('<Motion>', show_happy)

    # create states of pet in text format

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

    text_in_button_satiety = "SATIETY"
    satiety = Text(width=8, height=1)
    satiety.insert(1.0, text_in_button_satiety)
    satiety.grid(row=0, column=5)

    text_in_button_fun = "FUN"
    fun = Text(width=8, height=1)
    fun.insert(1.0, text_in_button_fun)
    fun.grid(row=2, column=5)

    text_in_button_health = "HEALTH"
    health = Text(width=8, height=1)
    health.insert(1.0, text_in_button_health)
    health.grid(row=4, column=5)

    text_in_button_energy = "ENERGY"
    energy = Text(width=8, height=1)
    energy.insert(1.0, text_in_button_energy)
    energy.grid(row=6, column=5)

    # create states of pet which will change

    text_in_window_with_state_of_satiety = str(pet.satiety)
    state_of_satiety = Text(width=3, height=1)
    state_of_satiety.insert(1.0, text_in_window_with_state_of_satiety)
    state_of_satiety.grid(row=0, column=6)

    text_in_window_with_state_of_fun = str(pet.fun)
    state_of_fun = Text(width=3, height=1)
    state_of_fun.insert(1.0, text_in_window_with_state_of_fun)
    state_of_fun.grid(row=2, column=6)

    text_in_window_with_state_of_health = str(pet.health)
    state_of_health = Text(width=3, height=1)
    state_of_health.insert(1.0, text_in_window_with_state_of_health)
    state_of_health.grid(row=4, column=6)

    text_in_window_with_state_of_energy = str(pet.energy)
    state_of_energy = Text(width=3, height=1)
    state_of_energy.insert(1.0, text_in_window_with_state_of_energy)
    state_of_energy.grid(row=6, column=6)

    decline_in_satiety()
    decline_in_fun()
    decline_in_health()
    decline_in_energy()

    root.mainloop()


if __name__ == "__main__":
    main()
