"""
f= open("myfile.txt","w")

for i in range(1,4):
    name=input("Enter Subject : ")
    f.write("\n"+name)
"""    
"""
f= open("myfile.txt","a")

for i in range(1,4):
    name=input("Enter Subject : ")
    f.write("\n"+name)
"""

f=open("myfile.txt","r")

count=0
for i in f.readlines():
    count+=1

print(count)
