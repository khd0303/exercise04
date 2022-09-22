fruit_dic = {'apple':6000,'melon':3000,'banana':5000,'orange':4000}

print(list(fruit_dic.keys()))
print(list(fruit_dic.values()))
print('fruit_dic 딕셔너리의 항목의 개수 :',len(fruit_dic))

if('apple' in fruit_dic):
    print('apple is in fruit_dic')
else:
    print('apple is not in fruit_dic')

if('mango' in fruit_dic):
    print('mango is in fruit_dic')
else:
    print('mango is not in fruit_dic')
