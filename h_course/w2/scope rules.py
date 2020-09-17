def update():
    x.append(1)

x = [1,1]
update()
print(x)

def update(n,x):
    n = 2
    x.append(4)
    print('update: ', n, x)

def main():
    n = 1
    x = [0,1,2,3]
    print('main: ', n, x)
    update(n,x)
    print('main: ', n, x)

main()

def increment(n):
    n += 1
    print(n)

n = 1
increment(n)
print(n)


def increment(n):
    n += 1
    return n+8
n = 1

while n < 10:
    n = increment(n)
print(n)