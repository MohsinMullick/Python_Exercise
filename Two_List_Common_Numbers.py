"""
two list common value
"""
from os.path import commonpath

list1=[1,2,3,4,5,6,7,8,9]
list2=[66,76,8,9,11,2]
common_value=list(set(list1) & set(list2))
print(f"after add elements common value: {common_value}")