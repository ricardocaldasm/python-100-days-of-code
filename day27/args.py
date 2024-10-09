def add(*args):  # tuple
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3))


def calculate(n, **kwargs):  # dictionary
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw) -> None:
        # self.make = kw["make"]
        # self.model = kw["model"] # this will crash if this key doesn't exist in the dict
        self.make = kw.get("make")
        self.model = kw.get("model")  # does not crash and returns None


my_car = Car(make="Nissan") # removed model = "GT-R"
print(my_car.model)
