#1
'''list1 = [3,5,7]
list2 = [2,3,4,5,6]

for i in range(len(list1)):
    for j in range(len(list2)):
        print(list1[i], '*' ,list2[j], '=',list1[i] * list2[j])


'''


#3

'''n_list = [10,20,30,50,60]

print(n_list)
sum = 0
for i in range(len(n_list)):
    sum += n_list[i]
print('리스트 원소들의 합 = ',sum)
'''


#4
'''
n_list = [10,20,30,50,60]

print(n_list)
num = 0
for i in range(len(n_list)):
    if n_list[i] >= num:
        num = n_list[i]


print('리스트 원소들중 최댓값: ',num)
'''


#5
'''
#(1)
s_list = ['abc','bcd','bcdefg','abba','cddc','opq']
num_min = 9999
num_max = 0
j = 0
for i in range(len(s_list)):
    #print(len(s_list[i]))

    if (num_min > len(s_list[i])):
        num_min =len(s_list[i])


for i in range(len(s_list)):
    if len(s_list[i]) == num_min:
        print('가장 길이가 짧은 문자열 : ',s_list[i])
        break

for i in range(len(s_list)):

    if (num_max < len(s_list[i])):
        num_max =len(s_list[i])


for i in range(len(s_list)):
    if len(s_list[i]) == num_max:
        print('가장 길이가 긴 문자열 : ',s_list[i])
        break


#(2)

s_list.sort(key=len)

print('가장 길이가 짧은 문자열 : ',end = '')
for i in range(len(s_list)):
    if len(s_list[i]) == num_min:
        print(s_list[i], end = ' ')
'''
#6

num = int(input('n을 입력하세요'))

print(num,'개의 수를 입력하시오 ')
lst1 = []
for i in range(num):
    lst1.append(int(input()))


print('합 :' ,sum(lst1), '평균 :',sum(lst1)/len(lst1), '최댓값 :',max(lst1),'최솟값 :',min(lst1))


