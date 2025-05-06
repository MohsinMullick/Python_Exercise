class NSU:
    def __init__(self):
        print("I'm in campus")

class CSE(NSU):
    def __init__(self):
        super().__init__()
        print("Now I'm in CSE class")

# Create instance outside the class
cse = CSE()