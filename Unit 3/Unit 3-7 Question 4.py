nums = []
for item in range(5):
    while True:
        x = int(input("New number: "))
        if x in nums:
            print("Already in list")
            continue
        else:
            nums += [x]
            break
print (nums)