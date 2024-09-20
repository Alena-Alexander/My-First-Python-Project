"""This is the My Functions Module.
This docstring explains the purpose of `my_functions` module, located in the `src` package.
"""


def some_function():
    """A function is a set of instructions to complete some objective or task.
    This is a function level docstring.
    """
    pass


class SomeClass:
    """A blueprint of a real life thing.

    Usage:
    =====

    >>> realThing = SomeClass()  # an instance of the class is essentially invoking the class to create a real object from the blueprint of the class.
    >>> realThing.some_method()  # calling the `some_method` function to do some task
    """

    def some_method(self): ...
    """A method is a function of a class.
    This is a method level docstring.
    """


def greet(name, city=None):
    if city:
        sentence = f"Hello {name} how is life in the {city}"
    else:
        sentence = f"Hello {name}"

    return sentence
