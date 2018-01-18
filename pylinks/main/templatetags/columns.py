from django import template

register = template.Library()

@register.filter
def columns(lst, cols):
    """
    Break a list into ``n`` lists, typically for use in columns.

    >>> lst = range(10)
    >>> for list in columns(lst, 3):
    ...     list
    [0, 1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
    """
    try:
        cols = int(cols)
        lst = list(lst)
    except (ValueError, TypeError):
        raise StopIteration()

    start = 0
    for i in range(cols):
        stop = start + len(lst[i::cols])
        yield lst[start:stop]
        start = stop
