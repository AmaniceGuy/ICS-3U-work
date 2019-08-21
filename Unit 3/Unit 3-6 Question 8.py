def double_preceeding(values):
    if (values != []):
        temp = values[0]
        values[0] = 0
        for i in range(1, len(values)):
            temp2 = values[i]
            values[i] = 2 * temp
            temp = temp2

def main():
    values = [1,3,7,11]
    double_preceeding(values)
    print(values)

main()