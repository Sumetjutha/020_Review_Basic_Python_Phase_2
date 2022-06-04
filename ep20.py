### การเข้าถึงข้อมูล

##############################################################################
tup = (1,2,3,4,"JohnTik","มะม่วง",True,3.99) # tuple
print("tup => ",tup)
print(type(tup))

print("เข้าถึงสมาชิกตำแหน่งที่ 1 ถึง 3 => ",tup[0:3])
print("เข้าถึงสมาชิกตำแหน่งที่ 4 => ",tup[4])
print("เข้าถึงสมาชิกตำแหน่งที่ 5 => ",tup[-3])
print("เข้าถึงสมาชิกตำแหน่งที่ 2 ถึง 5 => ",tup[1:5])
print("เข้าถึงสมาชิกตำแหน่งที่ 1 ถึงสมาชิกตัวสุดท้าย => ",tup[1:])

## ค่าลบล่ะ
print("เข้าถึงสมาชิกตำแหน่งที่ตัวสุดท้าย => ",tup[-1])
print("เข้าถึงสมาชิกตำแหน่งที่คั้งแต่ช่วงก่อน -1 ไปถึง -3 => ",tup[-3:-1])
print("เข้าถึงสมาชิกตำแหน่งที่คั้งแต่ -4 ไปถึงสมาชิกตัวสุดท้าย => ",tup[-4:])
print("เข้าถึงสมาชิกตำแหน่งที่คั้งแต่สมาชิกตัวแรก แต่ไม่เอาตัวสุดท้าย => ",tup[:-1])

##############################################################################