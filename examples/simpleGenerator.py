# simple_generator.py
#
# Very basic example
import sys, time


def simple_gen(collection):
    for num in collection:
        double = num * 2
        yield num










# Example use


if __name__ == '__main__':

    result = simple_gen([1,2,3,4,5])
    for item in result:
        print item
        time.sleep(.3)