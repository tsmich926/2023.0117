# 1-4 특정수의 배수찾기
# result=[]
# for i in range(10):
#     if i%2==0:
#         result.append()
#     if i%7==0:
#         result.append()
# print(result)

# S_triangle=list(map(int,input().split()))
# print(S_triangle)
# for i in range(len(S_triangle)):
#     if S_triangle[i]==S_triangle[i+1] and S_triangle[i]==S_triangle[i+2]:
#         print("d")

# triangle=list(map(int,input().split()))
# S_triangle=sorted(triangle)
# if S_triangle[0]+S_triangle[1]>S_triangle[2]:
#     print("삼각형")
#     if S_triangle[0]==S_triangle[1] and S_triangle[1]==S_triangle[2]:
#         print("정삼각형")
#     elif S_triangle[0]==S_triangle[1] or S_triangle[1]==S_triangle[2]or S_triangle[0]==S_triangle[2]:
#         print("이등변")
#     elif S_triangle[2]**2== S_triangle[0]**2 + S_triangle[1]**2:
#         print("직각삼각형")
# else:
#     print("삼각형x")

d={}
s={'a','b','c','d'}
for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c]=1
print(d)
