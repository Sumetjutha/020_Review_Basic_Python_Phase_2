### Default Parameter

########################################################################################################################
# การกำหนดค่าเริมต้นให้กับ parameter

def displayData(fname,lname,city="กรุงเทพ"): # กำหนดถ้าไม่ป้อนให้เป็นกรุงเทพ
    print("ชื่อ => ",fname)
    print("นามสกุล => ",lname)
    print("จังหวัด => ",city)

displayData("John","Tik","Intamara 44")
print("End")

displayData(fname="Jojo",city="Bangkok",lname="Jotaro")
print("End")

displayData(fname="Martin",lname="Odegaard")
print("End")


########################################################################################################################