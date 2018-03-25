
def count():
    fs = []
    print(fs)
    for i in range(1,4):

        def f():
            return i*i
        fs.append(f)
        print(fs)
    return fs

ff = count()

for f in ff:
    # print(count())
    print(f())
print('-------------------------')

def main():
    return a

li = []
a = 1
m1 = main
li.append(m1)

for l in li:
    print(l())

a = 2
m2 = main
li.append(m2)

for l in li:
    print(l())

a = 3
m3 = main
li.append(m3)

for l in li:
    print(l())

print(li)