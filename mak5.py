import sys
import copy
f=open('out.asm','w+')
f1=open(sys.argv[1],'r+')
###### First converting any text file to a normal file of our requirement ######################
l=[]
str1=''
str2=''
str3=''
for i in f1:
	str1=i.split()
	l.append(str1)
g=[]
for i in l:
	if len(i)<=3 and len(i)!=0:
		str6=''
		str4=i[0]
		if len(i)>=2:
			str5=i[1]
			if str5[len(str5)-1]==',' or str5[len(str5)-2]==',' or str5[len(str5)-3]==',':
				for m in range(0,3):
					str6=str6+str5[m]
			else:
				str6=str5
                if str4!="syscall" and str4[len(str4)-1]!=':' and str4!='j' and str4!="la" and str6!="$v0" :
			if str4[0]!='#' and str4[0]!='.':
				print str4[0]
				str2=i[0]+' '
				k=len(i)
				y11=0
                		for j in range(1,k):
                		        y=len(i[j])
                		        str3=i[j]
				        if i[j]=='#' or str3[0]=='#':
						break	
					if len(str3)>=2:
                                                if str3[1]=='#':
							y11=1
							print str,"2"
                                               		for z in range(0,1):
                                                        	str2=str2+str3[z]
                                        if len(str3)>=3:
							
                                                if str3[2]=='#':
							y11=1
							print str3,"3"
                                                        for z in range(0,2):
                                                        	str2=str2+str3[z]
                                        if len(str3)>=4:
							
                                                if str3[3]=='#':
							y11=1
							print str3,"4"
                                                        for z in range(0,3):
                                                        	str2=str2+str3[z]
                                        if len(str3)>=5:
                                                if str3[4]=='#':
							y11=1
							print str3,"4"
                                                        for z in range(0,3):
                                                        	str2=str2+str3[z]

	
	
	                	        if len(i[j])>=3 and str3[y-1]!=',' and y11!=1:
	                	                str2=str2+i[j]
	                		        if(j<k-1 and i[j+1]==','):
	                	                	str2=str2+i[j+1]
	                	        if len(i[j])>=3 and str3[y-1]==',' and y11!=1:
	                			str2=str2+i[j]
					if len(i[j])<=2 and str3[y-1]!=',' and y11!=1:
	                                               	str2=str2+i[j]
	                                               	if(j<k-1 and i[j+1]==','):
	                                                	str2=str2+i[j+1]
	                                if len(i[j])<=2 and str3[y-1]==',' and y11!=1:
	                                              	 str2=str2+i[j]

				f.write(str2)
               	                f.write("\n")
                                g.append(str2)
		
		

	if len(i)>3:
		
		str4=i[0]
		if str4!="syscall" and str4[len(str4)-1]!=':' and str4!='j' :
			if str4[0]!='#' and str4[0]!='.':
				print str4[0]
				str2=i[0]+' '
				k=len(i)
				y22=0
				for j in range(1,k):
					y=len(i[j])
					str3=i[j]
					if i[j]=='#' or str3[0]=='#':   
                                        	break
					if len(str3)>=2:
						if str3[1]=='#':
							y22=1
							print str3,"11"
							for z in range(0,1):
								str2=str2+str3[z]
					if len(str3)>=3:
						if str3[2]=='#':
							y22=1
							print str3,"33"
							for z in range(0,2):
								str2=str2+str3[z]
					if len(str3)>=4:
						if str3[3]=='#':
							y22=1
							print str3,"44"
							for z in range(0,3):
								str2=str2+str3[z]
					if len(str3)>=5:
                                                if str3[4]=='#':
							y22=1
							print str3,"55"
                                                        for z in range(0,3):
                                                               str2=str2+str3[z]

					if len(i[j])>=3 and str3[y-1]!=',' and y22!=1:
						
						str2=str2+i[j]
						if(j<k-1 and i[j+1]==','):
							str2=str2+i[j+1]
					if len(i[j])>=3 and str3[y-1]==',' and y22!=1:
						str2=str2+i[j]
					if len(i[j])<=2 and str3[y-1]!=',' and y22!=1:
                                                str2=str2+i[j]
                                                if(j<k-1 and i[j+1]==','):
                                                        str2=str2+i[j+1]
                                        if len(i[j])<=2 and str3[y-1]==',' and y22!=1:
                                                str2=str2+i[j]

				f.write(str2)
				f.write("\n")
				g.append(str2)
		
			
		
