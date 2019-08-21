def main():
    m, n = 12, 32
    print(gcd(m,n))

def gcd(m,n):
    if n == 0:
        return m
    elif n > 0 :
        return gcd(n, m % n)

main()