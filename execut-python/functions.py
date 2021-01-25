def positional(x, y):
    """ the argument x and y is positional arguments
    in the function the first value you pass in will be alwayes assing to x and the second value will be assigned to the y
    """
    return x + y


print(positional(5, 3))


def defAgr(name, age=18):
    """ Here age is default argument if we dont pass any value to age then it will assigend to value 18 """
    print('hello {} you are {} years old'.format(name, age))


defAgr('Kanon', 32)


def keyArg(a, b):
    resul = a/b
    print(resul)


""" Here we are setting the arguments value by assinging it's keyword values """
keyArg(b=1, a=2)


def limit_arg(*args):
    """
        *args allow a function to take any number of positional arguments.
    *args is used for sending the non-keyworded argument """
    i = 0
    for argument in args:
        i += 1
        print('Argument {} is {}'.format(i, argument))


limit_arg('Kanon', 1, 2, ['k', 'r'],)


def keword_argument(**kwargs):
    """ **kwargs allow a function to take any number of keyword arguments. """
    for key, value in kwargs.items():
        print('Key is :{}  and value is : {}'.format(key, value))


keword_argument(name='kanon', age=32, profession='Web Developer')


# A function will call another function with it's arguments and value

# as example -h is for Host url = example.com

def callme(h, r=''):
    print(h, '\n')
    print('\n', r)


ar = {'h': 'example.com'}

callme(**ar)


# Lambda Functions
