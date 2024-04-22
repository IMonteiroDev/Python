#  Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
r = 1.1
Area = 3.8013271108436504

def area(num):
    return num*r

answer = input("Valor area:\n")
numb = float(answer)

print(round(area(numb), 2))
