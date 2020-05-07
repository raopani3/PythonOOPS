f = open("change.log", 'r')

f1 = open("abc.txt", 'w')

for data in f:
    f1.write(data)


fimage = open("baby.JPG", 'rb')
fwite = open("babycopy.JPG", 'wb')

for img in fimage:
    fwite.write(img)


