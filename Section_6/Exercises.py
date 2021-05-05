def lesser_of_two(n1, n2):
    if n1 % 2 == 0 and n2 % 2 == 0:
        return min(n1, n2)
    else:
        return max(n1, n2)


print(lesser_of_two(2, 4))
print(lesser_of_two(2, 5))
print('**********************************************\n')


def same_letter(string):
    x = string.lower().split()

    return x[0][0] == x[1][0]


print(same_letter('Levelheaded Llama'))
print(same_letter('Crazy cat'))
print('**********************************************\n')


def other_side_of_seven(number):
    result = 0
    if number < 7 or number >= 7:
        result = (7 - number) * 2 + 7
    return result


print(other_side_of_seven(4))
print(other_side_of_seven(12))
print('**********************************************\n')


def reverse(string):
    x = string.split()

    return " ".join(x[::-1])


print(reverse("I am home"))
print(reverse("We are ready"))

print('**********************************************\n')


def makes_twenty(a, b):
    return a == 20 or b == 20 or (a + b == 20)


print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))
print('**********************************************\n')


def capitalized(name):
    f_half = name[:3]
    s_half = name[3:]
    return f_half.capitalize() + s_half.capitalize()


print(capitalized('macdonald'))

print('**********************************************\n')


def find_three(my_list):
    for i in range(0, len(my_list) - 1):
        if my_list[i] == 3 and my_list[i + 1] == 3:
            return True

    return False


print(find_three([1, 2, 3, 3, 6]))

print('**********************************************\n')


def paper_doll(string):
    result = []
    for i in range(0, len(string)):
        result.append(string[i] * 3)
    return "".join(result)


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

print('**********************************************\n')


def black_jac(a, b, c):
    if (a and b and c >= 1) and (a and b and c <= 11):
        if sum([a, b, c]) <= 21:
            return sum([a, b, c])
        elif sum([a, b, c]) > 21 and 11 in [a, b, c]:
            return sum([a, b, c]) - 10
        else:
            return "BUST"
    else:
        return "Must be between 1-11"


print(black_jac(5, 6, 1))
print(black_jac(1, 26, 1))
print(black_jac(9, 9, 1))
print('**********************************************\n')


def spy_007(*args):
    spy = []
    for i in range(0, len(args)):
        if args[i] == 0 or args[i] == 7:
            spy.append(args[i])
    if spy == [0, 0, 7]:
        return True
    else:
        return False


print(spy_007(1, 2, 4, 0, 0, 7, 5))
print(spy_007(1, 0, 2, 4, 0, 5, 7))
print(spy_007(1, 7, 2, 0, 4, 5, 0))
print('**********************************************\n')


def prime_numbers(number):
    prime = []

    if number < 2:
        return 0
    x = 3
    for x in range(number):
        if x % 2 ==0 or x % 3 ==0:
            prime.append(x)
    return prime
print(prime_numbers(5))
