prime_list = [2,3,5,7]
print('소수목록 : ',prime_list)

prime_list.append(11)
print('추가후 소수목록 : ',prime_list)

print()
print('삭제전 소수목록 : ',prime_list)

prime_list.remove(3)
print('삭제후 소수목록 : ',prime_list)

print()

nations = ['Korea','China','Russia','Malaysia']

print('국가목록 : ',nations)

nations.append('Nepal')
print('추가후 국가목록 : ',nations)

print()

if ('Japan' in prime_list):
    print('Japan은 리스트 내에 있습니다')
else:
    print('Japan은 리스트 내에 없습니다')

if ('Russia' in prime_list):
    print('Russia는 리스트 내에 있습니다')
else:
    print('Russia는 리스트 내에 없습니다')
