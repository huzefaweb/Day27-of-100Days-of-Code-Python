# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# print(add(3, 4, 5, 6))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():  # The items() method returns a view object.The view object contains the key-value
    #     # pairs of the dictionary, as tuples in a list.
    #     print(key)
    #     print(value)
    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")  # get() works same as square brackets but the benefit is
        # if the one of argument is missing it will not crash else if square brackets is used it would crash
        # if one argument is given but not the other

my_car = Car(make="Nissan", model="GTR-4")