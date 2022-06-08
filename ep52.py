### Arbitrary Arguments (kwargs)
# ** kwargs

########################################################################################################################
## *args => ค่าใน parameter มีได้หลายค่า
def add(*number):
    sum = 0
    for i in range(len(number)):
        sum+=number[i]
    print(sum)

add(10,5)
add(10,5,6)


## **kwargs ตั้งชื่อได้แบบไม่จำกัด
def displayData(**kwargs):
    print(kwargs)

displayData(fname="John Tik",lname="Jutajan",age=35,city="bangkok",status="โสด")


########################################################################################################################