print g
f.close()
f1.close()
############ End of primary conversion #########################	

f=open('out.asm','r+')	
k=0
list1=[]
global dict1
dict1={}
dict1.setdefault("RAW",[])
dict1.setdefault("WAW",[])
dict1.setdefault("WAR",[])
for i in f:
	list1.append(i.split('\n'))
	k+=1
p=''
s=[]
lis1=[]
for i in range(0,k):
	for j in list1[i]:
		s.append(j.split('\n'))	
for h in range(0,len(s)-1):
	try:
		lis1.append(s[2*h])	
	except:
		pass	
l=[]
lis2=[]
g=[]

for i in range(0,len(lis1)):
	if ['syscall'] in lis1:
		lis1.remove(['syscall'])
	elif ['.text'] in lis1:
		lis1.remove(['.text'])
	elif ['main:'] in lis1:
		lis1.remove(['main:'])
	elif ['.data'] in lis1:
		lis1.remove(['.data'])
	elif ['.globl main'] in lis1:
		lis1.remove(['.globl main'])	

f=[]
d=[]
c=''

lis3=[]
for l in lis1:
	for g in l:
		f=g.split(' ' or ',')
		c=','.join(f)
		lis3.append(c.split(','))
print lis3
###### End of Pre-Processing the assembly instructions #####################

flag=[[] for i in range(len(lis3))]
flag1=[[] for i in range(len(lis3))]

def chardel(k):
	s=''
	if k.endswith(')'):
		s=s+k[len(k)-4]+k[len(k)-3]+k[len(k)-2]
	else:
		s=k
	return s

def DepF(flag,flag1,lis3,k,dict1,string,i,r):
	print lis3[k-1],"has" +string +"dependency with",i
        flag[r].append(k-1)
        flag1[r].append(lis3[k-1])
        if lis3[k-1] not in dict1[string]:
        	dict1[string].append(lis3[k-1])
        if i not in dict1[string]:                   
	        dict1[string].append(i)

def adddep(add1,add2,add3,k):
	j=0
	for i in lis3[k:]:
		r=lis3.index(i)
		sum1=0
		if i[0]=='blez' or i[0]=='bltz' or i[0]=='bgtz' or i[0]=='bgez':
			if add1==chardel(i[1]):
				DepF(flag,flag1,lis3,k,dict1,'RAW',i,r)
		if i[0]=='add' or i[0]=='mul' or i[0]=='sub' or i[0]=='addi' or i[0]=='div':
			if add1==chardel(i[1]) :
				DepF(flag,flag1,lis3,k,dict1,'WAW',i,r)
			if add2==chardel(i[1]) :
				DepF(flag,flag1,lis3,k,dict1,'WAR',i,r)
			if add3==chardel(i[1]) :
				DepF(flag,flag1,lis3,k,dict1,'WAR',i,r)
			if add1==chardel(i[2]) :
				DepF(flag,flag1,lis3,k,dict1,'RAW',i,r)
			if  add1==chardel(i[3]):	
				DepF(flag,flag1,lis3,k,dict1,'RAW',i,r)
		if i[0]=='lw' or i[0]=='li' or i[0]=='lb' or i[0]=='move':
			if add1==chardel(i[1]):
				DepF(flag,flag1,lis3,k,dict1,'WAW',i,r)
			if add1==chardel(i[2]):
				DepF(flag,flag1,lis3,k,dict1,'RAW',i,r)
			if add2==chardel(i[1]):
				DepF(flag,flag1,lis3,k,dict1,'WAR',i,r)
			if add3==chardel(i[1]):
				DepF(flag,flag1,lis3,k,dict1,'WAR',i,r)
		if  i[0]=='sw' or i[0]=='sb':
			if add1==chardel(i[2]):
				DepF(flag,flag1,lis3,k,dict1,'WAW',i,r)
			if add2==char(i[2]):
				DepF(flag,flag1,lis3,k,dict1,'RAW',i,r)
			if add3==chardel(i[2]):
				DepF(flag,flag1,lis3,k,dict1,'RAW',i,r)
			if add1==chardel(i[1]):
				DepF(flag,flag1,lis3,k,dict1,'WAR',i,r)
		if i[0]=='beq' or i[0]=='bne' or i[0]=='blt' or i[0]=='bgt':
                        if add1==chardel(i[1]):
				DepF(flag,flag1,lis3,k,dict1,"RAW",i,r)
                        if add1==chardel(i[2]):
				DepF(flag,flag1,lis3,k,dict1,"RAW",i,r)
		
