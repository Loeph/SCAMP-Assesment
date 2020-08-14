x1=0
x2=1
sequence_length=int(input("Enter the length of the sequence: "))
new_list=[]
for i in range(sequence_length+1):
    sums=x1+x2
    new_list.append(sums)
    x1=x2
    x2=sums
print(new_list)
