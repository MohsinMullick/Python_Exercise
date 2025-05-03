"""If temperature is greater than 30
it's a hot day
Otherwise
if it's less than 10
It's a cold day
Otherwise
It's neither hot nor cold"""
temperature = float(input("Enter the temperature: "))

if temperature > 30:
    print("It's a hot day")
elif temperature < 10:
    print("It's a cold day")
else:
    print("It's neither hot nor cold")
