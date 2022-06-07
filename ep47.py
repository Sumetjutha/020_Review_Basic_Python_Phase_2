### Keyword Argument

########################################################################################################################

def displayData(fname,lname,city):
    print("ชื่อ => ",fname)
    print("นามสกุล => ",lname)
    print("จังหวัด => ",city)

displayData("John","Tik","Intamara 44")
print("End")

displayData("Jojo","Bangkok","Jotaro")
print("End")

# Keyword Argument
displayData(fname="Jojo",city="Bangkok",lname="Jotaro")
print("End")

########################################################################################################################