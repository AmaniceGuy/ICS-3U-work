def main():
    x,y = 3,4
    print(multiple(x,y))
       
def multiple(x,y):
    if y > 1:
        x += multiple(x,y-1)
        return x
    else:
        return x

main()