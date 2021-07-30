import AttributesAndClassInPython

hero = AttributesAndClassInPython.Heroes

blast = hero("Blast", 30, 1, "Dimensional Travel")
tatsumaki = hero(name="Tatsumaki ", age=23, rank=2, power="Psychokinesis")

vis = True


def sample():
    print(hero.heroes)


while vis:
    prompt = input("All Heroes\t- A\n"
                   "Pick a Hero\t- P\n"
                   "Quit\t- Q\n")
    if prompt.upper() == 'A':
        sample()
    elif prompt.upper() == 'P':
        sample()
        x = int(input("Select a Hero\n"))
        print(hero.heroes[x-1])
    else:
        vis = False
