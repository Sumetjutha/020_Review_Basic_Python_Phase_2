### หากลุ่มเลขคู่ / เลขคี่

##############################################################################
number = list([])
odds = list([]) # สร้างกลุ่ม เลขคี่
even = list([]) # สร้าง

while True: # ให้ทำงานตลอดเวลา
    x = int(input("ป้อนตัวเลขของคุณ : "))
    if x<0:
        break
    if x%2 == 0:
        even.append(x)
    else:
        odds.append(x)
    number.append(x)

print("list of number is => ",number)
print("list of even is => ",even)
print("list of odds is => ",odds)
print("End")


##############################################################################