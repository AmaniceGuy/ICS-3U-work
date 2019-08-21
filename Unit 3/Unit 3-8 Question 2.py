studMark = {}
for x in range(5):
    name = input("Student's name: ")
    if studMark.get(name,False) != False:
        print("Please input a new name")
        continue
    mark = int(input("Mark(out of 100): "))
    studMark[name] = mark
    