
#Searching Technique 2
#Binary Search
#by iteration method
def binary_search(arr,ele):
    a=sorted(arr)
    low=0
    high=len(arr)-1
    #mid=(low+high)//2
    while(low<=high):
        mid=(low+high)//2
        if a[mid]==ele:
            print("ele found in pos",mid)
            break
        elif ele>a[mid]:
            low=mid+1
        elif ele<a[mid]:
            high=mid-1
    else:
        print("not found")
n=int(input("enter  number"))
arr=[]
for i in range(0,n):
    s=int(input())
    arr.append(s)
ele=int(input())
binary_search(arr,ele)








#by using recursion 

def binary_search(arr,ele,l,h):
    while(l<=h):
        mid=l+h//2
        if arr[mid]==ele:
            return mid
        elif arr[mid]>ele:
            return binary_search(arr,ele,l,mid-1)
        elif arr[mid]<ele:
            return binary_search(arr,ele,mid+1,h)
    else:
        return -1


n=int(input("enter  number"))
arr=[]
for i in range(0,n):
    s=int(input())
    arr.append(s)
arr=sorted(arr)
ele=int(input())
print(binary_search(arr,ele,0,n-1))
    
      

            
