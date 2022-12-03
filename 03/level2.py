#! /usr/bin/env python3

def main():
    with open('input.txt') as f:
        arr = list(map(str.strip, f))
    total = 0
    for rs1, rs2, rs3 in zip(arr[::3], arr[1::3], arr[2::3]):
        item = list(set(rs1) & set(rs2) & set(rs3))[0]
        total += (ord(item) - 96 if "a" <= item <= "z" else ord(item) - 38)
    print(total)


if __name__ == '__main__':
    main()
