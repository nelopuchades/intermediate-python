# {key:value for value in iterable if condition}

def run():
    # Exercise 1
    # cubo = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    # print(cubo)

    naturales = {i: i**(0.5) for i in range(1, 1001)}
    print(naturales)


if __name__ == '__main__':
    run()
