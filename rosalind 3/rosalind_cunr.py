import math

def rosalind_cunr(n):
    return math.prod(range(2*n-5, 1, -2)) % 10**6

def main():
    n = 888
    count = rosalind_cunr(n)
    return count

if __name__ == '__main__':
    print(main())