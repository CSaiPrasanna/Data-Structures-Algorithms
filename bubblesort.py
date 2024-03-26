def bubble_sort(a):
    l=len(a)
    for i in range(0,len(a)):
        swapped=False
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swapped=True
        if swapped==False:
            break
n=int(input("enter number of elements:"))
a=[]
for i in  range(0,n):
    s=int(input("enter ele:"))
    a.append(s)
bubble_sort(a)
print(a)


'''Time complexity:
worst case:0(n2)
average case:0(n2)
best case:0(n)
space complexcity:0(1)
stable sorting algorithm'''

