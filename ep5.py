### เจาะลึกการใช้ List ต่อเนื่อง

##############################################################################
### การนับจำนวนสมาชิก
number=[1,2,3,4,5,6,7,8,9,10] 
fruit=["มะม่วง","มะนาว","มะยม","มะละกอ"]
name=["ก","ข"]

len(number)
print(len(number))
print(len(fruit))

### ใช้ loop มาทำงานร่วมด้วย กับการแจกแจงสมาชิกใน list
#### ใช้ len(fruit) เพื่อรู้ว่าเราจะทำซ้ำกี่รอบ
#### ใช้ len ร่วมกับ loop for
for i in range(len(fruit)):
    print(fruit[i])

### เขียนแบบนี้ก็ได้ แต่จะต่างกัน
for item in fruit:
    print(item)
##############################################################################