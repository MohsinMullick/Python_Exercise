"""
Sequence values
"""
marks={"Mohsin":64,"Hasif":63,"Satu":98}
sorted_dict=dict(sorted(marks.items(),key=lambda item:item[1]))
print(f"sorted_dict:{sorted_dict}")