def lwdeep(lw1,lw2,k):
	for i in lis3[k:]:
		r=lis3.index(i)
		if i[0]=='blez' or i[0]=='bltz' or i[0]=='bgtz' or i[0]=='bgez':
			if lw1==chardel(i[1]):
				DepF(flag,flag1,lis3,k,dict1,"RAW",i,r)
		if i[0]=='add' or i[0]=='mul' or i[0]=='sub' or i[0]=='addi' or i[0]=='div' or i[0]=='addu' or i[0]=='addiu':
			if lw1==chardel(i[1]):
				DepF(flag,flag1,lis3,k,dict1,"WAW",i,r)
			if lw1==chardel(i[2]):
				DepF(flag,flag1,lis3,k,dict1,"RAW",i,r)
			if lw1==chardel(i[3]):
				DepF(flag,flag1,lis3,k,dict1,"RAW",i,r)
			if lw2==chardel(i[1]):
				DepF(flag,flag1,lis3,k,dict1,"WAR",i,r)
		if i[0]=='lw' or i[0]=='li' or i[0]=='lb' or i[0]=='move' :
			if lw1==chardel(i[1]):
				DepF(flag,flag1,lis3,k,dict1,"WAW",i,r)
			if lw1==chardel(i[2]):
				DepF(flag,flag1,lis3,k,dict1,"RAW",i,r)
			if lw2==chardel(i[1]):
				DepF(flag,flag1,lis3,k,dict1,"WAR",i,r)
		if  i[0]=='sw' or i[0]=='sb':
			if lw1==chardel(i[2]):
				DepF(flag,flag1,lis3,k,dict1,"WAW",i,r)
			if lw1==chardel(i[1]):
				DepF(flag,flag1,lis3,k,dict1,"RAW",i,r)
			if lw2==chardel(i[2]):
				DepF(flag,flag1,lis3,k,dict1,"WAR",i,r)
		if i[0]=='beq' or i[0]=='bne' or i[0]=='blt' or i[0]=='bgt':
			if lw1==chardel(i[1]):
				DepF(flag,flag1,lis3,k,dict1,"RAW",i,r)
			if lw1==chardel(i[2]):
				DepF(flag,flag1,lis3,k,dict1,"RAW",i,r)
print dict1,"DEP"

def bdeep(lw1,lw2,k):
	for i in lis3[k:]:
		r=lis3.index(i)
		if i[0]=='add' or i[0]=='mul' or i[0]=='sub' or i[0]=='addi' or i[0]=='div':
			if lw1==chardel(i[1]):
				DepF(flag,flag1,lis3,k,dict1,"WAR",i,r)
			if lw2==chardel(i[1]):
				DepF(flag,flag1,lis3,k,dict1,"WAR",i,r)
		if i[0]=='lw' or i[0]=='li' or i[0]=='lb' or i[0]=='move':
			if lw1==chardel(i[1]):
				DepF(flag,flag1,lis3,k,dict1,"WAR",i,r)
			if lw2==chardel(i[1]):
				DepF(flag,flag1,lis3,k,dict1,"WAR",i,r)
		if  i[0]=='sw' or i[0]=='sb':
			if lw1==chardel(i[2]):
				DepF(flag,flag1,lis3,k,dict1,"WAR",i,r)
			if lw2==chardel(i[2]):
				DepF(flag,flag1,lis3,k,dict1,"WAR",i,r)
def bedeep(lw1,k):
	for i in lis3[k:]:
		r=lis3.index(i)
		if i[0]=='add' or i[0]=='mul' or i[0]=='sub' or i[0]=='addi' or i[0]=='div':
			if lw1==chardel(i[1]):
				DepF(flag,flag1,lis3,k,dict1,"WAR",i,r)
		if i[0]=='lw' or i[0]=='li' or i[0]=='lb' or i[0]=='move':
			if lw1==chardel(i[1]):
				DepF(flag,flag1,lis3,k,dict1,"WAR",i,r)
		if  i[0]=='sw' or i[0]=='sb':
			if lw1==chardel(i[2]):
				DepF(flag,flag1,lis3,k,dict1,"WAR",i,r)
