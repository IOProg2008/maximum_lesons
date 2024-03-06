a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

in_list=[a,b,c,d,e]
out_list=[]

for i in in_list:
    f=i**2
    out_list+f

print(sorted(out_list,reverse=True))