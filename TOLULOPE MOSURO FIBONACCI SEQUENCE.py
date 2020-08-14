x1=0
x2=1
y1=int(input("Enter the lower range of the length of the sequence"))
y2=int(input("Enter the upper range of the length of the sequence"))
new_list=[]
for i in range(y1,y2+1):
    sums=x1+x2
    new_list.append(sums)
    x1=x2
    x2=sums
print(new_list)
