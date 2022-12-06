row=int(input("Enter the value of Rows : "))
col=int(input("Enter the value of Columns : "))
last=row*col
test = list(range(1,last+1))
for i in range(1,len(test)):
    if i%3==0:
        if i==last:
            pass
        else:
            test[i-1],test[i]=test[i],test[i-1]
l=[]
m=[]
n=[]
for i in range(0,len(test)):
    if i%3==0:
        l.append(test[i])
    elif i%3==1:
        m.append(test[i])
    else:
        n.append(test[i])
print(l)
print(m)
print(n)