for i in range(len(lis3)):
	for j in range(len(lis3[i])):
		try:
			if lis3[i][j]=='lw' or lis3[i][j]=='move' or lis3[i][j]=='lb':
				lw1=lis3[i][j+1]
				lw2=lis3[i][j+2]
				k1=chardel(lw1)
				k2=chardel(lw2)
				fun2=lwdeep(k1,k2,i+1)
			if lis3[i][j]=='li':
				if lis3[i][j+1]=='$v0':
					continue
				else:
					lw1=chardel(lis3[i][j+1])
					lw2='#'
					fun2=lwdeep(lw1,lw2,i+1)
			elif lis3[i][j]=='sw' or lis3[i][j]=='sb':
				lw1=lis3[i][j+1]
				lw2=lis3[i][j+2]
				k1=chardel(lw1)
				k2=chardel(lw2)
				fun2=lwdeep(k2,k1,i+1)	
			elif lis3[i][j]=='add' or lis3[i][j]=='mul' or lis3[i][j]=='div' or lis3[i][j]=='sub' or lis3[i][j]=='addi':
				add1=lis3[i][j+1]
				add2=lis3[i][j+2]
				add3=lis3[i][j+3]
				k1=chardel(add1)
				k2=chardel(add2)
				k3=chardel(add3)
				fun1=adddep(k1,k2,k3,i+1)
			elif lis3[i][j]=='beq' or lis3[i][j]=='bne' or lis3[i][j]=='blt' or lis3[i][j]=='bgt':
				add1=lis3[i][j+1]
				add2=lis3[i][j+2]
				k1=chardel(add1)
				k2=chardel(add2)
				fun3=bdeep(k1,k2,i+1)
			elif lis3[i][j]=='bgtz' or lis3[i][j]=='blez' or lis3[i][j]=='bgez' or lis3[i][j]=='bltz' or lis3[i][j]=='beqz':
				add1=chardel(lis3[i][j+1])
				fun4=bedeep(add1,i+1)
		except:
			pass

print flag ,"Instruction Dependencies"  # Out of order excution sequence

flagult=[]
l1=[]
l1=list(flag)
l3=[]
for i in range(0,len(l1)):
        try:
                flagult.append(0)
        except:
                pass

l5=copy.deepcopy(flag)  #Copying very deeply

def process(l1,flagult):
        k=[]
        for i in range(len(l1)):
                if l1[i]==[] and flagult[i]==0:
                        k.append(i)

        return k
for fun in l1:
                s1=process(l1,flagult)
								      #print s1,"Each Iteration OOO"
                l3.append(s1)
        							      #print flagult,"Flagg"
                for s in s1:
                        position=s
                        flagult[position]=1
                        l1[position].append(-1)
        							      #print l1
                        for k in l1:
                                p1=l1.index(k)
                                for j in range(len(k)):
                                        try:
                                                if k[j]==position and flagult[p1]==0:
                                                        if k.count(position)==1:
                                                                k.remove(k[j])
                                                        else:
                                                                for t in range(k.count(position)):
                                                                        k.remove(position)
                                        except:
                                                pass

print l3,"***********  Out of Order Sequence"

#####Inorder Time#######

