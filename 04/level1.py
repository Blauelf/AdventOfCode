#! /usr/bin/env python3

import re


def main():
    with open('input.txt') as f:
        arr = [list(map(int, re.findall("\d+", assignment)))
               for assignment in f]
    total = sum(a[0] <= a[2] <= a[3] <= a[1] or
                a[2] <= a[0] <= a[1] <= a[3]
                for a in arr)
    print(total)


if __name__ == '__main__':
    main()
