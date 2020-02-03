
arr=[88,7,5,8,45]
print("Before sorting",arr)    
	
for i in range(0,len(arr)-1):
	for j in range(0,len(arr)-1):
		if(arr[j]>arr[j+1]):
			temp=arr[j]
			arr[j]=arr[j+1]
			arr[j+1]=temp
		print("i:",i,"j:",j,"\t arr:",arr)

print("After sorting",arr)
	
		