class StatesOfPet:
    name = ""
    color = ""
    fun = 101
    satiety = 101
    health = 101
    energy = 101

    def decline_in_satiety(self):
        self.satiety -= 1

    def decline_in_fun(self):
        self.fun -= 1

    def decline_in_health(self):
        self.health -= 1

    def decline_in_energy(self):
        if self.energy <= 30:
            self.fun -= 2
        self.energy -= 1

    def increase_health(self):
        self.health = min(100, self.health + 5)

    def increase_fun(self):
        self.energy -= 3
        self.health -= 3
        self.satiety -= 2
        self.fun = min(100, self.fun + 5)

    def increase_satiety(self):
        self.energy = min(100, self.energy + 2)
        self.satiety = min(100, self.satiety + 5)
        self.health = min(100, self.health + 1)
