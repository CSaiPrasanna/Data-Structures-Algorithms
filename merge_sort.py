#merge sort Algorithm
def merge_sort(arr):
    if len(arr)>1:
        l=arr[:len(arr)//2]
        r=arr[len(arr)//2:]
        #recursion
        merge_sort(l)
        merge_sort(r)
        #merge
        i=0#left arr index
        j=0#right arr index
        k=0 # merged array index
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j=j+1
            k=k+1
        while i <len(l):
            arr[k]=l[i]
            i=i+1
            k=k+1
        while j<len(r):
            arr[k]=r[j]
            j=j+1
            k=k+1


n=int(input("enter no of elements:"))
arr=[]
for i in range(0,n):
      s=int(input())
      arr.append(s)
merge_sort(arr)
print(arr)



#time complexity:0(n*logn)
