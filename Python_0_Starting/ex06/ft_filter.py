def ft_filter(function, iterable):
    """
        Built-in python 'filter' method rewritten
    """
    if function is None:
        return (item for item in iterable if bool(item))
    return (item for item in iterable if function(item))
