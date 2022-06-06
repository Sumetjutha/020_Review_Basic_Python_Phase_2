### Function

########################################################################################################################
## การรับค่าเข้ามาในฟังก์ชั่น

# def myData(name):
#     print("Hello "+str(name))

def myData(name):
    print("Hello",name)

myData("JohnTik")
myData("Jojo")
myData(5)

print("END")

def myData_A(name,lname,age):
    print("ชื่อ => ",name,": นามสกุล =>",lname,": อายุ => ",age)

name="สุเมธ"
lname="จุฑาจันทร์"
age=35

myData_A(name,lname,age)

print("END")
########################################################################################################################