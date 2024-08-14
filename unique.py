data=[2,3,3,4,2,5]
for i in range(len(data)):
    c=0
    for j in range(len(data)):
        if data[i]==data[j]:
            c=c+1
    if c==1:
        print(data[i])

