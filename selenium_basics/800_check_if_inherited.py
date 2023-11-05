def check_inheritance(obj, class_):
    # YOUR CODE HERE
    if type(obj) == class_:
        return isinstance(type(obj), class_)
    else:
        return isinstance(obj, class_)


if __name__ == "__main__":

    class Base:
        pass


    a = Base()
    b = [1, 2]
    c = False
    for x in [a, b, c]:

        if check_inheritance(x, int):
            print(f"{x} was inherited from {int.__name__}")
        if check_inheritance(x, list):
            print(f"{x} was inherited from {list.__name__}")
        if check_inheritance(x, Base):
            print(f"{x} was inherited from {Base.__name__}")
        if check_inheritance(x, object):
            print(f"{x} was inherited from {object.__name__}")