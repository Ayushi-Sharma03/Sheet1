#Q2:

#5**9=1953125
#3//2=1
#7//3=2
#7/3=2.3333333333333335
#6==6 = True
#a=20; a+=30; a%=3; print(a) = 2
#True * False = 0
#True & False = False
#True and False = False
#((6>3) and (7<4) or(18==3)) and (9>3)
#True is False = False
#False in 'False' = error
#((True==False) or (False>True)) and (False<=True)


#Q3:

s1="Nice to have it"
s2="here"
print("3. Output : ",s1,s2)


#Q4:

a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
i1=a[3]
i2=i1[1]
i3=i2[2]
index=i3[0]
print("\n4. Output : ",index)


#Q5:

a.insert(0,s1)
a.append(s2)
print("\n5. New List : ",a)


#Q6:

numbers=[386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,67,104,58,512,24,892,894,767,553,81,379,843,831,445,742,717,958,743,527]
print("\n6. Even Numbers :")
for i in numbers:
    if i%2==0:
        print(i)
    if i==237:
        break


#Q7:

color_list_1=set(["White","Black","Red"])
color_list_2=set(["Red","Green"])
print("\n7. Output : ",color_list_1.difference(color_list_2))


#Q8:

def check_Pangram(st):
    alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in alphabets:
        if c not in st.upper():
            return False
    return True
str=str(input("\n8. Enter a String : "))
if(check_Pangram(str)==True):
    print("The entered String is Pangram.")
else:
    print("The entered String is not a Pangram.")


#Q9:

n=input("\n9. Enter a Number : ")
sum=int(n)+int(n*2)+int(n*3)
print("Output : ",sum)


#Q10:

nums = input("\n10. Enter the Input : ")
sp = nums.split("#")
for i in range(len(sp)):
    sp[i]=sp[i].split(" ")
sp_x=sp[0]
sp_y=sp[1]
x=[]
y=[]
for i in sp_x:
    x.append(int(i))
for i in sp_y:
    y.append(int(i))
print("x = ",x)
print("y = ",y)


#Q11:

w=input("\n11. Enter words seperated with commas : ")
ilist=w.split(",")
ilist.sort()
flist=','.join(ilist)
print("Output : ",flist)


#Q12:

d={'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 'Marks': [57,87,67,79]}
s=d['Student']
m=d['Marks']
mm=max(m)
ind=m.index(mm)
print("\n12. Output : ", s[ind])


#Q13:

sen=input("\n13. Enter a Sentence : ")
l= 0
dig= 0
for i in sen:
    if i.isalpha()==True:
        l+=1
    if i.isdigit()==True:
        dig+=1
print("Number of letters : ",l)
print("Number of digits : ",dig)


#Q14:

d={'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'], 'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'], 'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
name=d['Name']
subj=d['Subject']
rat=d['Ratings']
input=input("\n14. Input: ")
n=[]
s=[]
r=[]
len=subj.count(input)
for i in range(len):
    ind= subj.index(input)
    n.append(name[ind])
    s.append(subj[ind])
    r.append(rat[ind])
    del name[ind]
    del subj[ind]
    del rat[ind]
nlist= dict()
nlist['Name'] = n
nlist['Subject'] = s
nlist['Ratings'] = r
print("\nOutput : ",nlist)


#Q15:

n=input("\n15. Enter an Integer: ")
num=int(n)
divi= [i for i in range(0,num) if(i%7==0)]
print(divi)

def divisible(n):
    for i in range(n): 
        if i%7==0:
            val=True
        else:
            val=False
        print(i,val)

divisible(num)


#Q16:

import math

x, y = 0, 0

while True:
    step=input("Type in UP/DOWN/LEFT/RIGHT #step number: ")

    if step=="":
        break

    else:
        step = step.split(" ")
        

        if step[0]=="UP":
            y=y+int(step[1])
        elif step[0]=="DOWN":
            y=y-int(step[1])
        elif step[0]=="LEFT":
            x=x-int(step[1])
        elif step[0]=="RIGHT":
            x=x+int(step[1])

c=math.sqrt(x**2 + y**2)

print("Distance:", c)

