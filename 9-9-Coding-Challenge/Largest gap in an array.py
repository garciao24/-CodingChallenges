
def solve(a):
     
    min1 = a[0]
    max1 = a[0]
    size = len(a)
  
    # finding maximum and minimum of an array
    for i in range (size):
     
        if (a[i] > max1):
            max1 = a[i]
        if (a[i] < min1):
            min1 = a[i]
     
    # print(max1)
    # print(min1)
    return abs(min1 - max1)
 


arr = [ -1, 2, 3, 4, -10 ]
print("Largest gap is : " ,solve(arr))