ins=list(lis3)
time=[] 									#Inorder Time list
time1=5
time.append(time1)
k=-1
for i in range(0,len(ins)):
	print ins[i]
	if ins[i][0]=='addi' or ins[i][0]=='add' or ins[i][0]=='mul' or ins[i][0]=='sub' or ins[i][0]=='div':
		try:
			ins[i][1]=chardel(ins[i][1])			
			ins[i][2]=chardel(ins[i][2])
			ins[i][3]=chardel(ins[i][3])
			if ins[i+1][0]=='beq' or ins[i+1][0]=='bne' or ins[i+1][0]=='blt' or ins[i+1][0]=='bgt' :
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i+1][1]==ins[i][1] or ins[i+1][2]==ins[i][1]:
					time1+=1
					time.append(time1)
				else:
					time1+=1
					time.append(time1)
			if ins[i+1][0]=='blez' or ins[i+1][0]=='bltz' or ins[i+1][0]=='bgtz' or ins[i+1][0]=='bgez':
				ins[i+1][1]=chardel(ins[i+1][1])
				if ins[i+1][1]==ins[i][1]:
					time1+=1
					time.append(time1)
				else:
					time1+=1
					time.append(time1)
			if ins[i+1][0]=='addi' or ins[i+1][0]=='add' or ins[i+1][0]=='mul' or ins[i+1][0]=='sub' or ins[i+1][0]=='div':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				ins[i+1][3]=chardel(ins[i+1][3])					
				if ins[i][1]== ins[i+1][2] or ins[i+1][3]==ins[i][1] or ins[i][1]==ins[i+1][1] or ins[i+1][1]==ins[i][2] or ins[i+1][1]==ins[i][3]:
					time1+=1
					time.append(time1)
				else:
					time1+=1
					time.append(time1)
			elif ins[i+1][0]=='lw':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][2] or ins[i][1]==ins[i+1][1] or ins[i+1][1]==ins[i][3] or ins[i+1][1]==ins[i][2]:
					time1=time1+1
					time.append(time1)
				else:
					time1+=1
					time.append(time1)
			elif ins[i+1][0]=='move' or ins[i+1][0]=='li':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][2] or ins[i][1]==ins[i+1][1] or ins[i+1][1]==ins[i][3] or ins[i+1][1]==ins[i][2]:
					time1=time1+1
					time.append(time1)
				else:
					time1+=1
					time.append(time1)
	        	elif ins[i+1][0]=='sw':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])				
				if ins[i][1]==ins[i+1][1] or ins [i][1]==ins[i+1][2] or ins[i+1][2]==ins[i][2] or ins[i+1][2]==ins[i][3]:
					time1=time1+1
					time.append(time1)
				else:
					time1+=1
					time.append(time1)
			else:
					time1=time1+1
					time.append(time1)
		except:
			pass
	if ins[i][0]=='lw':
		try:
			ins[i][1]=chardel(ins[i][1])			
			ins[i][2]=chardel(ins[i][2])
			if ins[i+1][0]=='beq' or ins[i+1][0]=='bne' or ins[i+1][0]=='blt' or ins[i+1][0]=='bgt' :
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i+1][1]==ins[i][1] or ins[i+1][2]==ins[i][1]:
					time1+=2
					time.append(time1)
				else:
					time1+=1
					time.append(time1)
			if ins[i+1][0]=='blez' or ins[i+1][0]=='bltz' or ins[i+1][0]=='bgtz' or ins[i+1][0]=='bgez':
				ins[i+1][1]=chardel(ins[i+1][1])
				if ins[i+1][1]==ins[i][1]:
					time1+=2
					time.append(time1)
				else:
					time1+=1
					time.append(time1)
			if ins[i+1][0]=='addi' or ins[i+1][0]=='add' or ins[i+1][0]=='mul' or ins[i+1][0]=='sub' or ins[i+1][0]=='div':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				ins[i+1][3]=chardel(ins[i+1][3])
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][1]==ins[i+1][3] or ins[i][2]==ins[i+1][1]:
					time1=time1+2
					time.append(time1)
				
				else:
					time1=time1+1
					time.append(time1)
			elif ins[i+1][0]=='lw':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][1]:
					time1+=2
					time.append(time1)
				else:
					time1=time1+1
					time.append(time1)
			elif ins[i+1][0]=='move' or ins[i+1][0]=='li':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][1]:
					time1+=2
					time.append(time1)
				else:
					time1=time1+1
					time.append(time1)
			elif ins[i+1][0]=='sw' :
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][2]:
					time1+=2
					time.append(time1)
					
				else:
					time1=time1+1
					time.append(time1)
			else:
				time1+=1
				time.append(time1)
		except:
			pass
	if ins[i][0]=='move' or ins[i][0]=='li':
		try:
			ins[i][1]=chardel(ins[i][1])			
			ins[i][2]=chardel(ins[i][2])
			if ins[i+1][0]=='beq' or ins[i+1][0]=='bne' or ins[i+1][0]=='blt' or ins[i+1][0]=='bgt' :
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i+1][1]==ins[i][1] or ins[i+1][2]==ins[i][1]:
					time1+=1
					time.append(time1)
				else:
					time1+=1
					time.append(time1)
			if ins[i+1][0]=='blez' or ins[i+1][0]=='bltz' or ins[i+1][0]=='bgtz' or ins[i+1][0]=='bgez':
				ins[i+1][1]=chardel(ins[i+1][1])
				if ins[i+1][1]==ins[i][1]:
					time1+=1
					time.append(time1)
				else:
					time1+=1
					time.append(time1)
			if ins[i+1][0]=='addi' or ins[i+1][0]=='add' or ins[i+1][0]=='mul' or ins[i+1][0]=='sub' or ins[i+1][0]=='div':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				ins[i+1][3]=chardel(ins[i+1][3])
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][1]==ins[i+1][3] or ins[i][2]==ins[i+1][1]:
					time1=time1+1
					time.append(time1)
				
				else:
					time1=time1+1
					time.append(time1)
			elif ins[i+1][0]=='lw':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][1]:
					time1+=1
					time.append(time1)
				else:
					time1=time1+1
					time.append(time1)
			elif ins[i+1][0]=='move' or ins[i+1][0]=='li':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])				
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][1]:
					time1+=1
					time.append(time1)
					
				else:
					time1=time1+1
					time.append(time1)
			elif ins[i+1][0]=='sw' :
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][1] or ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][2]:
					time1+=1
					time.append(time1)
					
				else:
					time1=time1+1
					time.append(time1)
			else:
				time1+=1
				time.append(time1)
		except:
			pass
	if ins[i][0]=='beq' or ins[i][0]=='bne' or ins[i][0]=='blt' or ins[i][0]=='bgt' :
		try:
			ins[i][1]=chardel(ins[i][1])			
			ins[i][2]=chardel(ins[i][2])
			if ins[i+1][0]=='addi' or ins[i+1][0]=='add' or ins[i+1][0]=='mul' or ins[i+1][0]=='sub' or ins[i+1][0]=='div':
				ins[i+1][1]=chardel(ins[i+1][1])
				if ins[i+1][1]==ins[i][1] or ins[i+1][1]==ins[i][2]:
					time1+=1
					time.append(time1)
					
				else:
					time1=time1+1
					time.append(time1)
			if ins[i+1][0]=='beq' or ins[i+1][0]=='bne' or ins[i+1][0]=='blt' or ins[i+1][0]=='bgt' :
					time1+=1
					time.append(time1)
			if ins[i+1][0]=='blez' or ins[i+1][0]=='bltz' or ins[i+1][0]=='bgtz' or ins[i+1][0]=='bgez':
					time1+=1
					time.append(time1)
			elif ins[i+1][0]=='sw' or ins[i+1][0]=='sb':
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][2]:
					time1+=1
					time.append(time1)
				else:
					time1=time1+1
					time.append(time1)
			elif ins[i+1][0]=='lw' or ins[i+1][0]=='move' or ins[i+1][0]=='li':
				ins[i+1][1]=chardel(ins[i+1][1])
				if ins[i][1]==ins[i+1][1] or ins[i+1][1]==ins[i][2]:
					time1=time1+1
					time.append(time1)
				else:
					time1=time1+1
					time.append(time1)
			else:
				time1=time1+1
				time.append(time1)
		except:
			pass
				
			
				
	if ins[i][0]=='sw':
		try:
			ins[i][1]=chardel(ins[i][1])			
			ins[i][2]=chardel(ins[i][2])
			if ins[i+1][0]=='beq' or ins[i+1][0]=='bne' or ins[i+1][0]=='blt' or ins[i+1][0]=='bgt' :
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i+1][1]==ins[i][2] or ins[i+1][2]==ins[i][2]:
					time1+=2
					time.append(time1)
				else:
					time1+=1
					time.append(time1)
			if ins[i+1][0]=='blez' or ins[i+1][0]=='bltz' or ins[i+1][0]=='bgtz' or ins[i+1][0]=='bgez':
				ins[i+1][1]=chardel(ins[i+1][1])
				if ins[i+1][1]==ins[i][2]:
					time1+=2
					time.append(time1)
				else:
					time1+=1
					time.append(time1)
			if ins[i+1][0]=='addi' or ins[i+1][0]=='add' or ins[i+1][0]=='mul' or ins[i+1][0]=='sub' or ins[i+1][0]=='div':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				ins[i+1][3]=chardel(ins[i+1][3])
				if ins[i][2]==ins[i+1][1] or ins[i][2]==ins[i+1][2] or ins[i][2]==ins[i+1][3] or ins[i][1]==ins[i+1][1] :
					time1+=2
					time.append(time1)
				else:
					time1=time1+1
					time.append(time1)
			elif ins[i+1][0]=='sw':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][2] or ins[i][2]==ins[i+1][1] or ins[i][2]==ins[i+1][2]:
					time1+=2
					time.append(time1)
				else:
					time1=time1+1
					time.append(time1)
			elif ins[i+1][0]=='lw' or ins[i+1][0]=='move' or ins[i+1][0]=='li':
				ins[i+1][1]=chardel(ins[i+1][1])
				ins[i+1][2]=chardel(ins[i+1][2])
				if ins[i][1]==ins[i+1][1] or ins[i+1][1]==ins[i][2] or ins[i][2]==ins[i+1][2]:
					time1=time1+2
					time.append(time1)
				else:
					time1=time1+1
					time.append(time1)
			else:
				time1=time1+1
				time.append(time1)
		except:
			pass

