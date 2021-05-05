from datetime import date

year = date.today().year


def display(a, b):
    year_ = 30
    get_year = year + year_
    x = 'Hi {}, you are {} years old. You turn {} in {}'.format(a, b, int(b) + year_, get_year)
    print(x)
    return x


def get_bio():
    name = input('What is your name?\n')
    age = input('How old are you?\n')
    return display(name, age)


def write_this():
    with open('C:\\Users\\loyd_\\Desktop\\Address.txt', 'w+') as myF:
        myF.write("Juliet Poquiz Dalley\n"
                  "4927 Celtic Cor\n"
                  "San Antonio, Tx 78244")


write_this()
