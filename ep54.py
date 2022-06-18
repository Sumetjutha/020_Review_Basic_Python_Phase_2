###  ฟังก์ชัน เรียก ฟังก์ชัน

########################################################################################################################
## สร้าง ฟังก์ชันเพื่อเปรียบเทียบตัวเลข
def compareMax(x,y):
    if x>y:
        return x
    else:
        return y

# max = compareMax(10,5)
max = compareMax(10,20)
print("ค่ามากสุด => ",max)

# def equal(x,y,z):
#     # เปรียบเทียบ x กับ y ก่อน
#     a = compareMax(x,y)
#     # เปรียบเทียบกับ z
#     m = compareMax(a,z)
#     return m

# เขียนแบบนี้ function ซ้อน function ได้มากกว่า
def equal(x,y,z):
    return compareMax(compareMax(x,y),z)

max = equal(10,20,30)
print("ค่ามากสุด => ",max)

max = equal(3,6,-5)
print("ค่ามากสุด => ",max)

########################################################################################################################

def displayFood():
    print("หูฉลาม")

def displayCity():
    displayFood()
    print("สวัสดีกรุงเทพ")

displayCity()

