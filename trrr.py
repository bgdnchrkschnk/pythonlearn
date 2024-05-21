x = 0


def outer():
    x = 1

    def inner():
        global x
        # x = 2
        print(x)
    inner()
outer()
