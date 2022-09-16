
import math
import re

def IsValidHexCode(str):
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', str)
    if match:                      
        return True
    else:
        return False


def NextPrime(N):
     
    if (N <= 1):
        return 2
 
    prime = N
    found = False

    while(not found):
        prime = prime + 1
 
        if(isPrime(prime) == True):
            found = True
 
    return prime


def isPrime(n):
    
    if(n <= 1):
        return False
    if(n <= 3):
        return True
     
    if(n % 2 == 0 or n % 3 == 0):
        return False
     
    for i in range(5,int(math.sqrt(n) + 1), 6):
        if(n % i == 0 or n % (i + 2) == 0):
            return False
     
    return True

print(IsValidHexCode("#CD5C5C"))
print(IsValidHexCode("#EAECEE"))
print(IsValidHexCode("#eaecee"))
print(IsValidHexCode("#CD5C58C"))
print(IsValidHexCode("#CD5C5Z"))
print(IsValidHexCode("#CD5C&C"))
print(IsValidHexCode("CD5C5C"))

print(NextPrime(12))
print(NextPrime(24))
print(NextPrime(11))