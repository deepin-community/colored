#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Test foreground and background colors """

from colored.library import Library
from colored import fore, back, style


def main():

    # Prints foreground colors
    for name in Library.COLORS.keys():
        print(f"{fore(name)}{name:>3}{style('reset')}", end='  ')

    # Prints background colors
    for name in Library.COLORS.keys():
        print(f"{style(4, name)}{back(name)}{name:>3}{style('reset')}", end='  ')

    # Prints underline with colors
    for name in Library.COLORS.keys():
        print(f"{style(4, name)}{name:>3}{style(59)}", end='  ')


if __name__ == '__main__':
    main()
