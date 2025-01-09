"""Modify a List of Numbers:
Create a list of numbers from 1 to 5. Change the second number in the list to 10 and print the updated list.
"""
numbers= [1,2,3,4,5]#declears list variables
print(numbers)#print functions
numbers[1]=10#modify second index
print(numbers)


"""we have a list of motorcycles(honda,yamaha,suzuki) and the first item in the
list is 'honda'. We can change the value of this first item after the list has
been 'ducati':"""
motorcycles=['honda','yamaha','suzuki'] #declears list variables
print(motorcycles)#print function
motorcycles[0]='ducati'#modify new value for first index or adding
print(motorcycles)#print function


#appending list
motorcycles=['honda','yamaha','suzuki']#declears  list variables and values
print(motorcycles)#print function
motorcycles.append('ducati')#appending new values
print(motorcycles)#print function



motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
