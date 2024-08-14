li=list(map(int,input().split()))
max_ele=li[0]
for num in li:
    if num>max_ele:
        max_ele=num
        print(max_ele)
