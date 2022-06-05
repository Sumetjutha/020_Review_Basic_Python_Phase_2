### Assignment 8 : จับคู่สินค้าและราคา

##############################################################################
fruit = ["มะม่วงดอง","แตงโมปั่น","ฝรั่งแช่บ๊วย"]
price = [50,30,15]
print("list of fruit => ",fruit)
print("list of price => ",price)

# function zip ใช้ในการวนลูปรอบ
for x,y in zip(fruit,price):
    print("สินค้า =>",x , "ราคา =>", y)
print("End")

## เรียงจาก ราคาต่ำสุดไปมากสุด แล้วค่อยเชื่อมกับ fruit
for x,y in zip(fruit,price[::-1]):
# price.reverse()
# price.sort()
# for x,y in zip(fruit,price):
    print("สินค้า =>",x , "ราคา =>", y)
print("End")
##############################################################################