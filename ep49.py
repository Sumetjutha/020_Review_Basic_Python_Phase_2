### List Parameter

########################################################################################################################
## list ก็สามารถทำงานได้
def displayFruit(item):
    # print(item)
    for i in range(len(item)):
        print("ผลไม้ชิ้นที่ ",i+1," คือ =>", item[i])

fruit=["มะม่วง","มะละกอ","ฝรั่ง","มะนาว"]

displayFruit(fruit)
print("End")

## tuple ก็สามารถทำงานได้
def displayFruitTuple(item):
    for i in range(len(item)):
        print("ผักชิ้นที่ ",i+1," คือ =>", item[i])

vegetable = ("ชะอม","แตงกวา","คะน้า")
displayFruitTuple(vegetable)

#######################################################################################################################