print ins
print time

#######Out of order time#########

k=0
def func(l5,j,time):
	lu=[]
	maxi=0
	global par
	global ti
	for k in range(len(l5)):
		if j==k:
			for m in l5[k]:
				lu.append(m)
			print lu,"List"
	for n in lu:
		if ins[n][0]=='lw' or ins[n][0]=='sw':
			if maxi<time[n]:
				par=n
				maxi=time[n]
				ti=2
		else:
			if maxi<time[n]:
				par=n
				maxi=time[n]
				ti=1
	time11=time[par]+ti
	return time11	 	

t1=[] 							#OOO Time list
for i in range(len(ins)):
	t1.append(0)
for i in range(len(l3)):
							#print i,"Iter"
	for j in l3[i]:
		if i==0:
							#print j,l3[i]
			t1[j]=5
		else:
			t=func(l5,j,t1)
			t1[j]=t
print t1

CPIinorder=float(max(time)-min(time)+1)/len(ins)
CPIOorder=float(max(t1)-min(t1)+1)/len(ins)
print CPIinorder,"IN"
print CPIOorder,"OUT"
print s

#####----------GUI----------######

from Tkinter import *
import random
import sys
root=[]
root=random.sample(xrange(1000),100)
root[0]=Tk()
root[0].title('Assembler')
root[0].geometry('500x300')
top=Frame(root[0])
top.pack()

