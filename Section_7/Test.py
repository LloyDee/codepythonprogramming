from RandomWordGenerator import RandomWord
import time, random

while True:
    rw = RandomWord(max_word_size=100)
    x = rw.generate().upper()
    print(x)
    time.sleep(0.3)
    if 'FD' in x:
        break
