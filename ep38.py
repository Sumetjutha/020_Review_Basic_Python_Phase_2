### Dictionary

##############################################################################
## การวนลูป
colors = dict({"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว",98:"บ้านแสนสุข",100:"บ้านป่า",True:"โสด",False:"แต่งงานแล้ว"})

# แบบนี้จะได้แค่ key ของ colors ออกมา
for item in colors:
    print(item)

# แบบนี้จะได้ value ของ colors ออกมา
for item in colors.values():
    print(item)

# ถ้าอยากได้ทั้ง key และ value
for item in colors.items():
    print(item)

# หรือจะเขียนแบบนี้ก็ได้
for k,v in colors.items():
    print("key =>",k," : value => ",v)

##############################################################################

##############################################################################
### การลบข้อมูลออกจาก Dictionary
## pop 
colors.pop("red")
print("color หลังใช้ pop => ",colors)

## popitem จะเอาข้อมูลล่าสุดที่ถูกเพิ่มเข้าไปเอาออกไป
colors.update({"black":"สีดำ","salmon":"สีส้มแซลมอน","red":"สีชมพู"})
colors.popitem()
print("color หลังใช้ popitem => ",colors)
colors.popitem()
print("color หลังใช้ popitem => ",colors)

## การใช้ clear จะทำการล้างสมาชิก เหลือเป็น dictionary เปล่าๆ
colors.clear()
print("color หลังใช้ clear => ",colors)

## การใช้ del คือการลบทิ้งไปทั้งยวงเลย
del colors
# print("color หลังใช้ del => ",colors) # มันจะ error เพราะมันถูกลบไปแล้ว
##############################################################################

##############################################################################
## การคัดลอก dictionary โดยใช้ copy()
colors = dict({"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว",98:"บ้านแสนสุข",100:"บ้านป่า",True:"โสด",False:"แต่งงานแล้ว"})

x = colors.copy()
print("x => ",x)

##############################################################################