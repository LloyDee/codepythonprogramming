from random import shuffle,randint
print("Range")

my_list = [1,2,3]
for num in range(1,11):
    print(num)

print("enumerate")
word = 'Lloyd'
for x,y in enumerate(word):
    print(x)

print("random")
ran_num = [1,2,3,4,5,6,7,8,9,10]
shuffle(ran_num)
print(ran_num)
ran_num.sort()
print(ran_num)

print(randint(0,5))

print('For input')