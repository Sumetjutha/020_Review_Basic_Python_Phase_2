### Function

########################################################################################################################
### การสร้างและเรียก ฟังก์ชัน

'''
def ชื่อฟังก์ชัน ():
    statment
'''

# สร้าง Function
from re import X


def sayHi():
    print("Hello JohnTik")

def sayThailand():
    print("สวัสดี")

def sayEngland():
    print("Hello / Hi")

# เรียก Function
sayThailand()
sayEngland()

# สร้าง function สำหรับหาผลบวก
def add():
    x = 3+1
    print(x)

add()
sayThailand()


# ใช้ร่วมกับ loop ก็ได้
for i in range(2):
    add()
########################################################################################################################