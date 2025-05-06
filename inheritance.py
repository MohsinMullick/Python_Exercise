class Phone:
    def call(self):
        print('When You buy a phone then you can call')

    def message(self):
        print("When you buy a phone then you can send message")


class Pixel(Phone):
    def photo(self):
        print("Now you can take photo")


# Create objects
phone = Phone()  # Corrected: Added parentheses
pixel = Pixel()  # Create a Pixel object

# Test methods
phone.call()      # Output: You buy a phone then you can call
phone.message()   # Output: When you buy a phone then you can send message


pixel.photo()     # Output: Now you can take photo
pixel.call()      # Output: You buy a phone then you can call (inherited from Phone)
pixel.message()   # Output: When you buy a phone then you can send message (inherited)