ph=PhotoImage(file="ser.png")
l11=Label(top,image=ph)
l11.pack(side=LEFT)


lb=Label(top,text="Currently Running File:"+' ')
lb.pack()

lb1=Label(top,text=sys.argv[1],fg="red")
lb1.pack()

def PrintFile():
	root[8]=Tk()
	root[8].title('File Check')
	top8=Frame(root[8])
	top8.pack()
#	scrollbar = Scrollbar(root)
#	scrollbar.pack( side = RIGHT, fill=Y )
	text=Text(top8,height=100,width=100)
#	text.insert(INSERT,"<<<<----------------------->>>"+'\n')
	f=open(sys.argv[1],'r+')
	for i in f:
		text.insert(INSERT,str(i)+'\n')
	text.insert(END,"End Of File\n")
	text.pack()
#	scrollbar.config(command=text.yview )
	
but8=Button(top,text="Check"+' '+sys.argv[1]+'',command=PrintFile,fg="purple")
but8.pack()
	
#RAW Dep
def PrintRAW():
	root[1]=Tk()
	root[1].title('Read After Write Dependencies')
	top1=Frame(root[1])
	top1.pack()
	text=Text(top1)
	text.insert(INSERT,"RAW dependencies\n")
	text.insert(INSERT,'---------------------------------'+'\n')
	if dict1["RAW"]==[]:
		text.insert(END,"NONE")
		text.pack()
	else:
		for i in dict1["RAW"]:
			text.insert(INSERT,' '.join(i)+'\n')
			text.insert(INSERT,'---------------------------------'+'\n')
		text.insert(END,"End of RAW dependencies")
		text.pack()
but1=Button(top,text="RAW Dependencies",command=PrintRAW,width=30)
but1.pack()

#WAR Dep
def PrintWAR():
	root[2]=Tk()
	root[2].title('Write After Read Dependencies')
	top2=Frame(root[2])
	top2.pack()
	text=Text(top2)
	text.insert(INSERT,"WAR dependencies\n")
	text.insert(INSERT,'---------------------------------'+'\n')
	if dict1["WAR"]==[]:
		text.insert(END,"NONE")
		text.pack()
	else:
		for i in dict1["WAR"]:
			text.insert(INSERT,' '.join(i)+'\n')
			text.insert(INSERT,'---------------------------------'+'\n')
		text.insert(END,"End of WAR dependencies")
		text.pack()
but2=Button(top,text="WAR Dependencies",command=PrintWAR,width=30)
but2.pack()

#WAW Dep
def PrintWAW():
	root[3]=Tk()
	root[3].title('Write After Write Dependencies')
	top3=Frame(root[3])
	top3.pack()
	text=Text(top3)
	text.insert(INSERT,"WAW dependencies\n")
	text.insert(INSERT,'---------------------------------'+'\n')
	if dict1["WAW"]==[]:
		text.insert(END,"NONE")
		text.pack()
	else:
		for i in dict1["WAW"]:
			text.insert(INSERT,' '.join(i)+'\n')
			text.insert(INSERT,'---------------------------------'+'\n')

		text.insert(END,"End of WAW dependencies")
		text.pack()
