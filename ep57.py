## Fibonacci Number

########################################################################################################################
## โดยใช้ Recursive Function
## 0, 1 ,1 ,2 ,3 ,5 , 8
## f0 = ? , f1 = ?
def fibonacci(number):
    if number <= 1 :
        # เลข 2 ลำดับแรก
        return number
    else :
        ## เลขลำดับถัดไป
        return fibonacci(number-1) + fibonacci(number-2)

for i in range(10): #  0 ,1 ,1 ,2 , 3 
    # 0 - 4
    print(fibonacci(i))  

x = [fibonacci(i) for i in range(10)]

print("list ของ fibonacci => ",x)

'''
i = 0 
i = 1
i = 2
'''


########################################################################################################################