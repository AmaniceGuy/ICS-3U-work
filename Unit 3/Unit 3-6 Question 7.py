def total(list):
    total = 0
    for index in range(len(list)):
        if str(list[index]) != list[index]:
            total += list[index]
    return total

def main():
    list = [1,2,"3,",4,"5", 6, "7", 8,"9"]
    print(list)
    print(total(list))
    
main()