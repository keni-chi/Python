# -*- coding: utf-8 -*-
"""import."""
import json


def func(x):
    """[summary].

    Args:
        x ([type]): [description]

    Returns:
        [type]: [description]

    """
    print(x)
    return x


def main():
    """main."""
    print('test')
    x = {'k': 'v'}
    y = json.dumps(x)
    z = func(y)
    print(z)


if __name__ == '__main__':
    """root."""
    main()
