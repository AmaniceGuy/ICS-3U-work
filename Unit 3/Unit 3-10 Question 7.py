def main():
    num = 9
    print(sumAll(num))

def sumAll(num):
    if num == 0:
        return num
    else:
        return num + sumAll(num - 1)
    
main()