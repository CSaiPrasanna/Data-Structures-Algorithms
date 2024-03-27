#selection_sort
def selection_sort(arr):
    n=len(arr)
    for i in range(0,n-1):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
                arr[i],arr[min]=arr[min],arr[i]


s=int(input("enter number of elements:"))
arr=[]
for i in range(0,s):
      a=int(input("enter the element:"))
      arr.append(a)
selection_sort(arr)
print(arr)



'''Time complexity:
worst case:0(n**2)
average case:0(n**2)
best case:0(n**2))
space complexcity:0(1)
stable sorting algorithm'''
