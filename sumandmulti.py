num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))
def add(num1,num2):
    return num1+num2
def mul(result1,num3):
    return result1*num3
   

result1 = add(num1,num2)
result2 = mul(result1,num3)
print(result2)