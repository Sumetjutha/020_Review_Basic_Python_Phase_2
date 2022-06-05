### Tuple

##############################################################################
### การลบข้อมูล del
tup = (1,2,3,4,"JohnTik","มะม่วง",True,3.99) # tuple
print("tup => ",tup)

del tup # ลบไปเลย โดยการ clear memory
# print(tup)


### การลบข้อมูลสมาชิก
tup = (1,2,3,4,"JohnTik","มะม่วง",True,3.99) # tuple
print("tup => ",tup)

# เราจะลบ มะม่วงออกไป
# เราจะใช้ pop หรือ remove โดยแปลงให้เป็น list ก่อน

tup = list(tup) # แปลงให้เป็น list
print("tup => ",tup)
print(type(tup))

## pop
tup.pop()
print("tup หลังการลบโดยใช้ pop => ",tup)

## remove "มะม่วง"
tup = (1,2,3,4,"JohnTik","มะม่วง",True,3.99) # tuple
print("tup => ",tup)

tup = list(tup) # แปลงให้เป็น list
tup.remove("มะม่วง")

print("tup หลังการลบโดยใช้ remove => ",tup)

# แปลงกลับเป็น tuple
tup = tuple(tup)
print("tup => ",tup)
print(type(tup))
##############################################################################