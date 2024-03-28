#insertion sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j]and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j=j-1

        
        


n=int(input("enter number of elements:"))
arr=[]
for i in range(0,n):
    s=int(input("enter the element:"))
    arr.append(s)
insertion_sort(arr)
print(arr)



#time complexities
'''worst_case : o(n^2)
        average_case:o(n^2)
        best_case:o(n)'''
