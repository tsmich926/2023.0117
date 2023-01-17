
#! 2023.01.17
#?
#!
#, 

#? 홀 짝 판별
# num = int(input())
# if num % 2==1 :
#     print('홀')
# else :
#     print('짝')


#?주어진 숫자전까지 출력
# n=0
# while True:
#     if n==3:
#         break
#     print(n)
#     n+=1

#?2부터9까지만 문자열출력,숫자 0-9까지 출력
# for i in range(10):
#     if i >1 :
#         print('0과1빼고')
#     print(i)

#?문자열에 원하는 알파벳이 존재하는지 찾기
# for char in 'avsdfjsd':
#     if char in 'a':
#         print('a존재')
#         break
#     else :
#         print('없음')

#?입력받은 문자열에 원하는 알파벳이 존재하는지 찾기
# st = input()
# for char in st:
#     if char in 'a':
#         print('a')
#         break
#     else:
#         print('x')

#? 한줄 조건 표현식
# num=-5
# value=num if num>=0 else 0
# print(num)

#? 합출력
# sum=0
# i=0
# while i<10 :
#     i+=1  
#     sum= sum+i
# print(sum)

#?입력받은 숫자 한줄씩 각각 출력하기
# chars = input()
# for char in range(len(chars)):
#     print(chars[char])

#?딕셔너리 키값출력
# grades= {'korea':80, 'eng':70}
# for student in grades:
#     print(student)

#?딕셔너리 키와 밸류값 출력
# grades= {'kor':80, 'eng':70}
# for student in grades:
#     print(student,grades[student])

#?딕셔너리 순회
# print(grades.keys())
# print(grades.values())
# print(grades.items())

#?enumerate()함수
#?인덱스와 객체를 쌍으로 담은 열거형 객체 반환
#?(index,value)형태의 튜플로 구성된 열거객체를 반환
# member= ['민수','영','철']
# for i, number in enumerate(member):
#     print(i,number)

#?list comprehension
"""[code for 변수 in interable]"""
#?반복가능한 객체에서 하나를 변수에 할당,코드를 실행한 결과를 list에 담아준다

#? 1부터 3의 세제곱 결과가 담긴 리스트 만들기
# cu_list=[]
# for number in range(1,4):
#     cu_list.append(number**3)
# print(cu_list)

#? 위의 코드를 간결하게
# cu_list = [number**3 for number in range(1,4)]
# print(cu_list)

#? dict comprehension
#? 1-3 세제곱 딕셔너리만들기
# cu_dict={}
# for number in range(1,4):
#     cu_dict[number]=number**3
# print(cu_dict)

# ? 간결 version
# cu_dict={number:number**3 for number in range(1,4)}
# print(cu_dict)

"""반복문 제어"""
# for num in range(10):
#     if num==5:
#         break
#     print(num)

# break :반복문종료
# ! continue: 건너뛰기 컨티뉴이후의 코드블록은 수행x 다음반복 수행
# for-else: 끝까지 반복문 실행한 이후에 else문 실행
# ! pass:아무것도 하지 않음

# 1)1부터 사용자가 입력한 양의 정수까지의 총합을 구하는 코드를 작성해보세요.
# 2)사용자로부터 입력 받은 양의 정수의 각 자리 수를 1의 자리부터 차례대로 출력하는 코드를 작성해보세요.

# 1)
# 2) numbers= input()
# for i in reversed(range(len(numbers))):
#     print(numbers[i])

# if 조건():
#     조건이 true면 문장수행
# else:
#     조건이 false면 수행

# idx=0
# while idx<=5:
#     print(idx)
#     idx+=1
# print('end')

# idx=0
# while True:
#     if a<0:

#         break #?23번째를 빠져나가는 break
#     print('end')

# if a<10:
#     if b<10:
#         break #?반복문이 없으므로 오류이다. break는 반복문을 빠져나간다

# if a<10:
#     pass
# elif b<10:
#     pass
# else:
#     pass
# print()

# print('end')

# continue는 반복이 시작하는 곳으로 돌아간다.
# 23번째 라인으로 간다

# break가 있으면 while 반복을 빠져나간다.

#!1-2 평균구하기
# score['algorithm']=90
# score['python']=85
# keyL=score.keys()
# valueL=score.values()
# lenV=len(score)
# sumV=sum(score.values())
# print(sumV//lenV)

#! 1-4 자릿수출력예제
# s=input('숫자를 입력해주세요:') #입력받으면 문자열이 된다.
# intL=list(map(int,s))
# print(sum(intL))
# ---------------------------------------
# enumerate()
# l = [1,2,3]
# l.append()

# x,y,z=1,2,3
# print(x,y,z)

# x=1,2
# print(x) #?튜플로 저장된다  가능

# x,y=1 #?불가능

# x,y = 1,2,3
# print(x,y) #?불가능

# x,*y = 1,2,3
# print(x,y)
#?가능. y의 타입이 list가 된다

# maxV= max(1,3,4,5,8-2)
#가능

s='i am ssafy'
print(s.capitalize()) #문장의 첫번째만 대문자로 한다.
print(s.find('a',3)) #3부터 시작해서 a를 찾아라

#!과제 윤년판별 3-2
year = input()
if year%4==0 and year%100!=0:
    print("윤년")
elif year%400 ==0 :
    print("윤년")
else:
    print("윤년이 아닙니다")

#!과제 끝말잇기
