"""
find list second max value
"""
numbers=[1,2,3,4,5,6,78,43,45]
sorted_numbers=sorted(set(numbers),reverse=True)
second_largest_numbers=sorted_numbers[1]
print(f"Second Largest Numbers: {second_largest_numbers}")