a=int(input("item1 cost: "))
b=int(input("item2 cost: "))
c=int(input("item3 cost: "))

sum=a+b+c
if(sum>50):
  sum=sum-(0.1*sum)
print("Total cost: ")
print(sum)
