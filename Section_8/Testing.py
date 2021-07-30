name = (input("Your name\n"))
stress_level = int(input("How stress are you?\t1-10"))

if stress_level > 5:
    print("{} you need some sleep".format(name))
else:
    print("{} you're okay".format(name))
