#! /usr/bin/env python3

def main():
    with open('input.txt') as f:
        arr = f.read().split('\n\n')
    arr = [sum(map(int, s.strip().split('\n'))) for s in arr]
    arr.sort(reverse=True)
    print(sum(arr[:3]))


if __name__ == '__main__':
    main()

