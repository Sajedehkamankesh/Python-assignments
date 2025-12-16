import random
a = random.randint(1, 6)
count = 0
while True:
    b = int(input(" add hads bezan ! "))
    count += 1
    if b == a :
        print(" dorost bod! ")
        print(" tedad talash ha :  ",count)
        break
    else:
        print(" eshtebah dobare talash kon !")