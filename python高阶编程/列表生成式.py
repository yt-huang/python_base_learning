def Test1(time):
    a,b = 1,1
    n = 3
    while n <=time:
        yield b #返回给生成器的返回值
        a,b = b,a+b
        n += 1

if __name__ == '__main__':
    a = Test1(6)
    # print(next(a))
    # print(next(a))
    # print(next(a))
    # print(next(a))
    # print(a.__next__())
    # print(a.__next__())
    # print(a.__next__())
    # print(a.__next__())
    print(a.send(None))
    print(a.send(""))
    print(a.send(""))
    print(a.send(""))