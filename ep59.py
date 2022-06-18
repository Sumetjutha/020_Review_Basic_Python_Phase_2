### Anomynous Function

########################################################################################################################
## lambda function
## สร้างขึ้นมาโดยไ่ม่อยากระบุชื่อ แต่ทำอย่้างอื่นได้ปกติ

def getCity(name):
    print("Hello",name)

getCity("Intamara")

'''
lambda arguments : expression
'''

x = lambda name : name
x = "John"
print(x)

sum = lambda x,y : x+y
print(sum(5,10))

multiply = lambda a,b : a*b
result = multiply(5,10)
print(result)

def myPower(x):
    return x*x

y = myPower(5)
print(y)

########################################################################################################################

########################################################################################################################
## เขียน lambda function ซ้อนใน function
def myPower_2(x):
    return lambda a : x**a

z = myPower_2(10)
result = z(2) # 5 ** 2
print(result)

########################################################################################################################
