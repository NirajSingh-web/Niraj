# print 1 to 10 number
def print1_to_10(start,end):
    if (start<=end):
        print(start)
        start+=1
        print1_to_10(start,end)
print1_to_10(1,10)

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(6))