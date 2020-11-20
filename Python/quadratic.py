
import math # imports math
def num(val1, val2, val3):# sets up the discriminant
    return (float((val2*val2) - (4 * val1 * val3)))

def ans1(val1, val2, num): # first root
    return(float((val2*-1)+math.sqrt(num))/(2*val1))

def ans2(val1, val2, num): #second root
    return(float((val2*-1)-math.sqrt(num))/(2*val1))

ans = [] # beginning of the array

print("quadratic solver")
print("Ax^2 + Bx + C")
a = float(input("Enter a: ")) 
b = float(input("Enter b: ")) 
c = float(input("Enter c: ")) 

if (float((b*b) - (4 * a * c)) < 0): #if statement that makes sure the roots are real
    print("This equation has no real roots.")
    
else:

    ans.append(ans1(a,b,num(a,b,c)))# appends the answers to the array
    ans.append(ans2(a,b,num(a,b,c)))
print(ans) #prints the array
