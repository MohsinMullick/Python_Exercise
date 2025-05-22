list1=[1,2,3,4,5,6,7,8,9]
list2=[6,7,8,9,11,2]
common_value=list(set(list1) ^ set(list2))
print(f"after add elements unique value: {common_value}")