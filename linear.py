#searching Technique1
#linear search
def linear(a,ele):
    for i in range(0,len(a)):
        if a[i]==ele:
            print("ele {} is found in pos {}".format(ele,i))
            break
    else:
        print("element not found")
#enter the number of elements 
n=int(input("enter a number:"))
a=[]
for i in range(0,n):
    s=int(input())
    a.append(s)
#enter the key element to search
ele=int(input())
linear(a,ele)




#"Time complexity:0(n)"
