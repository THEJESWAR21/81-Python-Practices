list1 = [0,1,2,3,4,6,9,99]
list2 = [0,1,55,66,7,7,9]

commonitems = list(set(list1) & set(list2))
print(commonitems)