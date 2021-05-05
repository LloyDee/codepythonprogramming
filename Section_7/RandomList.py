


n=int(input('Please enter a positive integer between 1 and 15: '))
for row in range(1,n+1):
    print(*("{:5}".format(row*col) for col in range(1, n+1)))


