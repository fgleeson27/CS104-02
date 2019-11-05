n=[]
sum=0
avg=0
count=0
for x in range (0,20):
    n=input ("Enter a number:")
    n=int(n)
    sum=sum+n
    count=count+1
    print()
print("Sum of 20 numbers=",sum)
avg=sum/count
print("Average is=", avg)
