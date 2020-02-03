import random

def bubble_sort(a):
	for i in range(0,len(a)-1):
		for j in range(0,len(a)-1):
			if a[j] > a[j+1]:
				temp = a[j]
				a[j]=a[j+1]
				a[j+1]=temp
			
			print("[i]=",i,"[j]=",j, "\t arr = ", a)
	
	print("Sorted list are : ", a)


a=[]
n=int(input("Enter number of Elements:"))
for i in range(n,0,-1):
	a.append(i)
print(a)
bubble_sort(a)

			



