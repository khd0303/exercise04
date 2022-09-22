#1
'''student_tuple = (('191101','홍길동','010-123-45xx'),('191102','임꺽정','010-223-45xx')
                 ,('191103','장길산','010-323-45xx'))

a = (student_tuple[0][0],student_tuple[0][1])
b = (student_tuple[1][0],student_tuple[1][1])
c = (student_tuple[2][0],student_tuple[2][1])

dictionary = dict((a,b,c))
print('학생정보 :',dictionary)

num = input('학번을 입력하세요 :')
if num in dictionary:
    print(num,'학생은 ',dictionary[num],'입니다')

elif int(num) < 0:
    print('프로그램을 종료합니다')

else:
    print('해당학번의 학생은 없습니다')

'''
#2
'''t1 = (1,2,3,4,5,1,1,2,4,5,6,7,4,2,1,4,7,7,5)
print('주어진 튜플 :',t1)
sett = set(t1)

t2 = tuple(sett)
print('중복제거 튜플 :',t2)'''

#3

'''money = (100,121,120,130,140,120,122,123,190,125)
num = 0

print('일일 매출기록 :',money)
for i in range(1,len(money)):
    if money[i-1] > money[i]:
        num+=1

print('지난 10일동안 전일대비 매출이 감소한 날은',num,'일 입니다')'''
#4
'''str = input('문자열을 입력하시오 :')

setstr = list(str)

if(setstr[0:int(len(setstr))//2:1] == setstr[int(len(setstr)):int(len(setstr))//2:-1]):
    print('회문입니다')
else:
    print('회문이 아닙니다')
'''
#5
t1 = (5,6,3,9,2,12,3,8,7)
print('before : ',t1)

lst = list(t1)

lst.remove(12)

lst.append(12)

t2 = tuple(lst)

print('after : ',t2)
