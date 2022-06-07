### Assignment 2

########################################################################################################################
def addtition(a,b,z):
    print("ผลของ addition => ",a+b+z)

addtition(10,20,50)

def sumThree(x,y,z):
    print("ผลบวก sumThree => ",x+y+z)

sumThree(10,20,60)


# *agrs
# ส่ง parameter ได้หลายตัว
# จะเป็นตัว tuple

def add(*agrs):
    print(agrs[0]+agrs[1])

add(10,20)

## ใช้ loop for
def add_A(*agrs):
    sum=0
    for item in agrs:
        sum+=item
    print("ผลของ sum A => ",sum)

add_A(10,20,30,40,50)

## ใช้ loop for ร่วมกับ range(len())
def add_B(*agrs):
    sum=0
    for item in range(len(agrs)):
        sum+=agrs[item]
    print("ผลของ sum B => ",sum)

add_B(10,20,30,40,50,70,80,999,1999)


def add_C(*number):
    sum=0
    for item in range(len(number)):
        sum+=number[item]
    print("ผลของ sum C => ",sum)

add_C(10,20,30,40,50,70,80,999,1999,299999)

########################################################################################################################