but3=Button(top,text="WAW Dependencies",command=PrintWAW,width=30)
but3.pack()

#Inorder seq
def PrintIn():
	root[4]=Tk()
	root[4].title('Inorder Sequence Execution')
	top4=Frame(root[4])
	top4.pack()
	text=Text(top4,height=100,width=100)
	text.insert(INSERT,"Instruction"+'          '+"Time Taken"+'\n')
	text.insert(INSERT,'--------------------------------------------------------------------'+'\n')	
	for i in range(len(lis3)):
		try:
			if len(lis3[i])<=3:
				text.insert(INSERT,lis3[i][0]+' '+lis3[i][1]+','+lis3[i][2]+'                   '+str(time[i])+'\n')
				text.insert(INSERT,'--------------------------------------------------------------------'+'\n')
			else:
				text.insert(INSERT,lis3[i][0]+' '+lis3[i][1]+','+lis3[i][2]+','+lis3[i][3]+'        '+str(time[i])+'\n')
				text.insert(INSERT,'--------------------------------------------------------------------'+'\n')
		except:
			pass
	text.insert(END,'\n')
	text.pack()
but4=Button(top,text="Inorder Execution",command=PrintIn,width=30)
but4.pack()


s=list(l3)
di={}
for i in s:
	for j in i:
		di[j]=lis3[j]

print di
	

#Outorder seq
def PrintOOO():
	root[5]=Tk()
	root[5].title('Out Of Order Sequence Execution')
	top5=Frame(root[5])
	top5.pack()
	text=Text(top5,height=100,width=100)
	text.insert(INSERT,"Instruction"+'          '+"Time Taken"+'\n')
	text.insert(INSERT,'--------------------------------------------------------------------'+'\n')	
	for i in di.keys():
		try:
			if len(di[i])<=3:
				text.insert(INSERT,di[i][0]+' '+di[i][1]+','+di[i][2]+'               '+str(t1[i])+'\n' )
				text.insert(INSERT,'--------------------------------------------------------------------'+'\n')
			else:
				text.insert(INSERT,di[i][0]+' '+di[i][1]+','+di[i][2]+','+di[i][3]+'         '+str(t1[i])+'\n')
				text.insert(INSERT,'--------------------------------------------------------------------'+'\n')
		except:
			pass
	text.insert(END,'\n')
	text.pack()
but5=Button(top,text="OOO Execution",command=PrintOOO,width=30)
but5.pack()

def CPin():
	root[6]=Tk()
	root[6].title('Cycle Per Instruction of Inorder')
	top6=Frame(root[6])
	top6.pack()
	text=Text(top6)
	text.insert(INSERT,"Total Cycles:")
	text.insert(INSERT,str(max(time)-min(time)+1)+'\n')
	text.insert(INSERT,"-----------------------------"+'\n')		
	text.insert(INSERT,"No. Of Instructions:")
	text.insert(INSERT,str(len(lis3))+'\n')	
	text.insert(INSERT,"-----------------------------"+'\n') 
	text.insert(INSERT,"CPI of this InOrder Sequence is:\n")
	text.insert(END,CPIinorder)
	text.pack()
but6=Button(top,text="CPI of Inorder",command=CPin,width=30)
but6.pack()

def CPOut():
	root[7]=Tk()
	root[7].title('Cycles Per Instruction of OOO')
	top7=Frame(root[7])
	top7.pack()
	text=Text(top7)
	text.insert(INSERT,"Total Cycles:")
	text.insert(INSERT,str(max(t1)-min(t1)+1)+'\n')
	text.insert(INSERT,"-----------------------------"+'\n') 
	text.insert(INSERT,"No of instructions:")
	text.insert(INSERT,str(len(lis3))+'\n')
	text.insert(INSERT,"-----------------------------"+'\n') 
	text.insert(INSERT,"CPI of this Out of Order Sequence is:\n")
	text.insert(END,CPIOorder)
	text.pack()
but7=Button(top,text="CPI of OOO",command=CPOut,width=30)
but7.pack()

def quit():
	root[0].destroy()
but8=Button(top,text="Exit",fg="blue",command=quit)
but8.pack()

for i in range(0,9):
	try:
		root[i].mainloop()
	except:
		pass
##### End of GUI ########
