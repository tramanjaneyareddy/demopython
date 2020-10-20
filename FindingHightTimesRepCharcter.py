str = "ramanjaneya reddy"
a = {}
for x in str:
    if x in a.keys():
        a[x]+=1
    else:
        a[x]=1
print(a)
num=0
hightrep=""
for x in a.keys():
    if(a[x]>num):
        num=a[x]
        hightrep=x
print("hight times repeted character count: "+hightrep+":",num)






