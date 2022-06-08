A = list[2,2,5,6,9,8]

A = list(range(100000))

def solution(A):
    uniqueInt = list([x for x in A if A.count(x) == 1])
    return uniqueInt[0]

print(solution(A))

# def solution(A):
#     # write your code in Python 3.6
    
#     uniqueInt = list([x for x in A if A.count(x) == 1])
    
#     return uniqueInt[0]

# print(solution(A))