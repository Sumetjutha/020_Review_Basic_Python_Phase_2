### FrozenSet

##############################################################################
fruit = set(["มะม่วง","มะยม","มะนาว"])
print("fruit => ",fruit)

fruit.add("ทุเรียน")
print("fruit => ",fruit)

fruit.discard("มะยม")
print("fruit => ",fruit)

## FrozenSet ==> จะลบหรือเพิ่มข้อมูลไม่ได้
fruitA = frozenset(["มะม่วง","มะยม","มะนาว"])
print("fruitA => ",fruitA)

for item in fruitA:
    print("ข้อมูล => ",item)
##############################################################################