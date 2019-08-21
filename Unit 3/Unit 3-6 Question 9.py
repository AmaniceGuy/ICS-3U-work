"""James Wang
   Jan 17/2109
   Problem description:
"""
def remove_negs(num_list):
    for item in num_list:
        if item < 0:
            num_list.remove(item)
 
    return num_list

def main():
    num_list = [1,2,3,-3,6,-1,-3,1]
    print(num_list)
    print(remove_negs(num_list))
    
main()