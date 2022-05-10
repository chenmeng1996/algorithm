def my_bin(n):
    def gen(x):
        y = abs(x)
        while y > 0:
            yield y % 2
            y = y >> 1
        else:
            if x == 0:
                yield 0
    l = [i for i in gen(n)]
    l.reverse()
    return "".join([str(v) for v in l])

if __name__ == "__main__":
    b = bin(10)
    print(b[2:])

    b = my_bin(10)
    print(b)