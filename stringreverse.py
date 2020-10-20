#string reversed program
def reverse(string):
    reversed_string = ""
    for i in string:
        reversed_string=i+reversed_string
    print("reversed string is:",reversed_string)
string = input("enter string:")
print("entered string",string)
reverse(string)
#given a is reversed like ouput : good is ram
#ex-1:
a='ram is good'
b=a.split()
b.reverse()
a=" ".join(b)
print(a)
#ex-2:
#given string in each letter reversed like outpu: tab tac
f='bat cat'
v=f.split()
r=[]
for x in v:
     r.append(x[::-1])

t=" ".join(r)
print(t)