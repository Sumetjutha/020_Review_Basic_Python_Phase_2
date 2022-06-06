### SET 

##############################################################################
## SET Operator

# UNION
fruitA = {"กล้วย","มะยม","มะนาว"}
fruitB = {"สตอเบอรี่","กีวี่","มะม่วง"}

allFruit = fruitA.union(fruitB)
print("สมาชิกของ allFruit => ",allFruit)

## อีกวิธีเราก็ใช้ Update
fruitA.update(fruitB)
print("สมาชิกของ fruitA => ",fruitA)


## การ Copy Set
fruitC = fruitA.copy()
print("สมาชิกของ fruitC => ",fruitC)

##############################################################################

##############################################################################
### Difference
fruitA = {"กล้วย","มะยม","มะนาว","แอปเปิ้ล","ทุเรียน"}
fruitB = {"แอปเปิ้ล","สตอเบอรี่","กีวี่","มะม่วง","ทุเรียน","มะม่วง",}

fruitC = fruitA.difference(fruitB)
print("สมาชิกของ fruitC , fruitA ที่ต่างจาก fruitB => ",fruitC)

## ถ้ากรณีไม่ต้องสร้างลงไปใน fruitC
print("fruitA => ",fruitA)
# fruitA.difference(fruitB)
fruitA.difference_update(fruitB)
print("fruitA เมื่อใช้ difference_update => ",fruitA)

##############################################################################

##############################################################################
## Intersection
fruitA = {"กล้วย","มะยม","มะนาว","แอปเปิ้ล","ทุเรียน"}
fruitB = {"แอปเปิ้ล","สตอเบอรี่","กีวี่","มะม่วง","ทุเรียน","มะม่วง",}

fruitC = fruitA.intersection(fruitB)
print("สมาชิกของ fruitC , fruitA ที่เหมือนกับ fruitB => ",fruitC)

fruitA.intersection_update(fruitB)
print("fruitA ที่เหมือนกับ fruitB เมื่อใช้ intersection_update => ",fruitA)

##############################################################################