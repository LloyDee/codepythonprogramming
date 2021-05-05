first_score = 85
second_score = 94
third_score = 90
fourth_score = 100
fifth_score = 100
average = (first_score + second_score + third_score + fourth_score + fifth_score) / 5

if average >= 90:
    print("Your average is {}. The Grade is A".format(average))
elif average >= 80:
    print("Your average is {}. The Grade is B".format(average))
elif average >= 70:
    print("Your average is {}. The Grade is C".format(average))
elif average >= 60:
    print("Your average is {}. The Grade is D".format(average))
else:
    print("{} average so you failed".format(average))
