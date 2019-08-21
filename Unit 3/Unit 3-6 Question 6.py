def double_it(list):
    for num in list:
        num *= 2
    return len(list)

def main():
    list = [1,2,224.5.5,5,5.,64.6,5.645,3,4,567,]
    print(list)
    print(double_it(list))
    print(list)

main()