### ฟังก์ชันแบบคืนค่า

########################################################################################################################
##
'''
1. แบบไม่มีการรับและส่งค่า
def name():

2. มีการรับค่าเข้าไปทำงาน
def name(a,b):
    statement

3. แบบรับค่าเข้าไปทำงาน และส่งออกมา
def name(a,b):
    return

4. ไม่มีการรับค่าเข้ามา แต่ส่งค่าออกไป

'''

def add(a,b):
    return a+b # ให้มันส่งค่าคืนกลับออกมา => คืนค่า function

add(10,20)
print("add => ",add(10,20))

y = add(50,60) # เก็บไปที่ตัวแปร
print("add => ",y)

def shownumber():
    return 500

z = shownumber()
print("number => ",z)

print("End")
########################################################################################################################


########################################################################################################################
def randomNumber(x):
    if x == '168':
        print("ถูกหวย")
        return 1000
    else:
        print("ไม่ถูกหวย")
        return 0

money = randomNumber("168")
print("เงินรางวัล => ",money)

dept = 300
result = money - dept

print("ใช้หนี้แล้ว เงินเหลือทั้งหมด => ",result)

########################################################################################################################
