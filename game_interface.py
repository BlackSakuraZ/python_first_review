from tkinter import Button, Canvas, Entry, END, HIDDEN, IntVar
from tkinter import Label, Radiobutton, Text, Tk, W
from tkinter.messagebox import showinfo
from tkinter.messagebox import askquestion
from pet import Pet


class Game:

    pet = Pet()

    def show_information(self):
        information = str("""Welcome to the tamagochi! Here you can create your own pet.
        At the beginning you should choose your pet's color and name and click save.
        Congratulations, your pet is created! It has four states: health, fun, satiety and energy.
        To increase first three of them you should click on buttons heal, play and feed respectively.
        To increase energy put your pet to sleep.
        Attention! If one of the states will be 0, your pet will die, you will be able to restart game.
        Good luck!""")
        showinfo("Guide", information)
        self.choose_settings()
        self.create_main_window()

    def choose_settings(self):
        def ok():
            showinfo("Information", "saved successfully")
            if value_of_button.get() == 1:
                self.pet.color = "tomato"
            if value_of_button.get() == 2:
                self.pet.color = "gold"
            if value_of_button.get() == 3:
                self.pet.color = "sky blue"
            if value_of_button.get() == 4:
                self.pet.color = "SeaGreen1"
            if value_of_button.get() == 5:
                self.pet.color = "magenta"
            settings_window.destroy()

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
        self.pet.name = text_from_pet_name.get()
        text_from_pet_name.grid(row=6, column=1)
        save_button = Button(text="save", font=("Ubuntu", 10), command=ok)
        save_button.grid(row=7, columnspan=2)
        settings_window.mainloop()

    def restart(self):
        showinfo("Information", "Your pet is dead")
        answer = askquestion("Restart", "Do you want to try again?")
        if answer == "yes":
            self.root.destroy()
            self.pet.fun = 101
            self.pet.satiety = 101
            self.pet.health = 101
            self.pet.energy = 101
            self.choose_settings()
        else:
            self.root.destroy()

    def sleep(self):
        self.pet.energy = 100
        new_state_of_energy = str(self.pet.energy)
        self.state_of_energy.delete(1.0, END)
        self.state_of_energy.insert(1.0, new_state_of_energy)
        new_color = self.canvas.body_color
        self.canvas.itemconfigure(self.pupil_left, fill=new_color, outline=new_color)
        self.canvas.itemconfigure(self.pupil_right, fill=new_color, outline=new_color)
        self.canvas.itemconfigure(self.eye_left, fill=new_color)
        self.canvas.itemconfigure(self.eye_right, fill=new_color)

    def wake_up(self):
        new_color = 'white'
        self.canvas.itemconfigure(self.pupil_left, fill="black", outline="black")
        self.canvas.itemconfigure(self.pupil_right, fill="black", outline="black")
        self.canvas.itemconfigure(self.eye_left, fill=new_color)
        self.canvas.itemconfigure(self.eye_right, fill=new_color)

    def pet_decline_in_satiety(self):
        self.pet.decline_in_satiety()
        if self.pet.satiety <= 0:
            self.restart()
        new_state_of_satiety = str(self.pet.satiety)
        self.state_of_satiety.delete(1.0, END)
        self.state_of_satiety.insert(1.0, new_state_of_satiety)
        self.root.after(4000, self.pet_decline_in_satiety)

    def pet_decline_in_fun(self):
        self.pet.decline_in_fun()
        if self.pet.fun <= 0:
            self.restart()
        new_state_of_fun = str(self.pet.fun)
        self.state_of_fun.delete(1.0, END)
        self.state_of_fun.insert(1.0, new_state_of_fun)
        self.root.after(3000, self.pet_decline_in_fun)

    def pet_decline_in_health(self):
        self.pet.decline_in_health()
        if self.pet.health <= 0:
            self.restart()
        new_state_of_health = str(self.pet.health)
        self.state_of_health.delete(1.0, END)
        self.state_of_health.insert(1.0, new_state_of_health)
        self.root.after(5000, self.pet_decline_in_health)

    def pet_decline_in_energy(self):
        self.pet.decline_in_energy()
        if self.pet.energy <= 0:
            self.restart()
        new_state_of_fun = str(self.pet.fun)
        self.state_of_fun.delete(1.0, END)
        self.state_of_fun.insert(1.0, new_state_of_fun)

        new_state_of_energy = str(self.pet.energy)
        self.state_of_energy.delete(1.0, END)
        self.state_of_energy.insert(1.0, new_state_of_energy)
        self.root.after(10000, self.pet_decline_in_energy)

    def pet_increase_health(self):
        self.pet.increase_health()
        new_state_of_health = str(self.pet.health)
        self.state_of_health.delete(1.0, END)
        self.state_of_health.insert(1.0, new_state_of_health)

    def pet_increase_fun(self):
        if self.pet.energy * self.pet.satiety * self.pet.health <= 0:
            self.restart()
        self.pet.increase_fun()

        new_state_of_energy = str(self.pet.energy)
        self.state_of_energy.delete(1.0, END)
        self.state_of_energy.insert(1.0, new_state_of_energy)

        new_state_of_health = str(self.pet.health)
        self.state_of_health.delete(1.0, END)
        self.state_of_health.insert(1.0, new_state_of_health)

        new_state_of_satiety = str(self.pet.satiety)
        self.state_of_satiety.delete(1.0, END)
        self.state_of_satiety.insert(1.0, new_state_of_satiety)

        new_state_of_fun = str(self.pet.fun)
        self.state_of_fun.delete(1.0, END)
        self.state_of_fun.insert(1.0, new_state_of_fun)

    def pet_increase_satiety(self):
        self.pet.increase_satiety()
        new_state_of_energy = str(self.pet.energy)
        self.state_of_energy.delete(1.0, END)
        self.state_of_energy.insert(1.0, new_state_of_energy)

        new_state_of_satiety = str(self.pet.satiety)
        self.state_of_satiety.delete(1.0, END)
        self.state_of_satiety.insert(1.0, new_state_of_satiety)

    def create_main_window(self):
        self.root = Tk()
        self.root.title(self.pet.name)
        self.canvas = Canvas(self.root, width=400, height=400)
        self.create_buttons()
        self.create_text_in_buttons()
        self.create_states()
        self.pet_decline_in_satiety()
        self.pet_decline_in_energy()
        self.pet_decline_in_health()
        self.pet_decline_in_fun()
        # creating pet
        self.canvas.body_color = self.pet.color
        self.body = self.canvas.create_oval(35, 20, 365, 350, fill=self.canvas.body_color)
        self.ear_left = self.canvas.create_polygon(75, 80, 75, 10, 165, 70, fill=self.canvas.body_color)
        self.ear_right = self.canvas.create_polygon(255, 45, 325, 10, 325, 77, fill=self.canvas.body_color)
        self.mouth_normal = self.canvas.create_line(170, 250, 200, 272, 230, 250, width=2, smooth=1)
        self.foot_left = self.canvas.create_oval(65, 320, 145, 360, fill=self.canvas.body_color)
        self.foot_right = self.canvas.create_oval(250, 320, 330, 360, fill=self.canvas.body_color)
        self.eye_left = self.canvas.create_oval(130, 110, 160, 170, fill="white")
        self.eye_right = self.canvas.create_oval(230, 110, 260, 170, fill="white")
        self.pupil_left = self.canvas.create_oval(140, 130, 150, 155, fill="black")
        self.pupil_right = self.canvas.create_oval(240, 130, 250, 155, fill="black")
        self.cheek_left = self.canvas.create_oval(70, 180, 120, 230, fill='pink', state=HIDDEN)
        self.cheek_right = self.canvas.create_oval(280, 180, 330, 230, fill='pink', state=HIDDEN)
        self.mouth_happy = self.canvas.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)

        self.canvas.grid(rowspan=17, columnspan=4)

        self.root.mainloop()

    def create_buttons(self):
        self.feed = Button(text="FEED", width=10, height=2, command=self.pet_increase_satiety)
        self.feed.grid(row=9, column=0, sticky=W)

        self.play = Button(text="PLAY", width=10, height=2, command=self.pet_increase_fun)
        self.play.grid(row=11, column=0, sticky=W)

        self.heal = Button(text="HEAL", width=10, height=2, command=self.pet_increase_health)
        self.heal.grid(row=13, column=0, sticky=W)

        self.put = Button(text="PUT TO SLEEP", width=10, height=2, command=self.sleep)
        self.put.grid(row=15, column=0, sticky=W)

        self.wake = Button(text="WAKE UP", width=10, height=2, command=self.wake_up)
        self.wake.grid(row=17, column=0, sticky=W)

    def create_text_in_buttons(self):
        self.text_in_button_satiety = "SATIETY"
        self.satiety = Text(width=8, height=1)
        self.satiety.insert(1.0, self.text_in_button_satiety)
        self.satiety.grid(row=0, column=0)

        self.text_in_button_fun = "FUN"
        self.fun = Text(width=8, height=1)
        self.fun.insert(1.0, self.text_in_button_fun)
        self.fun.grid(row=2, column=0)

        self.text_in_button_health = "HEALTH"
        self.health = Text(width=8, height=1)
        self.health.insert(1.0, self.text_in_button_health)
        self.health.grid(row=4, column=0)

        self.text_in_button_energy = "ENERGY"
        self.energy = Text(width=8, height=1)
        self.energy.insert(1.0, self.text_in_button_energy)
        self.energy.grid(row=6, column=0)

    def create_states(self):
        self.text_in_window_with_state_of_satiety = str(self.pet.satiety)
        self.state_of_satiety = Text(width=3, height=1)
        self.state_of_satiety.insert(1.0, self.text_in_window_with_state_of_satiety)
        self.state_of_satiety.grid(row=0, column=1, sticky=W)

        self.text_in_window_with_state_of_fun = str(self.pet.fun)
        self.state_of_fun = Text(width=3, height=1)
        self.state_of_fun.insert(1.0, self.text_in_window_with_state_of_fun)
        self.state_of_fun.grid(row=2, column=1, sticky=W)

        self.text_in_window_with_state_of_health = str(self.pet.health)
        self.state_of_health = Text(width=3, height=1)
        self.state_of_health.insert(1.0, self.text_in_window_with_state_of_health)
        self.state_of_health.grid(row=4, column=1, sticky=W)

        self.text_in_window_with_state_of_energy = str(self.pet.energy)
        self.state_of_energy = Text(width=3, height=1)
        self.state_of_energy.insert(1.0, self.text_in_window_with_state_of_energy)
        self.state_of_energy.grid(row=6, column=1, sticky=W)
