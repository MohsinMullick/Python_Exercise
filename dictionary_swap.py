"""
dictionary swap
"""
student={"mohsin":66,"hasif":98,"satu":87,"mullick":78}
swapped_dic={value:key for key, value in student.items()}
print(f"after dictionary swap:{swapped_dic}")