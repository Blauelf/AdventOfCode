#! /usr/bin/env python3

def main():
    with open('input.txt') as f:
        arr = list(map(str.strip, f))
    total = 0
    for rs in arr:
        num = len(rs) // 2
        first = set(rs[:num])
        second = set(rs[num:])
        item = list(first & second)[0]
        total += (ord(item) - 96 if "a" <= item <= "z" else ord(item) - 38)
    print(total)


if __name__ == '__main__':
    main()
