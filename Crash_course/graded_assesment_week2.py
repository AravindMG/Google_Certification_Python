from tokenize import String


def format_name(first_name, last_name):
    # code goes here
    if first_name != "" and last_name != "":
        string =  ("Name: " + last_name + ", "+ first_name)
    elif first_name == "":
        string = ("Name: " + last_name)
    elif last_name == "":
        string = ("Name: " + first_name)
    else:
        string = ""

    return string


def sum(x, y):
    return x + y


if __name__ == '__main__':
    print(format_name("Ernest", "Hemingway"))
    # Should be "Name: Hemingway, Ernest"

    print(format_name("", "Madonna"))
    # Should be "Name: Madonna"

    print(format_name("Voltaire", ""))
    # Should be "Name: Voltaire"

    print(format_name("", ""))
    # Should be ""

    print(sum(sum(1, 2), sum(3, 4)))

    print(((10 >= 5*2) and (10 <= 5*2)))
