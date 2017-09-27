# Introduction of function within a function
def outer(a):
    def inner():
        x = a + 1
        return x
    return inner()

# a simple example if not using functional programming
def all_even(alist):
    result = []
    for item in alist:
        if item % 2 ==0:
            result.append(item)
    return result

def all_odd(alist):
    result = []
    for item in alist:
        if item % 2 ==1:
            result.append(item)
    return result


# first iteration of simplifying
def is_even(numb):
    return numb % 2 == 0

def is_odd(numb):
    return numb % 2 == 1

# second iteration of simplifying
def myfilter(alist, func):
    result = []
    for item in alist:
        if func(item):
            result.append(item)
    return result

if __name__ == "__main__":
    print(outer(1))
    print(all_even(range(1,101)))
    print(all_odd(range(1, 101)))

    # first iteration of simplifying
    print(myfilter(range(1, 101), is_even))
    print(myfilter(range(1, 101), is_odd))

    # second iteration of simplifying
    print(myfilter(range(1, 101), lambda x: x % 2 == 0))
    print(myfilter(range(1, 101), lambda x: x % 2 == 1))
