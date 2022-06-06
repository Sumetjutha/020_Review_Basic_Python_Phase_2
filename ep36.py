### Dictionary

##############################################################################
## ข้อมูลภายในแตกต่างกันได้

## list, tuple
lis = list(["แดง","เหลือง","เขียว"])
tup = tuple(["แดง","เหลือง","เขียว"])
print("lis => ",lis)
print("tup => ",tup)

print(lis[0])
print(tup[0])

## dictionary เรา design index ขึ้นมาได้
# dictionary => key (การเข้าถึงข้อมูล) , value (ค่าของข้อมูล)
# list, tuple => index, value
# ชื่อตัวแปร = {key:value,key:value,key:value}
colors = {"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว",98:"บ้านแสนสุข",100:"บ้านป่า"}
print(colors["red"])
print(colors[98])

city = {"bangkok":"กรุงเทพ"}
print(city["bangkok"])

animal = {"ไก่":"chicken","แมว":"cat","dog":"หมา"}
print(animal["ไก่"])

student = {"ก้อง":40,"โจ้":50,"โค้ช":100}
print(student["ก้อง"])

room = {300:"A",301:"B",302:"C"}
print(room[300])


###### การสร้างแบบ constructor
pet = dict(cat="แมว",dog="หมา",duck="เป็ด")
print("pet => ",pet)
print(pet["dog"])

### การเข้าถึง ข้อมูลโดยใช้ [] หรือ .get ก็ได้
print(pet.get("cat"))

colors = {"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว",98:"บ้านแสนสุข",100:"บ้านป่า",True:"โสด",False:"แต่งงานแล้ว"}
print(colors.get(True))

##############################################################################