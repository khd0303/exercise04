a = [1,2,3]
b = [10,20,30]
a.append(b)

print(a)


a = [1,2,3]
b = [10,20,30]

a.extend(b)
print(a)

nlist = list(range(1,11))

print('nlist = ',nlist)

nlist.insert(0,0)
print('nlist = ',nlist)

nlist.reverse()
print('nlist = ',nlist)

print('마지막원소 : ',nlist[-1])
nlist.pop()
print('nlist = ',nlist)
