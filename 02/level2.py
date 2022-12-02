#! /usr/bin/env python3

def main():
    with open('input.txt') as f:
        arr = [l.split() for l in f]
    matrix = [[3, 4, 8], [1, 5, 9], [2, 6, 7]]
    print(sum(matrix[ord(i)-65][ord(j)-88] for (i,j) in arr))


if __name__ == '__main__':
    main()

