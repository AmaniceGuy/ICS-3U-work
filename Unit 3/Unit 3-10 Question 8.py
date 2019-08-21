def main():
    num,exp = 3,4
    print(powe(num,exp))
    
def powe(num,exp):
    if exp > 1:
        power = num * powe(num,exp-1)
        return power
    else:
        return num
main()