### Assignment 7 : จับคู่คำทักทาย / บุคคล

##############################################################################
'''
Hi, Hello

Tik, John

Hi Tik, Hi John, Hello Tik, Hello John
'''

greeting = ["สวัสดี","Hi","Hello","Good Bye"]

people = ["Tik","John","Sumet"]

result = list([])

### เขียนแบบปกติ
for x in greeting:
    # print(x)
    for y in people:
        # print(y)
        result.append(x+" "+y)
        # print(result)

print("ผลลัพธ์ของการทักทาย/จับคู่บุคคล, เขียนแบบปกติ => ",result)
print("End")


### เขียนแบบลดรูป
greeting = ["สวัสดี","Hi","Hello","Good Bye"]

people = ["Tik","John","Sumet"]

result = list([x+" "+y for x in greeting for y in people])

print("ผลลัพธ์ของการทักทาย/จับคู่บุคคล, เขียนแบบลดรูป => ",result)
print("End")
##############################################################################