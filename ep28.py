### Tuple

##############################################################################
### การ sort ข้อมูล
tup = (100,99,88,50,200,1,2,3,4,3.99,4) # tuple
print("tup => ",tup)

# เรียงจากน้อยไปมาก
# ต้องแปลงเป็น list ก่อน
tup = list(tup)
tup.sort()
print("tup หลังการเรียงข้อมูล จากน้อยไปมาก => ",tup)

tup.reverse()
print("tup หลังการเรียงข้อมูล จากมากไปน้อย => ",tup)

# แล้วแปลงกลับเป็น tuple
tup = tuple(tup)
print("tup เปลียนกลับเป็น tuple => ",tup)

##############################################################################