def foo(k, l):
    if k == len(l):
        print(l)
    for i in range(k, len(l)):
        l[0], l[i] = l[i], l[0]
        foo(k+1, l)
        l[0], l[i] = l[i], l[0]

def square(n):
    print(n & 0xF)

if __name__ == '__main__':
    square(10)
