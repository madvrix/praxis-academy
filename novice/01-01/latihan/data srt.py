x=[6,5,4,3,2,1]
for i in range(5):
    for j in range(5):
        if x[i]>x[j-1]:
            y=x[i]
            x[i]=x[j-1]
            x[j-1]=y
x
