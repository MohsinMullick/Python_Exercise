"""
function find the prime
"""
def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
        return True
    num =int(input("Entr some value: "))
    print(f"{num},prime number",is_prime())