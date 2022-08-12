list=[6,2,3,4,5,1]
for i in range(0, len(list)-1):
    for j in range(0, len(list)-i-1):
        if  list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print('hahha')
print(123456)
print(list)