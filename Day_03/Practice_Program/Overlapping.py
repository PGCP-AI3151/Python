
def overlapping(l1, l2):
    return bool(set(l1) & set(l2))

if __name__ == '__main__':
    list1 = [1,2,3,4,5,6]
    list2 = [7,8,9,0,1]
    print("Overlapping :- ",overlapping(list1,list2))