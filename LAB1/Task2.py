def list_check(list):
    base = list[0]
    for item in list:
        if(item < base):
            return False
        base = item
    return True
list1 = (1, 2, 8, 9 ,10)
print(list_check(list1))
