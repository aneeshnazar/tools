#!/usr/bin/env python3

def fibonacci(arg):
    a = [0, 1, 1];
    i = 2;
    if (arg <= i):
        return (a[arg]);
    while (i < arg):
        a[0] = a[1]
        a[1] = a[2]
        a[2] = a[1] + a[0]
        i += 1;
    return (a[2])

def main():
    for i in range(200):
        print (fibonacci(i));

if __name__ == '__main__':
    main()
