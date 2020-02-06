def implicit():
    print(7+8.5)


def explicit():
    add = 7 + 8
    change = str(add)
    print(type(change))


if __name__ == "__main__":
    implicit()
    explicit()