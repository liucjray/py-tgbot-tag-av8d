def get_caller(show=False):
    import inspect
    stack = inspect.stack()
    the_class = stack[1][0].f_locals["self"].__class__.__name__
    the_method = stack[1][0].f_code.co_name
    show and print("  I was called by {}.{}()".format(str(the_class), the_method))
    return the_class, the_method


def object_get(obj, dotted_key, default=None):
    import functools
    try:
        return functools.reduce(getattr, dotted_key.split('.'), obj)
    except AttributeError:
        return default


def dict_get(dictionary, dotted_key, default=None):
    import functools
    keys = dotted_key.split('.')
    try:
        return functools.reduce(lambda d, key: d.get(key) if d else default, keys, dictionary)
    except AttributeError:
        return default


def dd(msg):
    print(msg)
    exit()


def dump(msg):
    print(msg)


def lno():
    import inspect
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]
