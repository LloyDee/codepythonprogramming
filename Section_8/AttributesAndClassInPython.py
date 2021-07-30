class Heroes():

    classS = 'S'
    classA = 'A'
    classB = 'B'
    classC = 'C'

    heroes = ["1 - Blast", "2 - Tatsumaki", "3 - Silver Fang", "4 - Atomic Samurai", "5 - Child Emperor",
                   "6 - Metal Knight", "7 - King",
                   "8 - Zombieman", "9 - Drive Knight", "10 - Pig God", "11 - Superalloy Darkshine", "12 - Watchdog Man",
                   "13 - Flashy Flash",
                   "14 - Demon Cyborg", "15 - Metal Bat",
                                        "16 - Tanktop Master", "17 - Puri-Puri Prisoner"]

    def __init__(self, name, age, power, rank):
        self.name = name
        self.age = age

        self.power = power
        self.rank = rank

    def getinfo(self):
        print(
            "Name: {}\nAge: {}\nRank: {}\nPower: {}".format(self.name, self.age,  self.rank,
                                                                       self.power))

    # def list_of_heroes(self):
    #     heroes = ["1 - Blast", "2 - Tatsumaki", "3 - Silver Fang", "4 - Atomic Samurai", "5 - Child Emperor",
    #               "6 - Metal Knight", "7 - King",
    #               "8 - Zombieman", "9 - Drive Knight", "10 - Pig God", "11 - Superalloy Darkshine", "12 - Watchdog Man",
    #               "13 - Flashy Flash",
    #               "14 - Demon Cyborg", "15 - Metal Bat",
    #                                    "16 - Tanktop Master", "17 - Puri-Puri Prisoner"]
    #     for x in heroes:
    #         print(x)


