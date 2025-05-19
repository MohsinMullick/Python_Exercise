"""
Dictionary merge
"""
dict1={"name ":"Mohsin","Age":23}
dict2={"department":"CSE","Semester":7}
merged_dep={**dict1,**dict2}
print(f"After merged: {merged_dep}")
